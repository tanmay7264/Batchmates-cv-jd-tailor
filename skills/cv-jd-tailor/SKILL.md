---
name: cv-jd-tailor
description: Tailor anyone's CV to a job description. They upload their CV (PDF or DOCX) and paste the JD; you score it, offer bullet options to approve, then return a one-page, ATS-checked PDF in their CV's own format, with truthful XYZ bullets.
---

# CV × JD Tailor

*Works in any agent that supports Agent Skills (Claude, ChatGPT, Codex, Gemini CLI). Built by Tanmay Narnaware for BatchMates (batchmates.tech) · github.com/tanmay7264/Batchmates-cv-jd-tailor · MIT licence*

The user uploads **their CV** (PDF or DOCX) and gives **a job description** (text, file or link). They get back the strongest *truthful* version of their CV for that role: **same format**, ATS score 90+ where their real experience allows, exactly one page (or their original page count), as a PDF they can upload.

Flow: **Intake → Plan (they choose) → Build → Verify loop → Deliver**, then optional interview prep and cover letter.

## Ground rules (never break these)
1. **Never invent.** No new employers, titles, dates, degrees, grades, certifications, awards, tools, clients, user counts or metrics. Every number must already be in their CV or in facts they tell you in this chat. Keep numbers exactly as given; never merge two separate metrics.
2. **Keep their format.** Same layout, column structure, section order and headings, fonts (or a metric-identical substitute), colours, logo/photo, header/footer and page count. Only the content inside changes.
3. **Reframes are options, never silent edits.** You may offer bullets that describe, in the JD's words, work their real role plausibly involved. Label them **JD-aligned reframe**, give them no numbers, and include them only if the user ticks them. Every reframe they keep goes in the "prepare to explain" list.
4. **Partial evidence ("stretch").** If the CV or their facts show partial exposure to a JD requirement, phrase it defensibly ("contributed to", "supported", "exposure to") and list it as "stretch: prepare to explain".
5. **Real gaps stay out.** If nothing supports a JD requirement, never add it anywhere, including skills. Report it as a gap with an honest interview bridge.
6. **Ask little.** Don't ask whether they did something; offer it as a tickable option. Ask questions only when the answer changes the CV and you can't infer it (at most 2 per run).
7. **Privacy.** CVs are personal data. Don't publish them, don't put contact details in URLs, and keep files in the working directory only.

## Step 0: Intake
- You need a CV file and a JD. If either is missing, ask once for both together. If a JD link can't be fetched, ask them to paste the text.
- Optional, in the same message: company and role, facts not in the CV that they want considered ("I also used Power BI on my capstone"), and whether they want a cover letter or interview prep.
- If they upload a PDF but also have the DOCX, the DOCX gives the most faithful format. Ask for it only if the PDF layout is complex (two columns, sidebars, tables).

## Step 1: Read the CV and capture its format
1. Run `python3 scripts/extract_cv.py <cv>`. It prints the page size, fonts, sizes, colours, images, likely columns, ATS warnings (split email, text boxes, tables, header/footer contact, images, emoji) and the text exactly as a parser reads it. If `scripts/` isn't present, write the two files from the appendix first.
2. Look at the layout: `pdftoppm -r 80 -png <cv.pdf> page` (convert a DOCX first with `soffice --headless --convert-to pdf`), then view the PNG. Note the section order, headings, bullet style, date alignment, bold/colour usage and roughly how many characters fit on one line of each column.
3. Build a **facts sheet** (for yourself): every role, date, metric, skill, tool, certification and achievement in the CV, plus anything they told you. This is the only source of truth.

