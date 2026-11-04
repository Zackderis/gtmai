# Platform research behind build.py (2 Nov 2026)

## ChatGPT
Custom GPTs retire 11 Dec 2026. The replacement is **plugins**, which bundle skills and apps.
- Skills use the SKILL.md format: Plugins → Skills → Create → Upload. Officially for Business, Enterprise, Healthcare and Edu.
- Apollo.io, Gamma and Fireflies are official plugins.
- Plugin submission accepts a Claude-style plugin, with the skill at `skills/gtmai/SKILL.md`. Remove Claude references and app references.
- No answer-button widget.

Sources:
- help.openai.com/en/articles/20001066-skills-in-chatgpt
- help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq
- developers.openai.com/plugins/guides/submit-claude-plugin.md
- openai.com/business/plugins/apollo/, /gamma/, /fireflies/

## Gemini
Skills launched 30 Sep 2026 and replace Gems.
- Upload SKILL.md on its own, or as a folder or zip. Description at most 1,024 characters; 100 MB maximum.
- Personal accounts only for now.
- Custom apps (MCP) live under Settings → Connected Apps → Custom apps. US, personal account, English only.
- MCP URLs: Apollo `https://mcp.apollo.io/mcp`, Gamma `https://mcp.gamma.app/mcp`, Fireflies `https://api.fireflies.ai/mcp`.

Sources:
- blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/
- support.google.com/gemini/answer/17094296
- support.google.com/gemini/answer/17209137

## Grok
- grok.com Skills launched 18 May 2026. No published format; reported uploads are zip, .skill or .md.
- Grok Bot is xAI's own agent product and saves skills on request.
- Connectors: grok.com/connectors → New Connector → Custom (MCP URL). Gamma is a built-in connector.

Sources:
- x.ai/news/grok-skills
- docs.x.ai/grok-bot/skills-routines-and-automations
- docs.x.ai/grok/connectors
- gamma.app/integrations/grok

## Microsoft 365 Copilot
Agent Builder → Skills → Add (zip).
- SKILL.md under 20,000 characters; zip 50 MB; 25 MB per file; 350 files; folders at most 3 levels deep.
- MCP tools only through Copilot Studio (Tools → New tool → Model Context Protocol, OAuth dynamic discovery).
- Gamma is in the Microsoft 365 Agent Store.
- GitHub Copilot reads SKILL.md natively (`~/.copilot/skills/`).

Sources:
- learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-skills
- learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
- gamma.app/integrations/microsoft-copilot
