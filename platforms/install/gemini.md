# GTMAI for Gemini: install guide

GTMAI runs as a **skill** in the Gemini app (gemini.google.com). It connects to **Apollo.io**, **Gamma** and **Fireflies** as **custom apps**, or runs them in manual mode.

## What you need
- **A personal Google account,** aged 18+, with **Keep Activity** turned on. Skills are free.
  - Skills are still rolling out to personal accounts through mid-November 2026.
  - Workspace (work) accounts are on hold for now.
- **To connect the tools automatically:** custom apps currently need a **US** personal account in English.
  - Everyone else can still use GTMAI. The tools run in manual mode.
- Accounts with Apollo.io, Gamma and Fireflies.

## Install the skill (desktop web)
1. In Gemini on the web, open **Customise** in the sidebar, then the **Skills** tab → **Create → Upload**.
2. Choose `gtmai-gemini.zip`, then click **Continue**. Gemini fills in the name, description, instructions and files.
3. Click **Save skill**.
4. **Updating later:** on the skill's **⋮ → Replace skill**, upload the new zip, then open **⋮** again and click **Activate**. Replacing switches the skill off.

Install it on desktop web: uploaded skills can't be edited on mobile yet.

## Connect the three tools (US personal accounts)
In Gemini on the web, go to **Settings → Connected Apps → Custom apps → Add a custom app**. Add each of these, signing in when asked:
1. **Apollo.io:** `https://mcp.apollo.io/mcp`
2. **Gamma:** `https://mcp.gamma.app/mcp`
3. **Fireflies:** `https://api.fireflies.ai/mcp`

## Run it
1. In a new chat, pick a **Thinking** or **Pro** model if you have one (the fast model can skip steps), then type **start GTMAI**.
2. When a step needs a tool, GTMAI may ask you to start your reply with **@Apollo**, **@Gamma** or **@Fireflies**.
3. Gemini asks you to confirm actions that change things, like saving contacts, creating a sequence or building a deck. Check them and confirm.

## If a tool won't connect
Type **done** anyway when GTMAI asks. It switches that tool to **manual mode**:
- **Apollo:** you export a CSV.
- **Gamma:** you paste a prompt it writes.
- **Fireflies:** you paste the call transcript.

## Known limits (checked 2 Nov 2026)
- The skill must be re-uploaded to update it.
- Skills don't run inside Canvas or Deep Research.
- Google hasn't confirmed that Apollo's, Gamma's and Fireflies' MCP servers all complete Gemini's sign-in. If one doesn't, manual mode covers it.