## Step 2: Plan (send it, then wait for their picks)
Send one message with:
1. **Match score before** (/100), as a recruiter who has screened 10,000+ CVs for this role: JD keyword match 20, depth of relevant experience 25, domain fit 15, quantified impact 10, education 15, presentation/ATS 10, risk signals 5. Add a one-line blunt verdict.
2. **5 missing keywords**, each tagged **Can add** (evidence exists; say where it goes), **Stretch** (partial evidence) or **Real gap** (never added; give an interview bridge).
3. **ATS keyword map:** 20–30 terms an ATS would screen this JD for, in the JD's exact wording, each with weight 3/2/1, any exact alternatives (acronym or expansion only), and evidence proven/stretch/gap. Save it as `keywords.json` for the checker.
4. **Options per section**, numbered so they can reply "Experience: 1, 3, 4":
   - For every role, 3–4 bullet options in **XYZ form** (below). Mix *fact* bullets from the facts sheet with 1–2 clearly labelled *JD-aligned reframes*.
   - Summary or paragraph sections: 2 versions.
   - Projects and achievements: 4–6 candidates.
   - Mark the recommended one-page set with ★.
5. **Skills and certifications:** a recommended list plus a longer pick list from their real skills. Tell them they can add their own.
6. **Projected ATS** for the ★ set, and per section the points it earns and what would be lost if it were cut.
7. At most 2 questions that change the CV, or none.

### XYZ bullets (Google's formula)
"Accomplished **X**, as measured by **Y**, by doing **Z**." Write the result first.
- **Y** must be a real number from the facts sheet. If there is none, use a real scope measure (team size, number of markets, users served, duration, budget), never an invented percentage.
- **Z** is the method, using the JD's own words where they're true.
- Mark each option `[XYZ]`, `[no Y]` or `[no Z]` so they can see which bullets are strong. Reframes are always `[no Y]`.
- Bold sparingly: the lead verb and one key metric, only if the original CV uses bold that way.
- **Line fill:** size each bullet to end on a well-filled last line, never on 1–4 dangling words. Use the characters-per-line you measured in Step 1: aim for about 90–100% of one line or of two lines.

