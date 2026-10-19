#!/usr/bin/env python3
"""Check a finished CV PDF: page count, email, ATS keyword score and lines holding only a few words.
Usage: python3 ats_check.py CV.pdf keywords.json [--email you@x.com]
keywords.json: [{"term": "stakeholder management", "weight": 3, "alt": ["..."], "evidence": "proven|stretch|gap"}, ...]
ATS score = 85% weighted JD-term match in the PDF text + 15% parse checks (one page, email intact, real text)."""
import json, re, sys
import pdfplumber

def norm(x): return " " + re.sub(r"[^a-z0-9+#]+", " ", x.lower().replace("&", " and ")).strip() + " "
def has(T, term):
    t = norm(term).strip()
    forms = {t, t + "s", re.sub(r"s$", "", t), re.sub(r"ies$", "y", t), re.sub(r"y$", "ies", t)}
    return any(f and " " + f + " " in T for f in forms)

def lines_of(page):
    """Group words into visual lines, split into column segments where a row has a wide gap."""
    words = page.extract_words(keep_blank_chars=False, use_text_flow=False)
    rows = {}
    for w in words: rows.setdefault(round(w["top"] / 2), []).append(w)
    segs = []
    for _, ws in sorted(rows.items()):
        ws.sort(key=lambda w: w["x0"]); cur = [ws[0]]
        for w in ws[1:]:
            if w["x0"] - cur[-1]["x1"] > 25: segs.append(cur); cur = [w]
            else: cur.append(w)
        segs.append(cur)
    return [{"x0": s[0]["x0"], "x1": s[-1]["x1"], "top": s[0]["top"], "h": s[0]["bottom"] - s[0]["top"],
             "text": " ".join(w["text"] for w in s)} for s in segs]

def widows(lines):
    """Last lines of a paragraph/bullet that hold only a few words while the line above is full."""
    out = []
    for i, l in enumerate(lines):
        block = [m for m in lines if abs(m["x0"] - l["x0"]) < 30]
        right = max(m["x1"] for m in block); left = min(m["x0"] for m in block); W = right - left
        if W < 150: continue
        prev = [m for m in block if 0 < l["top"] - m["top"] < 2.0 * max(l["h"], 8)]
        if not prev: continue
        p = max(prev, key=lambda m: m["top"])
        ends_sentence = re.search(r"[.!?;)%]$", l["text"].strip()) and not re.fullmatch(r"[\d.,%\s]+", l["text"])
        if ends_sentence and (l["x1"] - left) < 0.40 * W and (right - p["x1"]) < 0.10 * W and len(l["text"].split()) <= 5:
            out.append(l["text"])
    return out

def main():
    pdf_path, kw_path = sys.argv[1], sys.argv[2]
    email = sys.argv[sys.argv.index("--email") + 1] if "--email" in sys.argv else None
    K = json.load(open(kw_path))
    with pdfplumber.open(pdf_path) as pdf:
        pages = len(pdf.pages); text = "\n".join(p.extract_text() or "" for p in pdf.pages)
        short = widows(lines_of(pdf.pages[0]))
    T = norm(text)
    em = re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", text)
    parse = [pages == 1, (email in text) if email else bool(em and len(em[0].rsplit(".", 1)[-1]) >= 2), len(text) > 600]
    tot = got = ceil = 0; hit, miss = [], []
    for k in K:
        w = k.get("weight", 1) if k.get("weight") in (1, 2, 3) else 1; tot += w
        ok = any(has(T, x) for x in [k["term"], *k.get("alt", [])])
        reach = k.get("evidence", "proven") != "gap"
        if ok: got += w; ceil += w; hit.append(k["term"])
        else:
            miss.append(f'{k["term"]} ({k.get("evidence", "?")}, w{w})')
            if reach: ceil += w
    score = round(85 * got / max(tot, 1) + 15 * sum(parse) / 3)
    ceiling = round(85 * ceil / max(tot, 1) + 15)
    print(f"pages: {pages}  {'PASS one page' if pages == 1 else 'FAIL more than one page'}")
    print(f"email on one line: {'PASS' if parse[1] else 'FAIL'}")
    print(f"ATS score: {score}/100  (honest ceiling without gap terms: {ceiling})")
    print("found: " + "; ".join(hit))
    print("missing: " + ("; ".join(miss) or "none"))
    print("short last lines (rewrite these items to end cleanly): " + (" | ".join(short) or "none"))

if __name__ == "__main__":
    main()
