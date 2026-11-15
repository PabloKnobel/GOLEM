import html, sys, json, re, glob, os, time, unicodedata, urllib.request, urllib.parse, yaml
V = sys.argv[1]; OUT = sys.argv[2]
UA = {"User-Agent": "GOLEM-metadata-check (mailto:none)"}
def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            return json.load(r)
    except Exception as e:
        return {"_error": str(e)}
def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii","ignore").decode().lower()
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()
def fm(path):
    t = open(path, encoding="utf-8").read()
    block = t.split("---")[1]
    try: return yaml.safe_load(block)
    except Exception:
        keep = "\n".join(l for l in block.splitlines() if re.match(r"^(title|authors|year|journal|volume|issue|pages|doi):", l))
        return yaml.safe_load(keep)
rows = []; raw = {}
for f in sorted(glob.glob(f"{V}/wiki/papers/*.md")):
    key = os.path.basename(f)[:-3]; m = fm(f); doi = m.get("doi","")
    cr = get("https://api.crossref.org/works/" + urllib.parse.quote(doi)).get("message", None) if doi else None
    oa = get("https://api.openalex.org/works/doi:" + doi) if doi else {}
    raw[key] = {"crossref": cr, "openalex": oa if "_error" not in oa else None}
    time.sleep(0.3)
    rec = {}; src = None
    if isinstance(cr, dict) and cr.get("title"):
        src = "crossref"
        rec["title"] = html.unescape((cr.get("title") or [""])[0]); rec["subtitle"]=html.unescape((cr.get("subtitle") or [""])[0])
        rec["authors"] = [a.get("family","") for a in cr.get("author",[])]
        rec["authors_full"] = [f'{a.get("family","")}, {a.get("given","")}' for a in cr.get("author",[])]
        dp = (cr.get("published-print") or cr.get("issued") or {}).get("date-parts",[[None]])[0]
        dpo = (cr.get("published-online") or {}).get("date-parts",[[None]])[0]
        rec["year"] = dp[0]; rec["year_online"] = dpo[0]
        rec["journal"] = html.unescape((cr.get("container-title") or [""])[0])
        rec["volume"] = cr.get("volume",""); rec["issue"] = cr.get("issue","")
        rec["pages"] = cr.get("page","") or cr.get("article-number","")
        rec["type"] = cr.get("type","")
    elif oa and "_error" not in oa:
        src = "openalex"
        rec["title"] = oa.get("title","")
        rec["authors"] = [ (x["author"]["display_name"].split()[-1]) for x in oa.get("authorships",[])]
        rec["authors_full"] = [x["author"]["display_name"] for x in oa.get("authorships",[])]
        rec["year"] = oa.get("publication_year"); rec["year_online"] = None
        b = oa.get("biblio",{}) or {}
        rec["journal"] = ((oa.get("primary_location") or {}).get("source") or {}).get("display_name","")
        rec["volume"] = b.get("volume",""); rec["issue"] = b.get("issue","")
        rec["pages"] = "-".join(x for x in [b.get("first_page"), b.get("last_page")] if x)
        rec["type"] = oa.get("type","")
    oa_year = oa.get("publication_year") if oa and "_error" not in oa else None
    issues = []
    if not src: issues.append("NOT FOUND in CrossRef or OpenAlex")
    else:
        if norm(m.get("title")) not in (norm(rec["title"]), norm(rec["title"]+" "+rec.get("subtitle",""))): issues.append(f'title: vault="{m.get("title")}" | {src}="{rec["title"]}"')
        va=[]
        for a in (m.get("authors") or []):
            a=str(a).strip()
            if re.fullmatch(r"([A-Z]\.\s?-?)+", a) and va: va[-1][1]=a
            else: va.append([a.split(",")[0], ""])
        m["_authors_paired"]=va
        va=[norm(x[0]) for x in va]
        ra = [norm(a) for a in rec["authors"]]
        if va != ra: issues.append(f'authors: vault={len(va)} {va[:4]}… | {src}={len(ra)} {ra[:4]}… ; diff_vault_only={[a for a in va if a not in ra]} diff_src_only={[a for a in ra if a not in va]}')
        if str(m.get("year")) != str(rec["year"]): issues.append(f'year: vault={m.get("year")} | {src} print/issued={rec["year"]} online={rec["year_online"]} openalex={oa_year}')
        if norm(m.get("journal")) != norm(rec["journal"]): issues.append(f'journal: vault="{m.get("journal")}" | {src}="{rec["journal"]}"')
        for k in ["volume","issue"]:
            if str(m.get(k,"")).strip('"?') != str(rec[k] or ""): issues.append(f'{k}: vault="{m.get(k)}" | {src}="{rec[k]}"')
        vp = re.sub(r"^Article\s+","",str(m.get("pages",""))); rp = str(rec["pages"] or "")
        if norm(vp).replace(" ","") != norm(rp).replace(" ",""): issues.append(f'pages: vault="{m.get("pages")}" | {src}="{rp}"')
    rows.append({"key": key, "doi": doi, "source": src, "type": rec.get("type"), "issues": issues})
json.dump(raw, open(f"{OUT}/raw_records.json","w"), indent=1)
json.dump(rows, open(f"{OUT}/check.json","w"), indent=1)
with open(f"{OUT}/report.md","w") as o:
    for r in rows:
        o.write(f'## {r["key"]} ({r["source"]}, {r["type"]})\n' + ("".join(f"- {i}\n" for i in r["issues"]) or "- OK\n"))
print("papers:", len(rows), "| found:", sum(1 for r in rows if r["source"]), "| clean:", sum(1 for r in rows if not r["issues"]))
print("crossref:", sum(1 for r in rows if r["source"]=="crossref"), "openalex-only:", sum(1 for r in rows if r["source"]=="openalex"))
