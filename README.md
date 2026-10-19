# BatchMates CV × JD Tailor

**A free, open AI skill that tailors your CV to a specific job description.** It works in **Claude, ChatGPT, Gemini, Codex, Grok, Groq** and any other chatbot. You get an ATS-checked, one-page PDF in your CV's own format, and nothing in it is made up.

Built by **[Tanmay Narnaware](https://tanmayportfolio.me)** for **[BatchMates](https://batchmates.tech)**, a resource ecosystem for MBA and university students.

![Agent Skill](https://img.shields.io/badge/Agent-Skill-d97757) ![Works with](https://img.shields.io/badge/Works%20with-Claude%20%7C%20ChatGPT%20%7C%20Gemini%20%7C%20Codex%20%7C%20Grok%20%7C%20Groq-2ea44f) ![License: MIT](https://img.shields.io/badge/License-MIT-blue) ![Input](https://img.shields.io/badge/Input-PDF%20%7C%20DOCX-555) ![Output](https://img.shields.io/badge/Output-1--page%20PDF-555)

---

## Why this exists
In campus placements and off-campus hiring, the first screen is usually an ATS keyword filter followed by a recruiter skim of about 7 seconds. Strong candidates get filtered out because their CV doesn't use the job description's language. Others oversell, then struggle to defend their CV in the interview.

This skill closes that gap honestly. It **mirrors the JD's wording where your experience genuinely supports it**, rewrites your bullets as measurable impact, and tells you plainly what you can't claim.

## What you get
| Step | What happens |
|---|---|
| 1. Read | Extracts your CV the way an ATS parser sees it and records its format (fonts, colours, columns, page size). Flags parsing problems: a split email, text boxes, contact details in the header, emoji. |
| 2. Score | A recruiter-style match score out of 100 on 7 weighted criteria, and the **5 missing keywords**, each tagged *Can add*, *Stretch* or *Real gap*. |
| 3. Choose | For every role, **3–4 bullet options** in Google's XYZ format ("Accomplished X, as measured by Y, by doing Z"). Fact bullets are kept separate from labelled JD-aligned reframes. You pick what goes in, and see the ATS points each section earns. |
| 4. Build | Rebuilds your CV in **your own format**. A DOCX is edited in place; a PDF has its layout reproduced with matching fonts. |
| 5. Verify | Loops until the CV reaches **ATS 90+** (or the honest ceiling), fits **one page** with the email on one line, and has **no bullets ending on 1–4 dangling words**. |
| 6. Extras (optional) | Interview guide covering every CV line, a rehearsal of the 3 hardest questions with grading, and a cover letter under 300 words. |

## The one hard rule: no fabrication
- **Never invented:** employers, titles, dates, degrees, grades, tools, clients, user counts or metrics. Every number comes from your CV or from facts you add in the chat.
- **Reframes are opt-in.** They carry a label and no numbers, and everything you keep lands on a "prepare to explain" list for your interview.
- **Real gaps are never added.** You get an honest interview bridge instead. If gaps cap your ATS score, the skill reports the ceiling rather than gaming it.

## Install

| Platform | How | Time |
|---|---|---|
| **Claude Code** | `/plugin install cv-jd-tailor --marketplace tanmay7264/Batchmates-cv-jd-tailor` | 10 sec |
| **Claude** (app) | Settings → Capabilities → Skills → Upload [`cv-jd-tailor.zip`](cv-jd-tailor.zip) | 1 min |
| **ChatGPT** Business/Enterprise/Edu | Plugins → Skills → Create → Upload the zip | 1 min |
| **ChatGPT** Free/Plus/Pro | Custom GPT or Project, with [`PROMPT.md`](PROMPT.md) as its instructions | 3 min |
| **OpenAI Codex** | Copy `skills/cv-jd-tailor` to `~/.agents/skills/` | 1 min |
| **Gemini** (app) | Gems → New Gem, with [`PROMPT.md`](PROMPT.md) as its instructions | 2 min |
| **Gemini CLI** | `gemini skills install https://github.com/tanmay7264/Batchmates-cv-jd-tailor.git --path skills/cv-jd-tailor` | 10 sec |
| **Grok** (xAI) | Project, with [`PROMPT.md`](PROMPT.md) as its instructions | 2 min |
| **Groq** | Playground, with [`PROMPT.md`](PROMPT.md) as the system prompt | 1 min |
| **Anything else** | Paste [`PROMPT.md`](PROMPT.md) as the first message | 30 sec |

👉 **Step-by-step instructions for every platform: [INSTALL.md](INSTALL.md)**

The **skill** version includes scripts that *measure* the ATS score and page fit. The **prompt** version runs the same workflow and rules on any chatbot, but the AI *estimates* those numbers.

## Use
📘 **Full step-by-step guide: [GUIDE.md](GUIDE.md).** It covers installation, preparing your inputs, choosing bullets, reading your scores, interview prep, copy-paste prompts, troubleshooting and the FAQ.

**Quick start:** start a chat and say:
> Tailor my CV to this JD

Then attach your CV and paste the job description, or link to it. Pick your bullets from the options the AI gives you, and you'll get the PDF back.

**Tips**
- Upload the **DOCX** if you have it. It keeps your formatting most faithfully.
- Add facts that aren't on your CV in the same message ("I also used Power BI in my capstone"). They count as your facts.
- Rehearse every item on the "prepare to explain" list before the interview.

## How the ATS score works
`ATS = 85% × weighted JD-keyword match in the final PDF text + 15% × parse checks (one page, email intact, readable text)`

The keyword map holds 20–30 terms taken verbatim from the JD, weighted 3/2/1, and each one is marked proven, stretch or gap. Gap terms count against the ceiling, so the score is never inflated with skills you don't have.

## Repository contents
```
.claude-plugin/
├── plugin.json               plugin manifest
└── marketplace.json          "batchmates" marketplace (one-command install)
skills/cv-jd-tailor/
├── SKILL.md                  workflow, rules, XYZ guidance, verification loop
└── scripts/
    ├── extract_cv.py         CV text as an ATS reads it, format report, ATS warnings
    └── ats_check.py          ATS score, honest ceiling, page/email checks, short-line detection
cv-jd-tailor.zip              ready-to-upload skill (Claude, ChatGPT Skills)
PROMPT.md                     portable prompt for any chatbot (<8,000 characters)
INSTALL.md                    install steps for every platform
GUIDE.md                      detailed user guide
```
The scripts need Python 3 and `pdfplumber`. The AI installs it automatically if it's missing.

## Limitations
- Rebuilding a complex two-column **PDF-only** CV from scratch is the weakest step. Upload a DOCX for the best fidelity.
- The ATS score is a transparent proxy, not any vendor's actual algorithm.
- The quality of the result depends on the facts you give it. It can't add what isn't there, by design.

## Author
**Tanmay Narnaware** is a product and growth person with a computer engineering background. He has a PGDM in E-Business from WeSchool, Mumbai, and was an exchange student at Otto-Friedrich-Universität Bamberg. He is the founder of BatchMates.

- Portfolio: [tanmayportfolio.me](https://tanmayportfolio.me)
- LinkedIn: [linkedin.com/in/ktanmayn](https://www.linkedin.com/in/ktanmayn)
- GitHub: [@tanmay7264](https://github.com/tanmay7264)
- BatchMates: [batchmates.tech](https://batchmates.tech)

Feedback, bugs and before→after scores are welcome: please [open an issue](https://github.com/tanmay7264/Batchmates-cv-jd-tailor/issues).

## License
[MIT](LICENSE) © 2026 Tanmay Narnaware
