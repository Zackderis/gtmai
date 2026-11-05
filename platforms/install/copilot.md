# GTMAI for Microsoft 365 Copilot: install guide

GTMAI runs as an **Agent Skill** inside a Microsoft 365 Copilot agent.

## What you need
- **A Microsoft 365 Copilot licence,** or pay-as-you-go access.
  - A **work or school** account. Personal Microsoft accounts (free Copilot or Microsoft 365 Personal/Family) have no Agents or Skills, so they can't install GTMAI.
  - Agent skills may still be a preview.
  - If **Skills** doesn't show up in Agent Builder, ask your IT admin.
- **To connect Apollo and Fireflies automatically: Copilot Studio.** It's licensed separately, and your admin may control it.
  - Without it, GTMAI still works: Apollo and Fireflies run in manual mode.
- Accounts with Apollo.io, Gamma and Fireflies.

## Create the agent and add the skill
1. Go to **m365.cloud.microsoft**, then **Agents & Skills → New agent**.
2. Name it **GTMAI**. For the instructions, use: *"Follow the GTMAI skill. Start with Stage 0 when the user says start GTMAI."*
3. On the **Configure** tab, open **Skills → Add**, and upload `gtmai-copilot.zip`. Upload the whole zip, not SKILL.md on its own.
4. Switch on **web search** (web grounding) for the agent.
5. Test it on the **Try it** tab, then **Create**.

## Connect the three tools
1. **Gamma:** in Copilot, open the **Agent Store**, search **Gamma**, and add it. Your admin may need to approve it.
2. **Apollo.io** (needs Copilot Studio):
   1. Copy the agent to Copilot Studio.
   2. Go to **Tools → Add a tool → New tool → Model Context Protocol**.
   3. Enter URL `https://mcp.apollo.io/mcp`, choose **OAuth 2.0 (Dynamic discovery)**, and sign in.
3. **Fireflies** (needs Copilot Studio): same steps as Apollo, with URL `https://api.fireflies.ai/mcp`.

## Run it
Chat with your **GTMAI agent** and type **start GTMAI**.

## If a tool won't connect
Type **done** anyway when GTMAI asks. It switches that tool to **manual mode**:
- **Apollo:** you export a CSV.
- **Gamma:** you paste a prompt it writes.
- **Fireflies:** you paste the call transcript.

## Free Copilot (personal Microsoft account): not recommended
Free Copilot has no Agents or Skills, so GTMAI can only be attached to a chat as a file. Tested 2 Nov 2026:
1. **Attaching fails until OneDrive is set up.** Copilot saves attachments to OneDrive, so open **onedrive.live.com** and sign in once first. Otherwise every upload shows "Unexpected error occurred".
2. Attach `gtmai-copilot-all-in-one.md` and type **Follow this file exactly. start GTMAI**. It starts the welcome.
3. **It then hits free Copilot's daily limit after one reply.** The file is too big for the free allowance, so a campaign can't actually run. Use Claude, ChatGPT, Gemini or Grok, or a Microsoft 365 Copilot work account.

## For developers: GitHub Copilot
GitHub Copilot (VS Code agent mode and the Copilot CLI) reads the same skill folder natively:
1. Unzip it to `~/.copilot/skills/gtmai/`, or to `.github/skills/gtmai/` in a project.
2. Add the Apollo, Gamma and Fireflies MCP servers in your editor's MCP settings.

## Known limits (checked 2 Nov 2026)
- Skill zip: 50 MB maximum and 8 skills per agent. SKILL.md must be under 20,000 characters; this one is built to fit.
- Agent Builder itself can't add MCP tools. That needs Copilot Studio.
