#!/usr/bin/env python3
"""GOLEM contacts and collaborators network.

Tables (master record) in _system/network/:
  people.csv  one row per person (no PHI; professional details only, work email allowed)
  events.csv  workshops, courses, sessions, conferences, mentoring pods
  works.csv   Pablo's works (from OpenAlex), linked to vault paper pages by DOI
  links.csv   person x context (work or event), with role
  review.csv  uncertain name matches, held until decided (never auto-merged)
  exclude_works.txt  OpenAlex work IDs misattributed to Pablo

Commands (run with python3 -I):
  seed-openalex <vault> <works.json>          add co-authors from an OpenAlex works dump
  add-event <vault> <event.json> <people.csv> add an event and its people
        event.json: {"event_id","title","kind","date","location","organizer","source"}
        people.csv: name,affiliation,email,role,expertise,orcid   (only name required)
  apply-review <vault>                        apply decisions written in review.csv
  sync <vault>                                promote pages, refresh auto blocks and portal list
  who <vault> <query>                         quick lookup by name, institution, email or expertise
"""
import csv, json, os, re, sys, unicodedata, datetime

PABLO_OPENALEX = {"A5037683761", "A5160173183"}
TODAY = datetime.date.today().isoformat()
F = {
    "people": ["person_id", "name", "aliases", "orcid", "openalex_ids", "affiliation", "affiliation_source",
               "email", "expertise", "named", "has_page", "notes"],
    "events": ["event_id", "title", "kind", "date", "location", "organizer", "source", "notes"],
    "works": ["work_id", "doi", "title", "year", "type", "citekey"],
    "links": ["person_id", "context_type", "context_id", "role", "date", "source"],
    "review": ["name", "affiliation", "email", "role", "expertise", "orcid", "context_type", "context_id",
               "date", "candidates", "decision"],
}
AUTO_S, AUTO_E = "<!-- network:auto start -->", "<!-- network:auto end -->"


def p(vault, t): return os.path.join(vault, "_system", "network", t + ".csv")


def load(vault, t):
    f = p(vault, t)
    if not os.path.exists(f): return []
    with open(f, newline="", encoding="utf-8") as h: return list(csv.DictReader(h))


def save(vault, t, rows):
    os.makedirs(os.path.dirname(p(vault, t)), exist_ok=True)
    with open(p(vault, t), "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=F[t], extrasaction="ignore", lineterminator="\n"); w.writeheader()
        for r in rows: w.writerow({k: r.get(k, "") for k in F[t]})


def norm(s):
    s = "".join(" " if unicodedata.category(c) == "Pd" else c for c in (s or ""))
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z\s-]", " ", s).replace("-", " ")
    return re.sub(r"\s+", " ", s).strip()


def slugify(s): return re.sub(r"\s+", "-", norm(s))


def surname_initial(n):
    t = norm(n).split()
    return (t[-1], t[0][0]) if len(t) >= 2 else (t[0] if t else "", "")