## Step 3: Build the CV in their format
Use exactly what they picked. Their typed additions count as facts. Polish for flow, remove repetition, and keep the JD terms verbatim.
- **DOCX uploaded** (best fidelity): edit a copy in place with python-docx. Keep each paragraph's style, and keep the formatting of the first run when replacing text. Recreate bold spans as separate runs with the same font, size and colour. Add or remove bullet paragraphs by copying an existing bullet paragraph (`copy.deepcopy(p._p)`) so numbering and indents stay identical. Then convert with `soffice --headless --convert-to pdf`.
- **PDF only:** rebuild the layout as one self-contained HTML page and print it with Playwright Chromium (`page.pdf(format='A4' or 'Letter', print_background=True)`; don't run `playwright install` if Chromium is already there). Match fonts with metric-identical free fonts where the original isn't installed: Times New Roman → Liberation Serif/Tinos, Arial → Liberation Sans/Arimo, Calibri → Carlito, Cambria → Caladea, Garamond → EB Garamond. Reproduce colours, rules, bars, column widths, date alignment and margins from the page image. Keep links clickable (`mailto:`, `tel:`, `https://`).
- **Fixes allowed even though the format is fixed:** put a split email on one line (shrink only the email if needed), drop emoji, and move contact details out of headers/footers or text boxes into body text. Mention each fix.

## Step 4: Verify loop (up to 3 rounds)
Run `python3 scripts/ats_check.py out.pdf keywords.json --email <their email>`. It reports pages, email intact, the **ATS score** (85% weighted JD-term match in the PDF text + 15% parse checks), the honest ceiling, missing terms, and **short last lines**. Then:
- **More pages than the target:** first tighten wording and cut the least JD-relevant bullet. Only then reduce font size, by at most 1pt below the original and never below 9pt. Never drop a whole section.
- **Spare space at the bottom:** increase line spacing slightly or restore the next-best bullet.
- **ATS below 90 with missing proven or stretch terms:** add each term verbatim where it was earned, or in skills. Never add gap terms. If gaps cap the score, report the honest ceiling instead of forcing it.
- **Short last lines:** rewrite those items to end cleanly. Usually shortening by the dangling words is enough; keep the facts and JD terms.
- **Every round:** view a PNG of page 1 to check alignment, overlap, columns and that nothing spills past the margin or footer. Check that every number appears in the facts sheet.

## Step 5: Deliver
Send the PDF (plus the edited DOCX if they uploaded one) with at most 8 lines:
- Match score before → after, and the ATS score (or honest ceiling).
- What changed and which format fixes you made.
- **Prepare to explain:** every stretch and reframe item kept.
- Real gaps and a one-line interview bridge for each.
- Reminder: upload the PDF, not a Word file, unless the portal asks for DOCX.

Then offer in one line: an interview guide, a 3-question rehearsal, or a cover letter.

## Optional extras
- **Interview guide (.md):** a 30-second pitch; for every CV bullet, the real story, a STAR outline, 2 likely follow-ups and what not to say; a numbers cheat sheet; how to discuss stretch and reframe items honestly; gaps and bridges; 3 sharp questions to ask them.
- **Rehearsal:** as the hiring manager, ask the 3 hardest realistic questions one at a time. After each answer give a score /10, what landed, what was missing, what a strong answer includes (their real facts only) and the likely follow-up.
- **Cover letter (under 300 words):** open with the company's actual problem (from the JD), then their top 3 relevant wins with real numbers, then a specific next step. Use plain words. Banned: "excited to apply", "passionate", "leverage", "synergy", "fast-paced environment", "great fit", "dynamic", "thrilled", "delve", rhetorical questions.

## Appendix: helper scripts
If `scripts/extract_cv.py` and `scripts/ats_check.py` aren't present, write them from below. They need `pdfplumber` (`pip install pdfplumber` if missing).

### scripts/extract_cv.py
```python
#!/usr/bin/env python3
"""Extract a CV's text (in reading order) and a format report.
Usage: python3 extract_cv.py CV.pdf|CV.docx [--json]
Prints what an ATS parser would read, plus layout facts needed to rebuild the same format."""
import json, re, sys, zipfile
from collections import Counter

def pdf_info(path):
    import pdfplumber
    rep = {"type": "pdf"}
    with pdfplumber.open(path) as pdf:
        rep["pages"] = len(pdf.pages)
        p0 = pdf.pages[0]
        rep["page_size_pt"] = [round(p0.width, 1), round(p0.height, 1)]
        rep["page_size"] = "A4" if abs(p0.height - 842) < 6 else "Letter" if abs(p0.height - 792) < 6 else "other"
        fonts, sizes, colours, images, text = Counter(), Counter(), Counter(), 0, []
        xs = []
        for pg in pdf.pages:
            for ch in pg.chars:
                fonts[re.sub(r"^[A-Z]{6}\+", "", ch.get("fontname", ""))] += 1
                sizes[round(ch.get("size", 0), 1)] += 1
                col = ch.get("non_stroking_color")
                if col is not None: colours[str(col)] += 1
            images += len(pg.images)
            xs += [round(w["x0"] / 20) * 20 for w in pg.extract_words()]
            text.append(pg.extract_text(layout=False) or "")
        rep["fonts"] = [f for f, _ in fonts.most_common(8)]
        rep["font_sizes"] = [s for s, _ in sizes.most_common(6)]
        rep["text_colours"] = [c for c, _ in colours.most_common(5)]
        rep["images"] = images
        starts = [x for x, n in Counter(xs).most_common(6) if n > 15]
        rep["likely_columns"] = 2 if starts and max(starts) - min(starts) > 120 else 1
        rep["text"] = "\n".join(text)
    return rep

def docx_info(path):
    z = zipfile.ZipFile(path)
    xml = z.read("word/document.xml").decode("utf8", "ignore")
    rep = {"type": "docx"}
    rep["text_boxes"] = xml.count("<w:txbxContent")
    rep["tables"] = xml.count("<w:tbl>")
    rep["images"] = len([n for n in z.namelist() if n.startswith("word/media/")])
    rep["fonts"] = [f for f, _ in Counter(re.findall(r'w:ascii="([^"]+)"', xml)).most_common(6)]
    rep["font_sizes"] = sorted({int(s) / 2 for s in re.findall(r'<w:sz w:val="(\d+)"', xml)})
    rep["text_colours"] = [c for c, _ in Counter(re.findall(r'w:color w:val="([0-9A-Fa-f]{6})"', xml)).most_common(5)]
    m = re.search(r'<w:pgSz w:w="(\d+)" w:h="(\d+)"', xml) or re.search(r'<w:pgSz[^>]*w:h="(\d+)"[^>]*w:w="(\d+)"', xml)
    if m:
        w, h = (int(m.group(1)), int(m.group(2))) if 'w:w="' + m.group(1) in xml else (int(m.group(2)), int(m.group(1)))
        rep["page_size"] = "A4" if abs(h - 16838) < 200 else "Letter" if abs(h - 15840) < 200 else "other"
    rep["columns"] = re.findall(r'<w:cols [^>]*w:num="(\d+)"', xml) or ["1"]
    hdr = False
    for n in z.namelist():
        if re.match(r"word/(header|footer)\d*\.xml$", n):
            t = re.sub(r"<[^>]+>", " ", z.read(n).decode("utf8", "ignore"))
            if re.search(r"@|\+?\d[\d\s]{8,}", t): hdr = True
    rep["contact_in_header_footer"] = hdr
    # paragraph text in document order, including text boxes (skipping mc:Fallback duplicates)
    xml2 = re.sub(r"<mc:Fallback>.*?</mc:Fallback>", "", xml, flags=re.S)
    paras = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml2, flags=re.S):
        t = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)).strip()
        if t: paras.append(t)
    rep["text"] = "\n".join(paras)
    return rep

def checks(rep):
    t = rep.get("text", ""); out = []
    emails = re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", t)
    split = re.search(r"[\w.+-]+@[\w-]*\s*\n\s*[\w.-]+", t) or re.search(r"@[\w-]+\.[a-z]{0,3}[ \t]*\n[ \t]*[a-z]{1,3}\b", t, re.I)
    cut = emails and len(emails[0].rsplit(".", 1)[-1]) < 2
    out.append("FAIL no email readable" if not emails else "FAIL email split across lines or cut off: " + emails[0] if (split or cut) else "PASS email: " + emails[0])
    out.append(("PASS " if len(t) > 600 else "FAIL ") + f"{len(t)} characters of real text")
    if rep.get("text_boxes"): out.append(f"FAIL {rep['text_boxes']} floating text box(es): many ATS parsers skip them")
    if rep.get("tables"): out.append(f"CHECK {rep['tables']} layout table(s): some parsers read cells out of order")
    if rep.get("contact_in_header_footer"): out.append("CHECK contact details in header/footer: some parsers ignore them")
    if rep.get("images"): out.append(f"CHECK {rep['images']} image(s): text inside images is invisible to a parser")
    if rep.get("pages", 1) > 1: out.append(f"CHECK {rep['pages']} pages")
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", t): out.append("CHECK emoji found: parsers often garble them")
    return out

if __name__ == "__main__":
    path = sys.argv[1]
    rep = docx_info(path) if path.lower().endswith(".docx") else pdf_info(path)
    rep["ats_checks"] = checks(rep)
    if "--json" in sys.argv:
        print(json.dumps(rep, indent=1, ensure_ascii=False))
    else:
        text = rep.pop("text")
        for k, v in rep.items(): print(f"{k}: {v}")
        print("\n===== TEXT AS A PARSER READS IT =====\n" + text)
```

### scripts/ats_check.py
```python
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
```
