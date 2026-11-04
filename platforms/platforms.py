"""Per-platform settings for build.py. Research notes (2 Nov 2026) are in ./RESEARCH.md."""

WRITTEN_QUESTIONS = (
    "**How to ask (hard rule).** This chat has no answer-button widget, so use **written options** everywhere: "
    "write the content out in full as normal chat text, then end the same message with the choices as a short numbered list "
    "(*\"Reply **1** to save it, **2** to change something\"*). Accept a number, the option's words, or a free-text answer. "
    "Wherever a stage file says \"Buttons\" or \"Options\", show those choices as that numbered list.\n"
    "- **One approval per reply.** Finish one step (e.g. saving the Context Center), say in text what happened (*\"✅ Saved: …\"*), "
    "then show the next thing to approve. Never chain two questions into one reply.\n"
)

CORE_QUESTIONS = (
    "- {A} has no answer-button widget here, so **always use written options**: write the content in full as normal chat text, "
    "then end the same message with a short numbered list (*\"Reply **1** to save it, **2** to change something\"*). "
    "Accept a number, the option's words, or a free-text answer. Where a stage file says \"Buttons\" or \"Options\", use this numbered list."
)

GAMMA_RETURNS_LINK = (
    "   **When Gamma finishes:** check the generation status about every 30–60 seconds until it's **completed**, then read the deck back. "
    "Use the `gamma.app/docs/…` link the Gamma tool returns. Never share a `/generations/` link or an unfinished deck. "
    "If your read-back finds fixes, send them in one edit and say what you changed.\n"
)

GAMMA_GET_LINK = (
    "the Gamma tool didn't hand me its link. Open your Gamma dashboard, open the deck, and copy the address from your browser "
    "(it starts with gamma.app/docs/). Paste it here."
)

