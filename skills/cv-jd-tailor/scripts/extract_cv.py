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