class Net:
    def __init__(self, vault):
        self.v = vault
        self.t = {k: load(vault, k) for k in F}
        self.by_id = {r["person_id"]: r for r in self.t["people"]}

    def save(self):
        self.t["people"] = sorted(self.by_id.values(), key=lambda r: r["person_id"])
        for k in F: save(self.v, k, self.t[k])

    def names(self, r): return {norm(r["name"])} | {norm(a) for a in r["aliases"].split(";") if a.strip()}

    def match(self, name, email="", orcid="", oa=""):
        """Return (person_id, None) for a sure match, (None, [candidates]) if uncertain, (None, []) if new."""
        for r in self.by_id.values():
            if email and r["email"] and email.lower() in r["email"].lower().split(";"): return r["person_id"], None
            if orcid and r["orcid"] and orcid == r["orcid"]: return r["person_id"], None
            if oa and oa in r["openalex_ids"].split(";"): return r["person_id"], None
        n = norm(name)
        ts = frozenset(n.split())  # same tokens in any order counts as the same name
        exact = [r["person_id"] for r in self.by_id.values() if ts in {frozenset(x.split()) for x in self.names(r)}]
        if len(exact) == 1: return exact[0], None
        if len(exact) > 1: return None, exact
        si = surname_initial(name)
        fuzzy = [r["person_id"] for r in self.by_id.values()
                 if any(surname_initial(x) == si for x in self.names(r))]
        return None, fuzzy

    def new_person(self, name, **kw):
        pid = base = slugify(name); i = 2
        while pid in self.by_id: pid = f"{base}-{i}"; i += 1
        r = {k: "" for k in F["people"]}; r.update(person_id=pid, name=name, **{k: v for k, v in kw.items() if v})
        self.by_id[pid] = r; return pid

    def enrich(self, pid, **kw):
        r = self.by_id[pid]
        for k, v in kw.items():
            if not v: continue
            if k in ("email", "openalex_ids", "expertise", "aliases"):
                cur = [x for x in r[k].split(";") if x]
                for x in v.split(";"):
                    if x and x not in cur: cur.append(x)
                r[k] = ";".join(cur)
            elif not r.get(k): r[k] = v

    def link(self, pid, ctype, cid, role, date, source):
        key = (pid, ctype, cid, role)
        if not any((l["person_id"], l["context_type"], l["context_id"], l["role"]) == key for l in self.t["links"]):
            self.t["links"].append(dict(person_id=pid, context_type=ctype, context_id=cid, role=role, date=date, source=source))

    def add(self, row, ctype, cid, date, source, oa=""):
        pid, cands = self.match(row.get("name", ""), row.get("email", ""), row.get("orcid", ""), oa)
        if pid is None and cands:
            if any(x["name"] == row.get("name") and x["context_id"] == cid for x in self.t["review"]): return None
            self.t["review"].append(dict(row, context_type=ctype, context_id=cid, date=date,
                                         candidates=";".join(cands), decision=""))
            return None
        if pid is None:
            pid = self.new_person(row["name"])
        else:
            n = row["name"]
            if norm(n) not in self.names(self.by_id[pid]): self.enrich(pid, aliases=n)
        self.enrich(pid, orcid=row.get("orcid", ""), openalex_ids=oa, email=row.get("email", ""),
                    expertise=row.get("expertise", ""))
        if row.get("affiliation"):
            r = self.by_id[pid]; r["affiliation"] = row["affiliation"]; r["affiliation_source"] = f"{source}, {date[:4]}"
        self.link(pid, ctype, cid, row.get("role", ""), date, source)
        return pid


def vault_dois(vault):
    out = {}
    d = os.path.join(vault, "wiki", "papers")
    for f in os.listdir(d):
        m = re.search(r'^doi:\s*"?([^"\n]+)"?', open(os.path.join(d, f), encoding="utf-8").read(), re.M)
        if m: out[m.group(1).strip().lower()] = f[:-3]
    return out


def seed_openalex(vault, path):
    net = Net(vault); dois = vault_dois(vault)
    excl_f = os.path.join(vault, "_system", "network", "exclude_works.txt")
    excl = {l.split()[0] for l in open(excl_f) if l.strip() and not l.startswith("#")} if os.path.exists(excl_f) else set()
    works = json.load(open(path))["results"]
    # oldest first so the latest affiliation wins
    for w in sorted(works, key=lambda x: x["publication_year"] or 0):
        wid = w["id"].rsplit("/", 1)[-1]
        if wid in excl: continue
        doi = (w["doi"] or "").replace("https://doi.org/", "").lower()
        if not any(x["work_id"] == wid for x in net.t["works"]):
            net.t["works"].append(dict(work_id=wid, doi=doi, title=w["title"], year=w["publication_year"],
                                       type=w["type"], citekey=dois.get(doi, "")))
        for a in w["authorships"]:
            aid = (a["author"].get("id") or "").rsplit("/", 1)[-1]
            if not a["author"].get("display_name"): continue
            if aid in PABLO_OPENALEX: continue
            inst = "; ".join(i["display_name"] for i in a.get("institutions", []))
            orcid = (a["author"].get("orcid") or "").replace("https://orcid.org/", "")
            net.add(dict(name=a["author"]["display_name"], affiliation=inst, orcid=orcid, role="co-author"),
                    "work", wid, str(w["publication_year"]), "OpenAlex", oa=aid)
    net.save(); print(f"people {len(net.by_id)}, works {len(net.t['works'])}, links {len(net.t['links'])}, review {len(net.t['review'])}")


def add_event(vault, ev_path, people_path):
    net = Net(vault); ev = json.load(open(ev_path))
    if not any(e["event_id"] == ev["event_id"] for e in net.t["events"]): net.t["events"].append(ev)
    n = r = 0
    with open(people_path, newline="", encoding="utf-8") as h:
        for row in csv.DictReader(h):
            if not row.get("name", "").strip(): continue
            pid = net.add(row, "event", ev["event_id"], ev.get("date", ""), ev.get("source", ""))
            n += pid is not None; r += pid is None
    net.save(); print(f"event {ev['event_id']}: {n} linked, {r} held for review")


