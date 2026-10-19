# User Guide: BatchMates CV × JD Tailor

A step-by-step guide, from installing the skill to an interview-ready CV. Built by **[Tanmay Narnaware](https://tanmayportfolio.me)** for **[BatchMates](https://batchmates.tech)**.

**Contents**
1. [What you need](#1-what-you-need)
2. [Install the skill](#2-install-the-skill)
3. [Prepare your inputs](#3-prepare-your-inputs)
4. [Run it: the full walkthrough](#4-run-it-the-full-walkthrough)
5. [How to choose bullets in the plan](#5-how-to-choose-bullets-in-the-plan)
6. [Reading your results](#6-reading-your-results)
7. [Interview guide, rehearsal and cover letter](#7-interview-guide-rehearsal-and-cover-letter)
8. [Prompts you can copy](#8-prompts-you-can-copy)
9. [Applying to many roles](#9-applying-to-many-roles)
10. [Troubleshooting](#10-troubleshooting)
11. [FAQ](#11-faq)

---

## 1. What you need
- A **Claude account** with skills and code execution available. Skills are on Free, Pro, Max, Team and Enterprise plans; availability can change, so check Claude's settings.
- **Your current CV** as a PDF or Word (.docx) file.
- **The job description**: the full text is best, but a link works if Claude can open it.
- About **10–15 minutes** for the first run.

## 2. Install the skill

### Option A: Claude app (web, desktop or mobile)
1. Download **[`cv-jd-tailor.zip`](cv-jd-tailor.zip)** from this repo. Click the file, then the download button. Don't unzip it.
2. Open Claude and go to **Settings → Capabilities**.
3. Turn on **Code execution and file creation**. The skill needs it to read your CV and build the PDF.
4. In the **Skills** section, click **Upload skill** and choose `cv-jd-tailor.zip`.
5. Make sure **cv-jd-tailor** is switched **on** in the list.

> On a Team or Enterprise plan, an admin may need to allow skill uploads first.

### Option B: Claude Code (plugin)
In a Claude Code session, run:
```
/plugin install cv-jd-tailor --marketplace tanmay7264/Batchmates-cv-jd-tailor
```
On older versions of Claude Code, run `/plugin marketplace add tanmay7264/Batchmates-cv-jd-tailor`, then `/plugin install cv-jd-tailor@batchmates`. To get updates, run `/plugin marketplace update batchmates`.

The helper scripts need `pdfplumber` (`pip install pdfplumber`). For PDF-only CVs you'll also want Playwright with Chromium. For DOCX CVs, LibreOffice (`soffice`) handles the conversion.

### Check it worked
In a new chat, ask: *"What skills do you have for CVs?"* Claude should mention **cv-jd-tailor**.

## 3. Prepare your inputs

**Your CV**
- **Upload the .docx if you have it.** Claude edits it in place, so fonts, spacing and layout stay exactly as they are.
- A PDF works too. Claude reproduces the layout, but complex two-column designs may come out slightly different.
- Your CV should contain **everything true** about you: tools, numbers, projects. The skill can't add facts it doesn't know.

**The job description**
- Paste the **full JD**, including responsibilities, requirements and "nice to have". More text gives a better keyword map.
- Add the **company and role** if they aren't obvious from the JD.

**Extra facts (optional, but powerful)**
If something true isn't on your CV, say so in the same message, for example:
> I also used SQL and Power BI in my capstone project; I led a 6-person team in the college fest.

Anything you state in the chat counts as your fact.

## 4. Run it: the full walkthrough

### Step 1: Start
Open a new chat, attach your CV, and send:
> Tailor my CV to this JD. Company: ___, Role: ___.
> [paste JD]

### Step 2: Claude reads your CV (automatic)
Claude extracts the text **exactly as an ATS parser sees it**, records your format, and flags problems such as:
- an email split across two lines, so recruiters can't copy it
- text boxes or headers that some ATS systems skip
- emoji or images that parsers garble

### Step 3: You receive the plan
This is the most important message. It contains:

| Part | What it means |
|---|---|
| **Match score (/100)** | How a recruiter would rate your current CV for this role, on 7 weighted criteria. Comes with a one-line verdict. |
| **5 missing keywords** | Each tagged **Can add** (you have the evidence), **Stretch** (partial evidence) or **Real gap** (you don't have it). |
| **ATS keyword map** | 20–30 terms from the JD, weighted 3/2/1. |
| **Bullet options** | 3–4 per role, numbered. ★ marks the recommended one-page set. |
| **Skills & certifications** | A recommended list plus extras to pick from. |
| **Section ATS points** | What each section contributes, and what you lose if you cut it. |

### Step 4: Reply with your picks
For example:
> Summary: 2. Apexon: 1, 2, 4. Internship: 1, 3. Projects: 2, 5. Skills: recommended + Figma. Go.

Or simply:
> Go with the ★ set.

### Step 5: Claude builds and checks (automatic)
Claude builds the CV in your format, then checks it in a loop (up to 3 rounds):
- ATS score **90+**, or the honest ceiling if real gaps prevent it
- **one page**
- email intact on one line
- no bullet ending on a line of only 1–4 words
- every number traced back to your facts

### Step 6: Download your PDF
You get the PDF (and the edited .docx if you uploaded one), plus a short summary covering:
- the score before → after
- what changed
- what to prepare to explain
- real gaps and how to handle them in the interview

## 5. How to choose bullets in the plan
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

## 6. Reading your results

### Match score vs ATS score
- The **match score** is a human recruiter's judgement: experience, domain, education, impact. Tailoring usually improves it by 5–15 points. Big jumps are rare, because experience can't be faked.
- The **ATS score** measures keyword coverage plus parse checks. Here 90+ is realistic when your experience fits the role.

### The "honest ceiling"
If the JD asks for things you don't have (say, 5 years of Java), those terms stay off your CV. The ceiling tells you the highest score you can reach truthfully. **A ceiling below 80 usually means the role is a stretch for your profile**, so it may be better to spend the effort on a better-matched role.

### "Prepare to explain"
Every stretch item and reframe you kept appears here. Before the interview, prepare one concrete story for each: what you did, how, and the result.

## 7. Interview guide, rehearsal and cover letter
After delivery, ask for any of these:

| Ask | You get |
|---|---|
| *"Make the interview guide"* | A 30-second pitch; for every CV line, the real story, a STAR outline, 2 likely follow-ups and what not to say; a numbers cheat sheet; questions to ask them. |
| *"Rehearse the 3 hardest questions"* | Claude plays the hiring manager. After each of your answers you get a score /10, what worked, what was missing, and the likely follow-up. |
| *"Write the cover letter"* | Under 300 words: the company's problem, then your top 3 relevant wins, then a concrete next step. No clichés. |

## 8. Prompts you can copy

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
In the final CV, shorten the second Apexon bullet and swap Project 3 for Project 5. Keep one page.
```

## 9. Applying to many roles
- **Group similar JDs** (for example, all Product Analyst roles). Tailor once per group, then make small edits per company.
- **Use one chat per role group**, so Claude keeps your choices and extra facts.
- **Name files clearly**: `Name_Company_Role.pdf`. Recruiters see the filename.
- **Track the honest ceiling.** Roles with a ceiling of 90+ are where to put most of your effort.

## 10. Troubleshooting

| Problem | Fix |
|---|---|
| Claude doesn't use the skill | Check it's switched on under Settings → Capabilities → Skills, and say *"use the cv-jd-tailor skill"*. |
| "Code execution not available" | Turn on code execution in Settings → Capabilities. |
| The layout looks different from my original | Upload the **.docx** instead of the PDF. |
| The CV spills onto 2 pages | Ask: *"Cut the least relevant bullet and tighten wording to fit one page."* |
| The ATS score is stuck below 90 | Check the missing terms. If they're real gaps, that's the honest ceiling. If they're true for you, tell Claude the fact and it will add the term. |
| A bullet claims too much | Say: *"Bullet X overstates my role. Rewrite it as support/contribution."* |
| The JD link didn't load | Paste the JD text instead. |
| A font isn't the same | Claude uses a metric-identical free font (e.g. Liberation Serif for Times New Roman). Spacing is unchanged; tell Claude if you'd prefer otherwise. |

## 11. FAQ

**Will it make things up to hit 90?**
No. It only uses facts from your CV and the chat. Gaps are reported, never added.

**Is my CV stored or shared?**
The skill doesn't publish or upload anything. Your files stay in your Claude conversation, under your account's normal data settings.

**Does a 90+ ATS score guarantee a shortlist?**
No. It means your CV passes keyword screening and reads cleanly. A human recruiter still judges your experience, and that's where the XYZ bullets help.

**Can I use it for non-MBA roles?**
Yes. It works for any CV and any JD, in any field.

**Can I use it in languages other than English?**
The workflow works in other languages, but the ATS checker matches keywords literally, so keep the JD and the CV in the same language.

**Found a bug or have a suggestion?**
[Open an issue](https://github.com/tanmay7264/Batchmates-cv-jd-tailor/issues). Sharing your before → after score helps improve the skill.

---
Made by **Tanmay Narnaware** · [tanmayportfolio.me](https://tanmayportfolio.me) · [LinkedIn](https://www.linkedin.com/in/ktanmayn) · [BatchMates](https://batchmates.tech) · MIT licence
