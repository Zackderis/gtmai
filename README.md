# GTMAI by Zack Deris

A guided AI go-to-market workflow that runs in one chat. GTMAI uses **Apollo**, **Gamma** and **Fireflies** to:

- learn your business from your website
- find look-alikes of your best clients in Apollo and pick the top 5
- find verified decision-makers
- build a personalised Gamma deck for each company
- write the emails and load a 4-step Apollo sequence (created **inactive**: nothing sends until you activate it)
- turn every sales call recorded in Fireflies into a closing deck and email

**Landing page:** https://zackderis.com/gtmai
**Step-by-step guide (with screenshots):** https://zackderis.notion.site/gtm

## Download

Get the zip for your AI from the [latest release](../../releases/latest):

| AI | File | Install |
|---|---|---|
| **Claude** (recommended) | `gtmai.zip` | Steps 1–6 of the [guide](https://zackderis.notion.site/gtm), then type `start GTMAI` |
| ChatGPT | `gtmai-chatgpt.zip` | [install/chatgpt.md](platforms/install/chatgpt.md) |
| Gemini | `gtmai-gemini.zip` | [install/gemini.md](platforms/install/gemini.md) |
| Grok | `gtmai-grok.zip` | [install/grok.md](platforms/install/grok.md) |
| Microsoft 365 Copilot | `gtmai-copilot.zip` | [install/copilot.md](platforms/install/copilot.md) |

You need a paid plan for your AI, plus accounts for Apollo, Gamma and Fireflies:

- Apollo: https://get.apollo.io/zack
- Gamma: https://gamma.app/?utm_campaign=prompt&utm_content=Zack+Deris&utm_source=LinkedIn
- Fireflies: https://fireflies.ai/?fpr=zdts

If a tool won't connect, GTMAI switches to manual mode and keeps going.

## What's in this repo

```
gtmai/                 The Claude skill: the source of truth
  SKILL.md             Rules and all 10 stages
  references/          Apollo, Gamma, sequence, ranking and deck-recipe guides
platforms/
  build.py             Builds every other platform's version from gtmai/
  platforms.py         Per-platform rewrites (tool setup, buttons, names)
  core-skill.md        The lean SKILL.md used on other platforms
  manual-mode.md       Fallback when a tool isn't connected
  install/             Install guide for each platform
```

## Building

Edit the Claude skill in `gtmai/`, then run:

```bash
python3 platforms/build.py
```

That writes every zip, install guide and all-in-one file to `dist/` (ignored by git). Build a single platform with `python3 platforms/build.py chatgpt`. Upload the zips from `dist/` to a new GitHub Release.

## License

Free to use for your own business and your clients; not for resale or redistribution. See [LICENSE](LICENSE).
