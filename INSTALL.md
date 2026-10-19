# Install on any AI assistant

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

## Claude (web, desktop, mobile)
1. Download [`cv-jd-tailor.zip`](cv-jd-tailor.zip). Don't unzip it.
2. Go to **Settings → Capabilities** and turn on **Code execution and file creation**.
3. Under **Skills**, choose **Upload skill** and select the zip. Make sure it's switched **on**.
4. In a new chat, attach your CV, paste the JD and say *"Tailor my CV to this JD"*.

## Claude Code
```
/plugin install cv-jd-tailor --marketplace tanmay7264/Batchmates-cv-jd-tailor
```
On older versions of Claude Code, run `/plugin marketplace add tanmay7264/Batchmates-cv-jd-tailor`, then `/plugin install cv-jd-tailor@batchmates`.

## ChatGPT Skills (Business, Enterprise, Edu)
1. In the ChatGPT sidebar, open **Plugins**, then the **Skills** tab, then **Create**, then **Upload from your computer**.
2. Upload [`cv-jd-tailor.zip`](cv-jd-tailor.zip). If it asks for a folder or a single file, use `skills/cv-jd-tailor/SKILL.md` from a cloned copy of this repo.
3. Wait for the security scan. Most skills become available straight away. On Enterprise or Edu, a workspace admin may need to allow skill uploads first.
4. In a chat with file uploads enabled, attach your CV, paste the JD and ask *"Tailor my CV to this JD"*.

## ChatGPT Custom GPT (Plus, Pro)
1. Go to **Explore GPTs → Create → Configure**.
2. **Name:** `CV × JD Tailor`. **Description:** *Tailor your CV to any job description: truthful, ATS-checked, one page.*
3. **Instructions:** paste the full contents of [`PROMPT.md`](PROMPT.md).
4. **Knowledge** (optional): upload `skills/cv-jd-tailor/scripts/extract_cv.py` and `ats_check.py`.
5. **Capabilities:** turn on **Code Interpreter & Data Analysis**. This lets it read DOCX and PDF files, build the file and count keywords.
6. **Conversation starter:** `Tailor my CV to this JD`.
7. Save it as *Only me*, or *Anyone with the link* to share it.

## ChatGPT Project (any plan)
1. Create a **Project**, open its settings and paste [`PROMPT.md`](PROMPT.md) into **Instructions**.
2. Start each new role as a chat inside the project: attach your CV and paste the JD.

## OpenAI Codex (CLI, IDE, app)
Codex reads skills from `~/.agents/skills` (personal) or `.agents/skills` (per repository).
```bash
git clone https://github.com/tanmay7264/Batchmates-cv-jd-tailor
mkdir -p ~/.agents/skills
cp -r Batchmates-cv-jd-tailor/skills/cv-jd-tailor ~/.agents/skills/
pip install pdfplumber
```
Restart Codex. Then run `$cv-jd-tailor` or just ask: *"Tailor ./my_cv.pdf to the JD in ./jd.txt"*.

## Gemini Gems
1. At [gemini.google.com](https://gemini.google.com), go to **Gems → New Gem**.
2. **Name:** `CV × JD Tailor`.
3. **Instructions:** paste [`PROMPT.md`](PROMPT.md).
4. **Knowledge** (optional): add the two scripts from `skills/cv-jd-tailor/scripts/`.
5. **Save.** Open the Gem, upload your CV, paste the JD and say *"Tailor my CV to this JD"*.

Gems can't always produce a PDF. If yours returns Markdown, paste it into your original CV file section by section and export it to PDF.

## Gemini CLI
```bash
gemini skills install https://github.com/tanmay7264/Batchmates-cv-jd-tailor.git --path skills/cv-jd-tailor
pip install pdfplumber
```
Or copy the folder by hand: `cp -r skills/cv-jd-tailor ~/.gemini/skills/` (`~/.agents/skills/` also works). Then ask: *"Tailor my_cv.docx to jd.txt"*.

## Grok (xAI)
1. At [grok.com](https://grok.com), create a **Project**. If your version doesn't have Projects, use **Settings → Customize / Custom instructions**.
2. Paste [`PROMPT.md`](PROMPT.md) as the project's instructions.
3. In the project, upload your CV, paste the JD and say *"Tailor my CV to this JD"*.

If your plan doesn't allow instructions as long as `PROMPT.md`, paste it as the first message of a chat instead.

## Groq (GroqCloud)
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

## Any other chatbot
This covers Perplexity (Spaces), Microsoft Copilot, Mistral Le Chat (Agents), DeepSeek, Meta AI, Qwen, local models and similar tools.
- **If it has saved instructions** (Spaces, Agents, Projects, custom instructions): paste [`PROMPT.md`](PROMPT.md) there once.
- **If it doesn't**, start each chat with:
  ```
  Follow these instructions for this whole chat:
  <paste PROMPT.md>
  ```
  Then attach or paste your CV and the JD.
- **No file uploads?** Paste your CV as text. Use `extract_cv.py`, or copy it from your PDF.

## Any Agent-Skills-compatible tool
Many coding agents read the open `SKILL.md` format. Copy `skills/cv-jd-tailor/` into the tool's skills folder, usually `~/.agents/skills/` or `.agents/skills/`.

---

### What changes between platforms
| | Skill + code execution | Prompt only |
|---|---|---|
| Reads PDF/DOCX | ✅ | ✅ on most apps (upload); paste text otherwise |
| Keeps your exact formatting | ✅ (edits your DOCX) | ⚠️ gives you text to paste into your file |
| ATS score | **Measured** by a script | Estimated by the AI |
| One-page check | **Measured** | Check it yourself after export |
| No-fabrication rules | ✅ | ✅ (same rules) |

Platform menus change often. If a step doesn't match what you see, follow the platform's help page for "custom instructions" or "skills", then [open an issue](https://github.com/tanmay7264/Batchmates-cv-jd-tailor/issues) so this guide gets updated.

Made by **[Tanmay Narnaware](https://tanmayportfolio.me)** · [BatchMates](https://batchmates.tech)