def apply_review(vault):
    """decision: merge:<person_id> | new | skip"""
    net = Net(vault); keep = []
    for row in net.t["review"]:
        d = row.get("decision", "").strip()
        if not d: keep.append(row); continue
        if d == "skip": continue
        pid = d.split(":", 1)[1] if d.startswith("merge:") else net.new_person(row["name"])
        if d.startswith("merge:") and norm(row["name"]) not in net.names(net.by_id[pid]): net.enrich(pid, aliases=row["name"])
        net.enrich(pid, email=row.get("email", ""), orcid=row.get("orcid", ""), expertise=row.get("expertise", ""))
        net.link(pid, row["context_type"], row["context_id"], row["role"], row["date"], "review")
    net.t["review"] = keep; net.save(); print(f"review left: {len(keep)}")


def fm_set(text, key, val):
    line = f"{key}: {val}"
    if re.search(rf"^{key}:.*$", text, re.M): return re.sub(rf"^{key}:.*$", lambda m: line, text, count=1, flags=re.M)
    return text.replace("\n---\n", f"\n{line}\n---\n", 1)


def auto_block(text, body):
    blk = f"{AUTO_S}\n{body}\n{AUTO_E}"
    if AUTO_S in text: return re.sub(re.escape(AUTO_S) + ".*?" + re.escape(AUTO_E), lambda m: blk, text, flags=re.S)
    return text.replace("\n## See also", f"\n{blk}\n\n## See also", 1) if "\n## See also" in text else text + "\n" + blk + "\n"


def ylist(items): return "[" + ", ".join(json.dumps(x) for x in items) + "]"


