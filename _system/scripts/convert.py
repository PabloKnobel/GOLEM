#!/usr/bin/env python3
"""Convert an inbox item to text and store it in raw/.

Usage:
    python _system/scripts/convert.py <input_file> [--vault .] [--type papers|decks|docs|web|notes|refs]
                                      [--slug SLUG] [--no-images] [--move]

Writes  raw/<type>/<slug>.<ext>  (original copy) and  raw/<type>/<slug>.md  (text),
appends a row to _system/manifest.csv, and prints a JSON summary to stdout.
Skips (status "duplicate") if the file's sha256 is already in the manifest.

Requirements: pip install pymupdf4llm python-pptx ; pandoc ; optional tesseract + libreoffice.
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TYPE_BY_EXT = {
    ".pdf": "papers", ".pptx": "decks", ".ppt": "decks", ".docx": "docs", ".doc": "docs",
    ".html": "web", ".htm": "web", ".md": "notes", ".txt": "notes",
    ".ris": "refs", ".xml": "refs", ".enw": "refs",
}
MANIFEST_FIELDS = ["sha256", "original_name", "raw_path", "text_path", "type", "added", "status", "pages", "method"]
MIN_CHARS_PER_PAGE = 200  # below this, a PDF page is treated as scanned and OCR'd


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s[:80] or "item"


def read_manifest(path: Path):
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def append_manifest(path: Path, row: dict):
    new = not path.exists()
    with path.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)


def convert_pdf(src: Path):
    import pymupdf  # installed with pymupdf4llm
    import pymupdf4llm
    doc = pymupdf.open(src)
    pages = doc.page_count
    md = pymupdf4llm.to_markdown(str(src), page_chunks=True)
    out, ocr_pages = [], []
    for i, chunk in enumerate(md):
        text = chunk.get("text", "")
        if len(text.strip()) < MIN_CHARS_PER_PAGE and shutil.which("tesseract"):
            text = ocr_page(doc[i])
            ocr_pages.append(i + 1)
        out.append(f"\n\n<!-- page {i + 1} -->\n\n{text}")
    method = "pymupdf4llm" + (f"+ocr(pages {ocr_pages})" if ocr_pages else "")
    return "".join(out), pages, method


def ocr_page(page) -> str:
    with tempfile.TemporaryDirectory() as td:
        img = Path(td) / "p.png"
        page.get_pixmap(dpi=300).save(img)
        res = subprocess.run(["tesseract", str(img), "-", "-l", "eng+spa+cat"],
                             capture_output=True, text=True)
        if res.returncode != 0:  # language packs missing → English only
            res = subprocess.run(["tesseract", str(img), "-"], capture_output=True, text=True)
        return res.stdout


def convert_pptx(src: Path, img_dir: Path, images: bool):
    from pptx import Presentation
    prs = Presentation(src)
    parts = []
    for n, slide in enumerate(prs.slides, 1):
        texts = []
        for shape in slide.shapes:
            if shape.has_text_frame:
                t = "\n".join(p.text for p in shape.text_frame.paragraphs if p.text.strip())
                if t:
                    texts.append(t)
            if getattr(shape, "has_table", False) and shape.has_table:
                for row in shape.table.rows:
                    texts.append(" | ".join(c.text for c in row.cells))
        notes = ""
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
        block = f"\n\n## Slide {n}\n\n" + "\n".join(texts)
        if images:
            block += f"\n\n![[{img_dir.name}/slide-{n:03d}.png]]"
        if notes:
            block += f"\n\n**Speaker notes:** {notes}"
        parts.append(block)
    if images:
        render_slides(src, img_dir)
    return "".join(parts), len(prs.slides), "python-pptx" + ("+slide-images" if images else "")


def render_slides(src: Path, img_dir: Path):
    office = shutil.which("soffice") or shutil.which("libreoffice")
    if not office:
        return
    import pymupdf
    img_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([office, "--headless", "--convert-to", "pdf", "--outdir", td, str(src)],
                       capture_output=True, timeout=300)
        pdfs = list(Path(td).glob("*.pdf"))
        if not pdfs:
            return
        doc = pymupdf.open(pdfs[0])
        for i, page in enumerate(doc, 1):
            page.get_pixmap(dpi=60).save(img_dir / f"slide-{i:03d}.png")


def convert_pandoc(src: Path):
    res = subprocess.run(["pandoc", str(src), "-t", "gfm", "--wrap=none"], capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(res.stderr.strip())
    return res.stdout, None, "pandoc"


def convert_refs(src: Path):
    """RIS or EndNote XML → markdown list of records (fields Claude needs for paper stubs)."""
    records = []
    text = src.read_text(errors="replace")
    if src.suffix.lower() == ".xml" and "<records" in text:
        import xml.etree.ElementTree as ET
        root = ET.fromstring(text)
        for rec in root.iter("record"):
            def g(path):
                el = rec.find(path)
                return "".join(el.itertext()).strip() if el is not None else ""
            records.append({
                "endnote_id": g("rec-number"),
                "title": g("titles/title"),
                "authors": ["".join(a.itertext()).strip() for a in rec.findall("contributors/authors/author")],
                "year": g("dates/year"),
                "journal": g("titles/secondary-title") or g("periodical/full-title"),
                "doi": g("electronic-resource-num"),
                "abstract": g("abstract"),
            })
    else:  # RIS
        cur = None
        for line in text.splitlines():
            m = re.match(r"^([A-Z][A-Z0-9])  - ?(.*)$", line)
            if not m:
                continue
            tag, val = m.group(1), m.group(2).strip()
            if tag == "TY":
                cur = {"authors": []}
            elif cur is None:
                continue
            elif tag == "ER":
                records.append(cur)
                cur = None
            elif tag in ("AU", "A1"):
                cur["authors"].append(val)
            elif tag in ("TI", "T1"):
                cur["title"] = val
            elif tag in ("PY", "Y1", "DA") and "year" not in cur:
                cur["year"] = val[:4]
            elif tag in ("JO", "JF", "T2"):
                cur.setdefault("journal", val)
            elif tag == "DO":
                cur["doi"] = val
            elif tag == "ID":
                cur["endnote_id"] = val
            elif tag == "AB":
                cur["abstract"] = val
    md = [f"# Reference export: {src.name}", "", f"{len(records)} records", ""]
    for r in records:
        md.append("```json\n" + json.dumps(r, ensure_ascii=False) + "\n```")
    return "\n".join(md), len(records), "refs-parser"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--vault", default=".")
    ap.add_argument("--type", choices=sorted(set(TYPE_BY_EXT.values())))
    ap.add_argument("--slug")
    ap.add_argument("--no-images", action="store_true")
    ap.add_argument("--move", action="store_true", help="move the original out of the inbox (default: copy)")
    a = ap.parse_args()

    src, vault = Path(a.input), Path(a.vault)
    ext = src.suffix.lower()
    kind = a.type or TYPE_BY_EXT.get(ext)
    if not kind:
        print(json.dumps({"status": "unsupported", "input": str(src)}))
        sys.exit(2)

    manifest = vault / "_system" / "manifest.csv"
    digest = sha256(src)
    if any(r["sha256"] == digest for r in read_manifest(manifest)):
        print(json.dumps({"status": "duplicate", "input": str(src), "sha256": digest}))
        return

    slug = a.slug or slugify(src.stem)
    out_dir = vault / "raw" / kind
    out_dir.mkdir(parents=True, exist_ok=True)
    while (out_dir / f"{slug}{ext}").exists():
        slug += "-b"
    raw_path, text_path = out_dir / f"{slug}{ext}", out_dir / f"{slug}.md"

    try:
        if ext == ".pdf":
            text, pages, method = convert_pdf(src)
        elif ext in (".pptx",):
            text, pages, method = convert_pptx(src, out_dir / slug, images=not a.no_images)
        elif ext in (".docx", ".doc", ".html", ".htm"):
            text, pages, method = convert_pandoc(src)
        elif ext in (".md", ".txt"):
            text, pages, method = src.read_text(errors="replace"), None, "copy"
        elif kind == "refs":
            text, pages, method = convert_refs(src)
        else:
            raise RuntimeError(f"no converter for {ext}")
    except Exception as e:  # report, don't crash the batch
        print(json.dumps({"status": "failed", "input": str(src), "error": str(e)}))
        sys.exit(1)

    (shutil.move if a.move else shutil.copy2)(str(src), raw_path)
    header = (f"---\nsource_file: {raw_path.name}\nsha256: {digest}\nconverted: {dt.date.today()}\n"
              f"method: {method}\npages: {pages if pages is not None else ''}\n---\n")
    text_path.write_text(header + text)
    row = {"sha256": digest, "original_name": src.name, "raw_path": str(raw_path.relative_to(vault)),
           "text_path": str(text_path.relative_to(vault)), "type": kind, "added": str(dt.date.today()),
           "status": "converted", "pages": pages or "", "method": method}
    append_manifest(manifest, row)
    print(json.dumps({"status": "converted", **row, "chars": len(text)}))


if __name__ == "__main__":
    main()
