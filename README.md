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

## Contents
- [Install on any AI assistant](#install-on-any-ai-assistant): Claude, ChatGPT, Codex, Gemini, Grok, Groq, others
- [How to use it: full guide](#how-to-use-it-full-guide)
- [The portable prompt](#the-portable-prompt-promptmd)
- [How the ATS score works](#how-the-ats-score-works)
- [Repository contents](#repository-contents)
- [Limitations](#limitations) · [Author](#author) · [License](#license)

**Quick start (any assistant):** install it using the table below, then start a chat and say *"Tailor my CV to this JD"*. Attach your CV and paste the JD, pick your bullets from the options, and you get your tailored CV back.

## Install on any AI assistant

CV × JD Tailor comes in two forms:

| Form | File | Use it on |
|---|---|---|
| **Agent Skill**: full version with helper scripts that measure the ATS score and page fit | [`skills/cv-jd-tailor/`](skills/cv-jd-tailor) or [`cv-jd-tailor.zip`](cv-jd-tailor.zip) | Claude, Claude Code, ChatGPT (Skills), OpenAI Codex, Gemini CLI, and any tool that reads `SKILL.md` |
| **Portable prompt**: the same workflow as one set of instructions (under 8,000 characters) | [`PROMPT.md`](PROMPT.md) | ChatGPT Custom GPTs and Projects, Gemini Gems, Grok, Groq, Perplexity, Copilot, Mistral, DeepSeek, Meta AI, anything with a chat box |

> **Which is better?** Use the skill wherever it's supported. Its scripts *measure* the ATS score and page count. With the prompt only, the AI *estimates* them, so check the output yourself.

**Quick picker**

| You use… | Go to |
|---|---|
| Claude (app) | [Claude](#claude-web-desktop-mobile) |
| Claude Code | [Claude Code](#claude-code) |
| ChatGPT Business / Enterprise / Edu | [ChatGPT Skills](#chatgpt-skills-business-enterprise-edu) |
| ChatGPT Free / Plus / Pro | [Custom GPT](#chatgpt-custom-gpt-plus-pro) or [Project](#chatgpt-project-any-plan) |
| OpenAI Codex | [Codex](#openai-codex-cli-ide-app) |
| Gemini (app) | [Gemini Gem](#gemini-gems) |
| Gemini CLI | [Gemini CLI](#gemini-cli) |
| Grok (xAI) | [Grok](#grok-xai) |
| Groq | [Groq](#groq-groqcloud) |
| Anything else | [Any chatbot](#any-other-chatbot) |

---

### Claude (web, desktop, mobile)
1. Download [`cv-jd-tailor.zip`](cv-jd-tailor.zip). Don't unzip it.
2. Go to **Settings → Capabilities** and turn on **Code execution and file creation**.
3. Under **Skills**, choose **Upload skill** and select the zip. Make sure it's switched **on**.
4. In a new chat, attach your CV, paste the JD and say *"Tailor my CV to this JD"*.

### Claude Code
```
/plugin install cv-jd-tailor --marketplace tanmay7264/Batchmates-cv-jd-tailor
```
On older versions of Claude Code, run `/plugin marketplace add tanmay7264/Batchmates-cv-jd-tailor`, then `/plugin install cv-jd-tailor@batchmates`.

### ChatGPT Skills (Business, Enterprise, Edu)
1. In the ChatGPT sidebar, open **Plugins**, then the **Skills** tab, then **Create**, then **Upload from your computer**.
2. Upload [`cv-jd-tailor.zip`](cv-jd-tailor.zip). If it asks for a folder or a single file, use `skills/cv-jd-tailor/SKILL.md` from a cloned copy of this repo.
3. Wait for the security scan. Most skills become available straight away. On Enterprise or Edu, a workspace admin may need to allow skill uploads first.
4. In a chat with file uploads enabled, attach your CV, paste the JD and ask *"Tailor my CV to this JD"*.

### ChatGPT Custom GPT (Plus, Pro)
1. Go to **Explore GPTs → Create → Configure**.
2. **Name:** `CV × JD Tailor`. **Description:** *Tailor your CV to any job description: truthful, ATS-checked, one page.*
3. **Instructions:** paste the full contents of [`PROMPT.md`](PROMPT.md).
4. **Knowledge** (optional): upload `skills/cv-jd-tailor/scripts/extract_cv.py` and `ats_check.py`.
5. **Capabilities:** turn on **Code Interpreter & Data Analysis**. This lets it read DOCX and PDF files, build the file and count keywords.
6. **Conversation starter:** `Tailor my CV to this JD`.
7. Save it as *Only me*, or *Anyone with the link* to share it.

### ChatGPT Project (any plan)
1. Create a **Project**, open its settings and paste [`PROMPT.md`](PROMPT.md) into **Instructions**.
2. Start each new role as a chat inside the project: attach your CV and paste the JD.

### OpenAI Codex (CLI, IDE, app)
Codex reads skills from `~/.agents/skills` (personal) or `.agents/skills` (per repository).
```bash
git clone https://github.com/tanmay7264/Batchmates-cv-jd-tailor
mkdir -p ~/.agents/skills
cp -r Batchmates-cv-jd-tailor/skills/cv-jd-tailor ~/.agents/skills/
pip install pdfplumber
```
Restart Codex. Then run `$cv-jd-tailor` or just ask: *"Tailor ./my_cv.pdf to the JD in ./jd.txt"*.

### Gemini Gems
1. At [gemini.google.com](https://gemini.google.com), go to **Gems → New Gem**.
2. **Name:** `CV × JD Tailor`.
3. **Instructions:** paste [`PROMPT.md`](PROMPT.md).
4. **Knowledge** (optional): add the two scripts from `skills/cv-jd-tailor/scripts/`.
5. **Save.** Open the Gem, upload your CV, paste the JD and say *"Tailor my CV to this JD"*.

Gems can't always produce a PDF. If yours returns Markdown, paste it into your original CV file section by section and export it to PDF.

### Gemini CLI
```bash
gemini skills install https://github.com/tanmay7264/Batchmates-cv-jd-tailor.git --path skills/cv-jd-tailor
pip install pdfplumber
```
Or copy the folder by hand: `cp -r skills/cv-jd-tailor ~/.gemini/skills/` (`~/.agents/skills/` also works). Then ask: *"Tailor my_cv.docx to jd.txt"*.

### Grok (xAI)
1. At [grok.com](https://grok.com), create a **Project**. If your version doesn't have Projects, use **Settings → Customize / Custom instructions**.
2. Paste [`PROMPT.md`](PROMPT.md) as the project's instructions.
3. In the project, upload your CV, paste the JD and say *"Tailor my CV to this JD"*.

If your plan doesn't allow instructions as long as `PROMPT.md`, paste it as the first message of a chat instead.

### Groq (GroqCloud)
Groq is a fast inference platform. It has no saved assistants, so you set the system prompt each session.
1. Open the **Playground** at [console.groq.com](https://console.groq.com) and pick a large model.
2. Paste [`PROMPT.md`](PROMPT.md) into the **System** field.
3. In the user message, paste your **CV text** (Groq chat doesn't take file uploads), then the JD.

Developers can call the API with `PROMPT.md` as the `system` message:
```python
from groq import Groq
prompt = open("PROMPT.md").read()
r = Groq().chat.completions.create(model="<a current large model>", messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": "CV:\n" + open("cv.txt").read() + "\n\nJD:\n" + open("jd.txt").read()}])
print(r.choices[0].message.content)
```
To get CV text out of a PDF or DOCX file, run `python3 skills/cv-jd-tailor/scripts/extract_cv.py my_cv.pdf`.

### Any other chatbot
This covers Perplexity (Spaces), Microsoft Copilot, Mistral Le Chat (Agents), DeepSeek, Meta AI, Qwen, local models and similar tools.
- **If it has saved instructions** (Spaces, Agents, Projects, custom instructions): paste [`PROMPT.md`](PROMPT.md) there once.
- **If it doesn't**, start each chat with:
  ```
  Follow these instructions for this whole chat:
  <paste PROMPT.md>
  ```
  Then attach or paste your CV and the JD.
- **No file uploads?** Paste your CV as text. Use `extract_cv.py`, or copy it from your PDF.

### Any Agent-Skills-compatible tool
Many coding agents read the open `SKILL.md` format. Copy `skills/cv-jd-tailor/` into the tool's skills folder, usually `~/.agents/skills/` or `.agents/skills/`.

---

#### What changes between platforms
| | Skill + code execution | Prompt only |
|---|---|---|
| Reads PDF/DOCX | ✅ | ✅ on most apps (upload); paste text otherwise |
| Keeps your exact formatting | ✅ (edits your DOCX) | ⚠️ gives you text to paste into your file |
| ATS score | **Measured** by a script | Estimated by the AI |
| One-page check | **Measured** | Check it yourself after export |
| No-fabrication rules | ✅ | ✅ (same rules) |

Platform menus change often. If a step doesn't match what you see, follow the platform's help page for "custom instructions" or "skills", then [open an issue](https://github.com/tanmay7264/Batchmates-cv-jd-tailor/issues) so this guide gets updated.

## How to use it: full guide

### What you need
- An AI assistant from the [install table](#install-on-any-ai-assistant). One with **code execution** gives the best results: Claude, ChatGPT, Gemini or Codex.
- **Your current CV** as a PDF or Word (.docx) file.
- **The job description**: the full text is best, but a link works if the AI can open it.
- About **10–15 minutes** for the first run.

### Prepare your inputs

**Your CV**
- **Upload the .docx if you have it.** The AI edits it in place, so fonts, spacing and layout stay exactly as they are.
- A PDF works too. The AI reproduces the layout, but complex two-column designs may come out slightly different.
- Your CV should contain **everything true** about you: tools, numbers, projects. The skill can't add facts it doesn't know.

**The job description**
- Paste the **full JD**, including responsibilities, requirements and "nice to have". More text gives a better keyword map.
- Add the **company and role** if they aren't obvious from the JD.

**Extra facts (optional, but powerful)**
If something true isn't on your CV, say so in the same message, for example:
> I also used SQL and Power BI in my capstone project; I led a 6-person team in the college fest.

Anything you state in the chat counts as your fact.

### Run it: the full walkthrough

#### Step 1: Start
Open a new chat, attach your CV, and send:
> Tailor my CV to this JD. Company: ___, Role: ___.
> [paste JD]

#### Step 2: The AI reads your CV (automatic)
The AI extracts the text **exactly as an ATS parser sees it**, records your format, and flags problems such as:
- an email split across two lines, so recruiters can't copy it
- text boxes or headers that some ATS systems skip
- emoji or images that parsers garble

#### Step 3: You receive the plan
This is the most important message. It contains:

| Part | What it means |
|---|---|
| **Match score (/100)** | How a recruiter would rate your current CV for this role, on 7 weighted criteria. Comes with a one-line verdict. |
| **5 missing keywords** | Each tagged **Can add** (you have the evidence), **Stretch** (partial evidence) or **Real gap** (you don't have it). |
| **ATS keyword map** | 20–30 terms from the JD, weighted 3/2/1. |
| **Bullet options** | 3–4 per role, numbered. ★ marks the recommended one-page set. |
| **Skills & certifications** | A recommended list plus extras to pick from. |
| **Section ATS points** | What each section contributes, and what you lose if you cut it. |

#### Step 4: Reply with your picks
For example:
> Summary: 2. Company A: 1, 2, 4. Internship: 1, 3. Projects: 2, 5. Skills: recommended + Figma. Go.

Or simply:
> Go with the ★ set.

#### Step 5: The AI builds and checks (automatic)
The AI builds the CV in your format, then checks it in a loop (up to 3 rounds):
- ATS score **90+**, or the honest ceiling if real gaps prevent it
- **one page**
- email intact on one line
- no bullet ending on a line of only 1–4 words
- every number traced back to your facts

#### Step 6: Download your PDF
You get the PDF (and the edited .docx if you uploaded one), plus a short summary covering:
- the score before → after
- what changed
- what to prepare to explain
- real gaps and how to handle them in the interview

### How to choose bullets in the plan
Each bullet option has a tag:
- **`[XYZ]`** is the strongest: result, number and method. Prefer these.
- **`[no Y]`** has no number; it uses scope (team size, users, markets) instead. Fine when there's no metric.
- **`[no Z]`** has a result but no method. Use it sparingly.
- **JD-aligned reframe** describes your real work in the JD's vocabulary, with no numbers. Pick one only if you can talk about it confidently for 2 minutes.

**Rules of thumb**
- 3–4 bullets for your most relevant role, 2–3 for the others.
- One reframe per role at most. Recruiters probe the JD words they see on your CV.
- If two bullets say the same thing in different words, keep the one with the number.
- Don't pick a bullet just because it contains a keyword. The summary and skills sections can carry keywords too.

### Reading your results

#### Match score vs ATS score
- The **match score** is a human recruiter's judgement: experience, domain, education, impact. Tailoring usually improves it by 5–15 points. Big jumps are rare, because experience can't be faked.
- The **ATS score** measures keyword coverage plus parse checks. Here 90+ is realistic when your experience fits the role.

#### The "honest ceiling"
If the JD asks for things you don't have (say, 5 years of Java), those terms stay off your CV. The ceiling tells you the highest score you can reach truthfully. **A ceiling below 80 usually means the role is a stretch for your profile**, so it may be better to spend the effort on a better-matched role.

#### "Prepare to explain"
Every stretch item and reframe you kept appears here. Before the interview, prepare one concrete story for each: what you did, how, and the result.

### Interview guide, rehearsal and cover letter
After delivery, ask for any of these:

| Ask | You get |
|---|---|
| *"Make the interview guide"* | A 30-second pitch; for every CV line, the real story, a STAR outline, 2 likely follow-ups and what not to say; a numbers cheat sheet; questions to ask them. |
| *"Rehearse the 3 hardest questions"* | The AI plays the hiring manager. After each of your answers you get a score /10, what worked, what was missing, and the likely follow-up. |
| *"Write the cover letter"* | Under 300 words: the company's problem, then your top 3 relevant wins, then a concrete next step. No clichés. |

### Prompts you can copy

**Standard run**
```
Tailor my CV to this JD. Company: <company>, Role: <role>.
Extra facts not on my CV: <optional>.
<paste JD>
```

**Fast run (skip choosing)**
```
Tailor my CV to this JD and go straight to the ★ recommended set. Then give me the PDF.
<paste JD>
```

**Just the diagnosis**
```
Only score my CV against this JD and list the 5 missing keywords. Don't rebuild it yet.
<paste JD>
```

**Second role, same chat**
```
Same CV, new JD. Company: <company>, Role: <role>.
<paste JD>
```

**Fix one thing**
```
In the final CV, shorten the second bullet under my latest role and swap Project 3 for Project 5. Keep one page.
```

### Applying to many roles
- **Group similar JDs** (for example, all Product Analyst roles). Tailor once per group, then make small edits per company.
- **Use one chat per role group**, so the AI keeps your choices and extra facts.
- **Name files clearly**: `Name_Company_Role.pdf`. Recruiters see the filename.
- **Track the honest ceiling.** Roles with a ceiling of 90+ are where to put most of your effort.

### Troubleshooting

| Problem | Fix |
|---|---|
| The AI doesn't use the skill | Check the skill is enabled, or that `PROMPT.md` is in the instructions, then say *"use the cv-jd-tailor skill"*. |
| "Code execution not available" | Turn on code execution (Claude: Settings → Capabilities; ChatGPT GPT: Code Interpreter), or use the prompt version, which returns text. |
| The layout looks different from my original | Upload the **.docx** instead of the PDF. |
| The CV spills onto 2 pages | Ask: *"Cut the least relevant bullet and tighten wording to fit one page."* |
| The ATS score is stuck below 90 | Check the missing terms. If they're real gaps, that's the honest ceiling. If they're true for you, tell the AI the fact and it will add the term. |
| A bullet claims too much | Say: *"Bullet X overstates my role. Rewrite it as support/contribution."* |
| The JD link didn't load | Paste the JD text instead. |
| A font isn't the same | The AI uses a metric-identical free font (e.g. Liberation Serif for Times New Roman). Spacing is unchanged; tell the AI if you'd prefer otherwise. |

### FAQ

**Will it make things up to hit 90?**
No. It only uses facts from your CV and the chat. Gaps are reported, never added.

**Is my CV stored or shared?**
The skill doesn't publish or upload anything. Your files stay in your AI chat, under your account's normal data settings.

**Does a 90+ ATS score guarantee a shortlist?**
No. It means your CV passes keyword screening and reads cleanly. A human recruiter still judges your experience, and that's where the XYZ bullets help.

**Can I use it for non-MBA roles?**
Yes. It works for any CV and any JD, in any field.

**Can I use it in languages other than English?**
The workflow works in other languages, but the ATS checker matches keywords literally, so keep the JD and the CV in the same language.

**Found a bug or have a suggestion?**
[Open an issue](https://github.com/tanmay7264/Batchmates-cv-jd-tailor/issues). Sharing your before → after score helps improve the skill.

## The portable prompt (`PROMPT.md`)
Paste this into any assistant's custom instructions (GPT, Gem, Project, Space, system prompt), or send it as the first message of a chat. It's also available as a file: [`PROMPT.md`](PROMPT.md).

<details>
<summary><b>Show the full prompt</b> (click to expand, then copy)</summary>

```text
You are CV × JD Tailor (by Tanmay Narnaware, BatchMates). The user gives you their CV (file or pasted text) and a job description (JD). You return the strongest TRUTHFUL version of their CV for that role, in their CV's own format, on one page, optimised for ATS keyword screening.

GROUND RULES (never break)
1. Never invent. No new employers, titles, dates, degrees, grades, certifications, awards, tools, clients, user counts or metrics. Every number must come from their CV or facts they state in this chat. Never merge two separate numbers.
2. Keep their format: same section order, headings, bullet style, date placement and page count. Only content changes.
3. Reframes are opt-in. You may offer bullets that describe their real work in the JD's words. Label them "JD-aligned reframe", put no numbers in them, and use them only if the user picks them. List every reframe kept under "Prepare to explain".
4. Partial evidence = "Stretch": phrase it defensibly ("contributed to", "supported", "exposure to") and list it under "Prepare to explain".
5. Real gaps stay out of the CV, skills included. Report them with an honest interview bridge.
6. Ask little: at most 2 questions per run, only when the answer changes the CV. Don't ask whether they did something; offer it as an option.

STEP 0 — INTAKE
Need: CV and JD. If one is missing, ask once for both. Invite optional extras in the same message: company and role, true facts missing from the CV, and whether they want a cover letter or interview prep.

STEP 1 — READ
Read the whole CV and note its format. Flag ATS risks: email split across lines, text boxes, two-column layout, tables, contact details in the header or footer, images, emoji. Build an internal FACTS SHEET of every role, date, metric, tool, skill, certification and achievement. It is your only source of truth.

STEP 2 — PLAN (send, then wait for their picks)
a) MATCH SCORE /100, judged as a recruiter: JD keyword match 20, depth of relevant experience 25, domain fit 15, quantified impact 10, education 15, presentation/ATS 10, risk signals 5. Show the table and a one-line blunt verdict.
b) 5 MISSING KEYWORDS, each tagged Can add (say where), Stretch, or Real gap (with an interview bridge).
c) ATS KEYWORD MAP: 20–30 JD terms, in the JD's exact wording, each weighted 3/2/1 and marked proven/stretch/gap.
d) OPTIONS, numbered so they can reply "Exp A: 1,3,4":
   - every role: 3–4 bullets in XYZ form, mixing fact bullets with 1–2 labelled reframes
   - summary: 2 versions
   - projects/achievements: 4–6 candidates
   - mark the recommended one-page set with ★
   Tag each bullet [XYZ], [no Y] or [no Z].
e) SKILLS: a recommended list from their real skills plus a pick list. Tell them they can add their own.
f) PROJECTED ATS for the ★ set, and the points each section adds.

XYZ RULE: "Accomplished X, as measured by Y, by doing Z." Put the result first. Y must be a real number from the facts sheet; otherwise use real scope (team size, users, markets, duration), never an invented %. Z uses the JD's words where true. Size each bullet to fill its last line well; never end on 1–4 dangling words.

STEP 3 — BUILD
Use exactly what they picked. Polish flow, remove repetition, keep JD terms verbatim. Fix ATS risks while keeping the look: email on one line, no emoji, contact details in the body text.
Output, by capability:
- If you can run code: edit their DOCX in place (python-docx, keep styles and runs) or rebuild the layout as HTML and print it to an A4/Letter PDF. Return the file.
- If you can't run code: return the full final CV as clean Markdown, mirroring their sections and order, ready to paste into their original file section by section. Say which lines replace which.

STEP 4 — VERIFY (repeat until it passes, max 3 rounds)
- ATS SCORE = 85 × (sum of weights of map terms found verbatim in the final CV ÷ total weight) + 15 × (one page? email intact? plain text readable? ÷ 3). Target 90+. If gap terms cap it, report the honest ceiling = the score if every proven/stretch term were present. Never add gap terms.
- Missing proven or stretch terms: add them verbatim where earned, or in skills.
- Too long for one page: tighten wording, then cut the least relevant bullet. Never drop a whole section.
- Every number appears in the facts sheet. Nothing invented.
If you can run code, count keywords with a script on the final text and check the page count. Otherwise count carefully and say the score is estimated.

STEP 5 — DELIVER (max 8 lines plus the file/CV)
Match score before → after; ATS score (or honest ceiling); what changed; ATS fixes made; Prepare to explain (every stretch/reframe kept); real gaps + one-line bridges; "Upload the PDF unless the portal asks for DOCX." Then offer: interview guide / 3-question rehearsal / cover letter.

EXTRAS (on request)
- Interview guide: a 30-sec pitch; for each CV bullet the real story, a STAR outline, 2 likely follow-ups and what not to say; numbers cheat sheet; how to discuss stretch items honestly; 3 smart questions to ask.
- Rehearsal: play the hiring manager. Ask the 3 hardest realistic questions one at a time. After each answer: score /10, what landed, what was missing, a strong answer using only their facts, the likely follow-up.
- Cover letter (<300 words): the company's real problem from the JD, then their top 3 relevant wins with real numbers, then a concrete next step. Plain words. Banned: excited to apply, passionate, leverage, synergy, fast-paced, great fit, dynamic, thrilled, delve, rhetorical questions.

STYLE: direct, specific, no fluff. Treat the CV as private data; don't repeat contact details unnecessarily.
```
</details>

## How the ATS score works
`ATS = 85% × weighted JD-keyword match in the final PDF text + 15% × parse checks (one page, email intact, readable text)`

The keyword map holds 20–30 terms taken verbatim from the JD, weighted 3/2/1, and each one is marked proven, stretch or gap. Gap terms count against the ceiling, so the score is never inflated with skills you don't have.

## Repository contents
```
.claude-plugin/
├── plugin.json               plugin manifest (Claude Code)
└── marketplace.json          "batchmates" marketplace (one-command install)
skills/cv-jd-tailor/
├── SKILL.md                  workflow, rules, XYZ guidance, verification loop
└── scripts/
    ├── extract_cv.py         CV text as an ATS reads it, format report, ATS warnings
    └── ats_check.py          ATS score, honest ceiling, page/email checks, short-line detection
cv-jd-tailor.zip              ready-to-upload skill (Claude, ChatGPT Skills)
PROMPT.md                     portable prompt for any chatbot (<8,000 characters)
README.md                     this file: install, guide, FAQ
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