PLATFORMS = {
    "chatgpt": {
        "label": "ChatGPT",
        "assistant": "ChatGPT",
        "logo_domain": "openai.com",
        "zip_root": "flat",
        "plugin_package": True,
        "connect": {
            "Gamma": "In ChatGPT, open **Plugins** in the sidebar, search **Gamma**, click **Install plugin → Connect**, and approve.",
            "Apollo.io": "In ChatGPT, open **Plugins** in the sidebar, search **Apollo.io**, click **Install plugin → Connect**, and approve.",
            "Fireflies": "In ChatGPT, open **Plugins** in the sidebar, search **Fireflies**, click **Install plugin → Connect**, and approve.",
        },
        "last_thing": "**Last thing:** run GTMAI in a **Work** chat if your plan has it, and make sure web search is allowed. When ChatGPT asks you to approve an Apollo or Gamma action, check it and approve it.",
        "questions_block": WRITTEN_QUESTIONS,
        "gamma_preview": GAMMA_RETURNS_LINK,
        "gamma_get_link": GAMMA_GET_LINK,
        "core": {
            "platform_label": "ChatGPT",
            "description": (
                "GTMAI by Zack Deris: a guided AI go-to-market workflow run in one chat with the Apollo.io, Gamma and Fireflies plugins. "
                "Use when the user says \"GTMAI\", \"start GTMAI\", \"run GTMAI\" or \"continue GTMAI\", pastes a GTMAI Campaign card, replies "
                "\"done\" during a GTMAI campaign, or asks to run Zack Deris's Apollo + Gamma + Fireflies outbound workflow. It sets up the 3 tools, "
                "finds best-fit companies in Apollo, picks the top 5, finds verified decision-makers, builds a personalised Gamma deck per company, "
                "and builds a 4-step Apollo sequence (LinkedIn connect, LinkedIn engage, Email 1 with 5 perfect-fit companies, Email 2 with the deck "
                "4 hours later). After each sales call it turns the Fireflies recording into a closing deck and email."
            ),
            "tools_block": (
                "- **Apollo.io, Gamma and Fireflies** are official ChatGPT plugins. Use their tools directly. If one isn't available, ask the user to "
                "install and connect it from **Plugins**, or to @-mention it (e.g. `@Apollo.io`) in their next message.\n"
                "- The reference files name Apollo tools as they appear in Apollo's MCP server (e.g. `apollo_mixed_people_api_search`). The plugin's "
                "tool names can differ slightly: use whichever Apollo tool does the described action.\n"
                "- **Web search** is used for company research. **Work** mode suits long campaigns best."
            ),
            "confirm_note": "   - ChatGPT may show its own approval prompt before Apollo or Gamma actions. That's expected: tell the user to check what it says and approve it.",
            "failure_fixes": (
                "   - **A tool isn't available in this chat:** ask the user to install or connect it from **Plugins** (search its name), or to @-mention it, then type **done**.\n"
                "   - **A login or permission error:** reconnect it from **Plugins → [tool] → Connect**."
            ),
            "questions_core": CORE_QUESTIONS,
        },
    },
    "grok": {
        "label": "Grok",
        "assistant": "Grok",
        "logo_domain": "x.ai",
        "zip_root": "flat",
        "all_in_one": True,
        "connect": {
            "Gamma": "In Grok, open **[grok.com/connectors](https://grok.com/connectors)**, find **Gamma**, click **Connect**, and approve.",
            "Apollo.io": "In Grok, open **[grok.com/connectors](https://grok.com/connectors)** → **New Connector** → **Custom**. Name it **Apollo.io**, paste `https://mcp.apollo.io/mcp`, save, and sign in to Apollo when asked.",
            "Fireflies": "In Grok, open **[grok.com/connectors](https://grok.com/connectors)** → **New Connector** → **Custom**. Name it **Fireflies**, paste `https://api.fireflies.ai/mcp`, save, and sign in to Fireflies when asked.",
        },
        "last_thing": "**Last thing:** in this chat, make sure the **Apollo.io, Gamma and Fireflies** connectors are turned on, and that web search is on.",
        "questions_block": WRITTEN_QUESTIONS,
        "gamma_preview": GAMMA_RETURNS_LINK,
        "gamma_get_link": GAMMA_GET_LINK,
        "core": {
            "platform_label": "Grok",
            "description": (
                "GTMAI by Zack Deris: a guided AI go-to-market workflow run in one Grok chat with the Apollo.io, Gamma and Fireflies connectors. "
                "Use when the user says \"GTMAI\", \"start GTMAI\", \"run GTMAI\" or \"continue GTMAI\", pastes a GTMAI Campaign card, replies "
                "\"done\" during a GTMAI campaign, or asks to run Zack Deris's Apollo + Gamma + Fireflies outbound workflow. It sets up the 3 tools, "
                "finds best-fit companies in Apollo, picks the top 5, finds verified decision-makers, builds a personalised Gamma deck per company, "
                "and builds a 4-step Apollo sequence (LinkedIn connect, LinkedIn engage, Email 1 with 5 perfect-fit companies, Email 2 with the deck "
                "4 hours later). After each sales call it turns the Fireflies recording into a closing deck and email."
            ),
            "tools_block": (
                "- **Gamma** is a built-in Grok connector. **Apollo.io** and **Fireflies** are added as custom connectors (their MCP servers). Use their tools directly.\n"
                "- The reference files name Apollo tools as they appear in Apollo's MCP server (e.g. `apollo_mixed_people_api_search`); use whichever Apollo tool does the described action.\n"
                "- **Web search** is used for company research.\n"
                "- If your environment can't open files under `references/` when a stage starts, ask the user to attach that file (or the all-in-one GTMAI file) to the chat."
            ),
            "confirm_note": "",
            "failure_fixes": (
                "   - **A connector's tools aren't available in this chat:** ask the user to check it's added and turned on at **grok.com/connectors**, then type **done**.\n"
                "   - **A login or permission error:** remove and re-add the connector at **grok.com/connectors**, signing in again."
            ),
            "questions_core": CORE_QUESTIONS,
        },
    },
    "gemini": {
        "label": "Gemini",
        "assistant": "Gemini",
        "logo_domain": "gemini.google.com",
        "zip_root": "flat",
        "connect": {
            "Gamma": "In Gemini (on the web), go to **Settings → Connected Apps → Custom apps → Add a custom app**, paste `https://mcp.gamma.app/mcp`, and sign in to Gamma.",
            "Apollo.io": "In Gemini (on the web), go to **Settings → Connected Apps → Custom apps → Add a custom app**, paste `https://mcp.apollo.io/mcp`, and sign in to Apollo.",
            "Fireflies": "In Gemini (on the web), go to **Settings → Connected Apps → Custom apps → Add a custom app**, paste `https://api.fireflies.ai/mcp`, and sign in to Fireflies.",
        },
        "last_thing": "**Last thing:** custom apps currently need a personal Google account in the US. If you can't add them, that's fine: type **done** and I'll run that tool in manual mode. When a step needs a tool, I may ask you to start your reply with **@Apollo**, **@Gamma** or **@Fireflies**.",
        "questions_block": WRITTEN_QUESTIONS,
        "gamma_preview": GAMMA_RETURNS_LINK,
        "gamma_get_link": GAMMA_GET_LINK,
        "core": {
            "platform_label": "Gemini",
            "description": (
                "GTMAI by Zack Deris: a guided AI go-to-market workflow run in one Gemini chat with Apollo.io, Gamma and Fireflies (as connected apps, "
                "or in manual mode). Use when the user says \"GTMAI\", \"start GTMAI\", \"run GTMAI\" or \"continue GTMAI\", pastes a GTMAI Campaign "
                "card, replies \"done\" during a GTMAI campaign, or asks to run Zack Deris's Apollo + Gamma + Fireflies outbound workflow. It sets up "
                "the 3 tools, finds best-fit companies in Apollo, picks the top 5, finds verified decision-makers, builds a personalised Gamma deck per "
                "company, and builds a 4-step Apollo sequence (LinkedIn connect, LinkedIn engage, Email 1 with 5 perfect-fit companies, Email 2 with the "
                "deck 4 hours later). After each sales call it turns the Fireflies recording into a closing deck and email."
            ),
            "tools_block": (
                "- **Apollo.io, Gamma and Fireflies** connect to Gemini as **custom apps** (their MCP servers). Call their tools when a step needs them. "
                "If a tool isn't being picked up, ask the user to start their next message with **@Apollo**, **@Gamma** or **@Fireflies**.\n"
                "- Gemini asks the user to confirm actions that change things (saving contacts, creating a sequence, building a deck). Tell them to expect it.\n"
                "- The reference files name Apollo tools as they appear in Apollo's MCP server (e.g. `apollo_mixed_people_api_search`); use whichever Apollo tool does the described action.\n"
                "- Custom apps need a personal US Google account today. Anyone else runs the tools in manual mode."
            ),
            "confirm_note": "   - Gemini also shows its own confirmation before write actions. That's expected: tell the user to check it and confirm.",
            "failure_fixes": (
                "   - **A tool isn't available in this chat:** ask the user to add it under **Settings → Connected Apps → Custom apps**, or to @-mention it, then type **done**. If they can't add custom apps, use manual mode.\n"
                "   - **A login or permission error:** remove and re-add the custom app, signing in again."
            ),
            "questions_core": CORE_QUESTIONS,
        },
    },
    "copilot": {
        "label": "Microsoft 365 Copilot",
        "assistant": "Copilot",
        "logo_domain": "microsoft.com",
        "zip_root": "flat",
        "skill_md_limit": 20000,
        "all_in_one": True,
        "connect": {
            "Gamma": "In Microsoft 365 Copilot, open the **Agent Store**, search **Gamma**, and add it (your IT admin may need to approve it).",
            "Apollo.io": "In **Copilot Studio**, open your GTMAI agent → **Tools → Add a tool → New tool → Model Context Protocol**. Paste `https://mcp.apollo.io/mcp`, choose **OAuth 2.0 (Dynamic discovery)**, and sign in to Apollo. No Copilot Studio access? Skip this: I'll run Apollo in manual mode.",
            "Fireflies": "In **Copilot Studio**, open your GTMAI agent → **Tools → Add a tool → New tool → Model Context Protocol**. Paste `https://api.fireflies.ai/mcp`, choose **OAuth 2.0 (Dynamic discovery)**, and sign in to Fireflies. No Copilot Studio access? Skip this: you'll paste call transcripts instead.",
        },
        "last_thing": "**Last thing:** chat with your **GTMAI agent** (not the default Copilot chat) so these tools and this workflow are switched on.",
        "questions_block": WRITTEN_QUESTIONS,
        "gamma_preview": GAMMA_RETURNS_LINK,
        "gamma_get_link": GAMMA_GET_LINK,
        "core": {
            "platform_label": "Microsoft 365 Copilot",
            "description": (
                "GTMAI by Zack Deris: a guided AI go-to-market workflow run in one Copilot chat with Apollo.io, Gamma and Fireflies (connected tools, "
                "or manual mode). Use when the user says \"GTMAI\", \"start GTMAI\", \"run GTMAI\" or \"continue GTMAI\", pastes a GTMAI Campaign "
                "card, replies \"done\" during a GTMAI campaign, or asks to run Zack Deris's Apollo + Gamma + Fireflies outbound workflow. It finds "
                "best-fit companies in Apollo, picks the top 5, finds verified decision-makers, builds a personalised Gamma deck per company, and "
                "builds a 4-step Apollo sequence (LinkedIn connect, LinkedIn engage, Email 1 with 5 perfect-fit companies, Email 2 with the deck "
                "4 hours later). After each sales call it turns the Fireflies recording into a closing deck and email."
            ),
            "tools_block": (
                "- **Gamma** comes from the Microsoft 365 Agent Store (@Gamma). **Apollo.io** and **Fireflies** are MCP tools added to this agent in Copilot Studio. "
                "Many workplaces won't have Copilot Studio: then Apollo and Fireflies run in **manual mode**, and the campaign still works.\n"
                "- The reference files name Apollo tools as they appear in Apollo's MCP server (e.g. `apollo_mixed_people_api_search`); use whichever Apollo tool does the described action.\n"
                "- **Web search** (web grounding) is used for company research."
            ),
            "confirm_note": "",
            "failure_fixes": (
                "   - **A tool isn't available in this chat:** check the user is chatting with the GTMAI agent, and that the tool is added (Gamma from the Agent Store; Apollo and Fireflies in Copilot Studio). If they can't add it, use manual mode.\n"
                "   - **A login or permission error:** ask them to sign in to that tool again from the agent's tool settings, or ask their IT admin."
            ),
            "questions_core": CORE_QUESTIONS,
        },
    },
}
