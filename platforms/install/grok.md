# GTMAI for Grok: install guide

GTMAI runs as a **skill** in Grok (grok.com, iOS and Android). It uses **Gamma** (a built-in Grok connector) plus **Apollo.io** and **Fireflies** (custom connectors).

## What you need
- A Grok account. Skills and custom connectors work best on a paid plan: SuperGrok, or X Premium+.
- Accounts with Apollo.io, Gamma and Fireflies.

## Install the skill
1. Go to **grok.com/skills** and upload `gtmai-grok.zip`.
2. **If the upload isn't accepted:** start a new chat, attach `gtmai-grok-all-in-one.md`, and say: *"Save this as a skill called GTMAI."*
   - Grok hasn't published its skill format.
   - The all-in-one file holds the entire skill in one document, so nothing depends on Grok loading the extra reference files.

## Connect the three tools
Go to **grok.com/connectors**:
1. **Gamma:** find it in the list and click **Connect**.
2. **Apollo.io:** click **New Connector → Custom**. Name it `Apollo.io`, use URL `https://mcp.apollo.io/mcp`, save, and sign in to Apollo.
3. **Fireflies:** click **New Connector → Custom**. Name it `Fireflies`, use URL `https://api.fireflies.ai/mcp`, save, and sign in to Fireflies.

On Business or Enterprise plans, your admin may need to allow custom connectors first.

## Using Grok Bot instead
If you use Grok Bot:
1. Open a Bot.
2. Attach the all-in-one file and say *"Save this process as a skill called GTMAI"*.
3. Add the three tools under **Connect apps** (Apollo and Fireflies by their MCP URLs above).

## Run it
In a new chat, type **start GTMAI**. GTMAI walks you through every stage and asks before it spends credits or sends anything.

## If a tool won't connect
Type **done** anyway when GTMAI asks. It switches that tool to **manual mode**:
- **Apollo:** you export a CSV.
- **Gamma:** you paste a prompt it writes.
- **Fireflies:** you paste the call transcript.

## Known limits (checked 2 Nov 2026)
- xAI hasn't published a skill file format or limits. Test the zip upload first, and use the all-in-one file as the fallback.
- Apollo and Fireflies aren't in Grok's connector catalogue yet. Their custom MCP connections are expected to work but haven't been verified by xAI.