def sync(vault):
    net = Net(vault)
    works = {w["work_id"]: w for w in net.t["works"]}; events = {e["event_id"]: e for e in net.t["events"]}
    pdir = os.path.join(vault, "wiki", "entities", "people"); edir = os.path.join(vault, "wiki", "events")
    os.makedirs(pdir, exist_ok=True); os.makedirs(edir, exist_ok=True)
    tpl_p = open(os.path.join(vault, "_system", "templates", "person.md"), encoding="utf-8").read()
    tpl_e = open(os.path.join(vault, "_system", "templates", "event.md"), encoding="utf-8").read()
    by_p = {}
    for l in net.t["links"]: by_p.setdefault(l["person_id"], []).append(l)

    def ctx_line(l):
        if l["context_type"] == "work":
            w = works.get(l["context_id"], {})
            ref = f"[[{w['citekey']}]]" if w.get("citekey") else f"{w.get('title','?')}" + (f" (https://doi.org/{w['doi']})" if w.get("doi") else "")
            return f"- {w.get('year','?')} · co-author · {ref}"
        e = events.get(l["context_id"], {})
        return f"- {e.get('date','?')} · {l['role'] or 'participant'} · [[{l['context_id']}]] ({e.get('kind','event')})"

    new_pages = 0
    for pid, r in net.by_id.items():
        ls = by_p.get(pid, [])
        ctxs = {(l["context_type"], l["context_id"]) for l in ls}
        coauth = any(l["context_type"] == "work" for l in ls)
        promote = coauth or r["named"] == "yes" or len(ctxs) >= 2
        r["has_page"] = "yes" if promote else ""
        if not promote: continue
        f = os.path.join(pdir, pid + ".md")
        if not os.path.exists(f):
            aff = f" Affiliation: {r['affiliation']} ({r['affiliation_source']})." if r["affiliation"] else ""
            how = "co-author" if coauth else "contact"
            txt = tpl_p.replace('title: ""', f"title: {json.dumps(r['name'])}").replace("created:", f"created: {TODAY}", 1)
            txt = txt.replace("{{LEAD}}", f"**{r['name']}** is a {how} of Pablo's.{aff}")
            new_pages += 1
        else:
            txt = open(f, encoding="utf-8").read()
        dates = sorted(l["date"] for l in ls if l["date"])
        roles = sorted({l["role"] or "participant" for l in ls})
        for k, v in [("aliases", ylist([a for a in r["aliases"].split(";") if a])), ("affiliation", json.dumps(r["affiliation"])),
                     ("email", json.dumps(r["email"])), ("orcid", json.dumps(r["orcid"])),
                     ("expertise", ylist([x for x in r["expertise"].split(";") if x])), ("roles", ylist(roles)),
                     ("n_coauthored", sum(1 for c in ctxs if c[0] == "work")),
                     ("n_events", sum(1 for c in ctxs if c[0] == "event")),
                     ("first_contact", dates[0] if dates else ""), ("last_contact", dates[-1] if dates else ""),
                     ("updated", TODAY)]:
            txt = fm_set(txt, k, v)
        body = "## Shared work and events\n_Generated from `_system/network/`; edit the tables, not this list._\n" + \
               "\n".join(sorted((ctx_line(l) for l in ls), reverse=True))
        open(f, "w", encoding="utf-8").write(auto_block(txt, body))

    for eid, e in events.items():
        f = os.path.join(edir, eid + ".md")
        if not os.path.exists(f):
            txt = tpl_e.replace('title: ""', f"title: {json.dumps(e['title'])}").replace("created:", f"created: {TODAY}", 1)
            txt = txt.replace("{{LEAD}}", f"**{e['title']}** ({e.get('kind','event')}, {e.get('date','?')}"
                              + (f", {e['location']}" if e.get("location") else "") + ")."
                              + (f" Organizer: {e['organizer']}." if e.get("organizer") else "") + f" Source: {e.get('source','?')}.")
        else:
            txt = open(f, encoding="utf-8").read()
        for k, v in [("kind", e.get("kind", "")), ("date", e.get("date", "")), ("location", json.dumps(e.get("location", ""))), ("updated", TODAY)]:
            txt = fm_set(txt, k, v)
        ppl = sorted((l for l in net.t["links"] if l["context_type"] == "event" and l["context_id"] == eid), key=lambda l: net.by_id[l["person_id"]]["name"])
        lines = [(f"- [[{l['person_id']}|{net.by_id[l['person_id']]['name']}]]" if net.by_id[l["person_id"]]["has_page"] else f"- {net.by_id[l['person_id']]['name']}")
                 + f" · {l['role'] or 'participant'}" + (f" · {net.by_id[l['person_id']]['affiliation']}" if net.by_id[l["person_id"]]["affiliation"] else "") for l in ppl]
        body = f"## People ({len(ppl)})\n_Generated from `_system/network/`; edit the tables, not this list._\n" + "\n".join(lines)
        open(f, "w", encoding="utf-8").write(auto_block(txt, body))

    portal = os.path.join(vault, "wiki", "portals", "network.md")
    if os.path.exists(portal):
        txt = open(portal, encoding="utf-8").read()
        paged = sorted((r for r in net.by_id.values() if r["has_page"]), key=lambda r: surname_initial(r["name"]))
        body = f"## All people with pages ({len(paged)})\n" + " · ".join(f"[[{r['person_id']}|{r['name']}]]" for r in paged) + \
               f"\n\n## All events ({len(events)})\n" + "\n".join(f"- [[{k}]]" for k in sorted(events)) + \
               f"\n\n_Tables: {len(net.by_id)} people, {len(events)} events, {len(works)} works, {len(net.t['links'])} links, " \
               f"{len(net.t['review'])} names held for review._"
        open(portal, "w", encoding="utf-8").write(auto_block(txt, body))
    net.save(); print(f"pages: {sum(1 for r in net.by_id.values() if r['has_page'])} people ({new_pages} new), {len(events)} events")


def who(vault, q):
    net = Net(vault); qn = norm(q); works = {w["work_id"]: w for w in net.t["works"]}; events = {e["event_id"]: e for e in net.t["events"]}
    hits = [r for r in net.by_id.values() if qn in " ".join(norm(r[k]) for k in ("name", "aliases", "affiliation", "expertise")) or q.lower() in r["email"].lower()]
    for r in hits[:25]:
        print(f"{r['name']} [{r['person_id']}] | {r['affiliation']} | {r['email']} | {r['expertise']}")
        for l in net.t["links"]:
            if l["person_id"] == r["person_id"]:
                c = works.get(l["context_id"], {}).get("title") if l["context_type"] == "work" else events.get(l["context_id"], {}).get("title")
                print(f"   {l['date']} {l['role']}: {c}")
    print(f"{len(hits)} match(es)" + (" (first 25 shown)" if len(hits) > 25 else ""))


if __name__ == "__main__":
    a = sys.argv[1:]
    {"seed-openalex": lambda: seed_openalex(a[1], a[2]), "add-event": lambda: add_event(a[1], a[2], a[3]),
     "apply-review": lambda: apply_review(a[1]), "sync": lambda: sync(a[1]), "who": lambda: who(a[1], " ".join(a[2:]))}[a[0]]()
