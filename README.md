# cv-jd-tailor: a Claude skill that tailors your CV to a job description

Upload your CV (PDF or DOCX) and a job description. You get back the strongest **truthful** version of your CV for that role: same format, ATS-checked, on one page, as a PDF.

## What it does
1. **Reads your CV** and records its format: fonts, colours, columns and page size. It also flags ATS problems like a split email, text boxes or contact details in the header.
2. **Scores your CV against the JD** the way a recruiter would (/100) and lists the 5 missing keywords, each tagged *Can add*, *Stretch* or *Real gap*.
3. **Gives you options** for each role: 3–4 bullets in Google's XYZ format ("Accomplished X, as measured by Y, by doing Z"). Fact bullets are kept separate from labelled JD-aligned reframes. You pick.
4. **Builds the CV in your own format.** A DOCX is edited in place; a PDF has its layout rebuilt.
5. **Checks the result in a loop:** ATS score 90+ (or the honest ceiling), one page, email on one line, and no bullets that end on 1–4 dangling words.
6. **Optional extras:** an interview guide, a hardest-questions rehearsal and a cover letter under 300 words.

**It never invents anything.** No new employers, titles, tools, metrics or dates. JD requirements you can't back up are reported as gaps, with a suggested interview bridge; they are never added to the CV.

## Install
1. Download [`cv-jd-tailor.zip`](cv-jd-tailor.zip).
2. In Claude, go to **Settings → Capabilities**, turn on code execution, then under **Skills** choose **Upload skill** and select the zip.
3. Start a chat: *"Tailor my CV to this JD"*, attach your CV and paste the JD.

Claude Code: copy the `cv-jd-tailor/` folder into `~/.claude/skills/`.

## Tips
- Upload the **DOCX** if you have it. It keeps your formatting most faithfully.
- Treat every item listed under "prepare to explain" as something you will be asked about in the interview.

## Files
- `cv-jd-tailor/SKILL.md`: the workflow and rules.
- `cv-jd-tailor/scripts/extract_cv.py`: CV text, format report and ATS warnings.
- `cv-jd-tailor/scripts/ats_check.py`: ATS keyword score, page and email checks, short-line detection.

MIT licensed. Built by [Tanmay Narnaware](https://tanmayportfolio.me).
