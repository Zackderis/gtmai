# GTMAI for ChatGPT: install guide ({VERSION})

GTMAI runs as a **skill** inside ChatGPT. It uses three official ChatGPT plugins: **Apollo.io**, **Gamma** and **Fireflies**.

## What you need
- **Any paid ChatGPT plan** (Plus, Pro, Business, Enterprise or Edu). Skills live under **Plugins**.
- **Accounts with Apollo.io, Gamma and Fireflies.** Gamma uses about 100-150 credits per deck, so a paid Gamma plan covers a full campaign.

## Option A: upload the skill
1. In ChatGPT (web or desktop), click **Plugins** in the sidebar, then the **Skills** tab.
2. Click **Create → Upload from your computer**, and choose `GTMAI for ChatGPT.zip`.
3. Wait for the scan to show **Available**. If it says **Needs Review**, your workspace admin approves it.

## Option B: install the plugin (once GTMAI is listed in the Plugin Directory)
1. Click **Plugins** in the sidebar and search **GTMAI**.
2. Click **Install plugin**.

## Connect the three tools (both options)
In **Plugins**, search for each of these, then click **Install plugin → Connect** and approve:
1. **Apollo.io**
2. **Gamma** (pick your workspace)
3. **Fireflies**

## Run it
1. Start a new chat and switch the top toggle to **Work**.
2. Set thinking effort to **Medium** or higher (click the model name next to the send button). On **Light**, ChatGPT can skip reading the skill.
3. Type **/** and pick **gtmai** from the Skills list, then type **start** and send.
   - Don't just type "start GTMAI" without picking the skill. ChatGPT may hand the request to Apollo's own GTM planning tool or to old chats in its memory instead.
4. GTMAI walks you through every stage and asks before it spends credits or sends anything.
5. ChatGPT may also show its own approval prompt before Apollo or Gamma actions. That's normal: check it, then approve.

## If a tool won't connect
Type **done** anyway when GTMAI asks. It switches that tool to **manual mode**:
- **Apollo:** you export a CSV.
- **Gamma:** you paste a prompt it writes.
- **Fireflies:** you paste the call transcript.

Your campaign still runs.

## Known limits (checked 2 Nov 2026)
- OpenAI hasn't published size or file limits for skills. This skill is about 150 KB unzipped.
- Custom GPTs are being retired on 11 Dec 2026. GTMAI is deliberately built as a skill and plugin, not a GPT.
