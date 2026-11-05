"""Build GTMAI for other AI assistants from the Claude skill (../gtmai).

The Claude version stays the source of truth. For each platform this script:
  1. splits the Claude SKILL.md into one file per stage (references/stages/),
  2. rewrites every Claude-specific instruction for that platform (tool setup, buttons,
     Gamma links, the assistant's name in decks and emails),
  3. writes a lean SKILL.md (rules + stage map) that stays under the strictest size limit (Copilot: 20,000 chars),
  4. adds a manual-mode guide for any tool that won't connect,
  5. zips the skill and writes an install guide.

Run:  python3 build.py            (all platforms)
      python3 build.py chatgpt    (one platform)
"""
import os, re, sys, shutil, zipfile, json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "gtmai")
OUT = os.environ.get("GTMAI_OUT", os.path.join(os.path.dirname(HERE), "dist"))
BUILD = os.path.join(HERE, "_build")
VERSION = "v12"

sys.path.insert(0, HERE)
from platforms import PLATFORMS  # noqa: E402

STAGE_FILES = [  # (heading prefix in the Claude SKILL.md, file name)
    ("## Stage 0", "stage-0-start.md"),
    ("## Stage 1", "stage-1-setup.md"),
    ("## Stage 2", "stage-2-context-center.md"),
    ("## Stage 3", "stage-3-company-search.md"),
    ("## Stage 4", "stage-4-top-5.md"),
    ("## Stage 5", "stage-5-people.md"),
    ("## Stage 6", "stage-6-decks.md"),
    ("## Stage 7", "stage-7-booking-link.md"),
    ("## Stage 8", "stage-8-sequence.md"),
    ("## Stage 9", "stage-9-closing.md"),
]


def split_stages(skill):
    starts = [(skill.index(h), f) for h, f in STAGE_FILES]
    starts.sort()
    out = {}
    for i, (pos, f) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(skill)
        out[f] = skill[pos:end].strip() + "\n"
    return out


def must_replace(text, old, new, where):
    if old not in text:
        raise SystemExit(f"[{where}] expected text not found:\n  {old[:120]}")
    return text.replace(old, new)


def adapt_stage(name, text, P):
    A = P["assistant"]
    if name == "stage-0-start.md":
        start = text.index("**Two kinds of question")
        end = text.index("**Resume:**")
        text = text[:start] + P["questions_block"] + "\n" + text[end:]
        start = text.index("Your first reply has **two parts")
        end = text.index("> 👋 **Welcome to GTMAI.**")
        text = text[:start] + ("Your first reply is the welcome message below, written out word for word as normal chat text, "
                               "ending with the video question and *\"Reply **1** for YES, or **2** for NO.\"* Then stop and wait.\n\n") + text[end:]
        text = must_replace(text, "  > Load your skill or upload the .md file here. For example, if your brief skill is already installed in your Claude, just type / followed by the skill name (/brief.md, /brief, etc.).",
                            "  > Attach your brief.md file here, or paste its text straight into the chat.", name)
        text = must_replace(text, "Buttons (required): **Upload brief.md** · **Ask me questions** · **Pull from my website**",
                            "Options: **1) Upload brief.md** · **2) Ask me questions** · **3) Pull from my website**", name)
        text = must_replace(text, "(an attached file, or a skill's contents loaded into the chat)", "(an attached file, or text pasted into the chat)", name)
        text = text.replace(" with each service as a button,", " with each service as a numbered option,")
    if name == "stage-1-setup.md":
        for tool in ("Gamma", "Apollo.io", "Fireflies"):
            text = must_replace(text, f"In Claude, go to **Customize → Connectors**, search **{tool}**, click **Connect**, and approve.",
                                P["connect"][tool], name)
        text = must_replace(text, "> **Last thing:** in this chat, click **+ → Connectors** and make sure **Apollo.io, Gamma and Fireflies** are switched on, and that **Web search** is on.",
                            "> " + P["last_thing"], name)
        text = must_replace(text, "come back to this chat and type **done** for your next instructions.",
                            "come back to this chat and type **done** for your next instructions. If one of them won't connect, type **done** anyway and I'll switch that tool to manual mode.", name)
        text = must_replace(text, "4. **Apollo, Gamma and web search must be ✅ to continue.** If only Fireflies or the mailbox is ❌, say:",
                            "4. **Any ❌ tool switches to manual mode** (`references/manual-mode.md`): tell the user in one line what changes for them, then continue. If only Fireflies or the mailbox is ❌, say:", name)
        text = text.replace("connected all 3 connectors", "connected all 3 tools")
    if name == "stage-3-company-search.md":
        text = must_replace(text, "Claude builds the search through the Apollo connector,", f"{A} builds the search through the Apollo tool,", name)
        text = text.replace("Buttons (required): **Look-alike company list (Recommended)** · **Full ICP search**",
                            "Options: **1) Look-alike company list (Recommended)** · **2) Full ICP search**")
        text = text.replace("Ask with buttons, with every client inside the question", "Ask, with every client named inside the question")
        text = text.replace("show those first with the same buttons instead of asking the agent", "show those first instead of asking the agent")
        text = text.replace("Ask with buttons, with the count inside the question", "Ask, with the count inside the question")
    if name == "stage-6-decks.md":
        text = must_replace(text, "4 how we found them (Claude + Apollo hub)", f"4 how we found them ({A} + Apollo hub)", name)
        text = must_replace(text, "Claude ✅ · Apollo ✅ ·", f"{A} ✅ · Apollo ✅ ·", name)
        text = must_replace(text, "plus Claude and Apollo (`apollo_organizations_lookup` on claude.ai and apollo.io)",
                            f"plus {A} and Apollo (`apollo_organizations_lookup` on {P['logo_domain']} and apollo.io)", name)
        text = must_replace(text, "(card 4 is always the Claude + Apollo hub diagram)", f"(card 4 is always the {A} + Apollo hub diagram)", name)
        start = text.index("   **On claude.ai the finished deck shows up")
        end = text.index("5. **Share it and get the link.**")
        text = text[:start] + P["gamma_preview"] + "\n" + text[end:]
        text = must_replace(text, "   - **Otherwise (the usual case on claude.ai):**", "   - **Otherwise:**", name)
        text = must_replace(text, "it's the preview above. To get its link: click **Edit in Gamma**, then **Open link**, and copy the address from your browser (it starts with gamma.app/docs/). Paste it here.",
                            P["gamma_get_link"], name)
        text = text.replace("(e.g. `?source=mcp&client=claude`)", "(e.g. `?source=mcp`)")
    return text


def adapt_reference(fname, text, P):
    A = P["assistant"]
    if fname == "gamma-decks.md":
        text = must_replace(text, "| [CLAUDE_LOGO], [APOLLO_LOGO] | one `apollo_organizations_lookup` on claude.ai and apollo.io per campaign |",
                            f"| [AI_LOGO], [APOLLO_LOGO] | one `apollo_organizations_lookup` on {P['logo_domain']} and apollo.io per campaign |", fname)
        text = must_replace(text, "On claude.ai, they only click **Edit in Gamma → Open link** once to copy the deck link (SKILL.md Stage 6b step 5).",
                            "If the Gamma tool doesn't hand you the deck link, they open the deck in Gamma once and copy its link (Stage 6b step 5).", fname)
        text = must_replace(text, "with the Claude logo and the Apollo logo side by side", f"with the {A} logo and the Apollo logo side by side", fname)
        text = must_replace(text, "Claude logo: [CLAUDE_LOGO]", f"{A} logo: [AI_LOGO]", fname)
        text = must_replace(text, "- Square icon logos (Claude, Apollo)", f"- Square icon logos ({A}, Apollo)", fname)
        text = text.replace("You own it · Claude + Apollo run it", f"You own it · {A} + Apollo run it")
        text = text.replace("Sending it through the Gamma connector", "Sending it through the Gamma tool")
    if fname == "sequence.md":
        text = must_replace(text, "- Claude writes it onto each lead's connection task", f"- {A} writes it onto each lead's connection task", fname)
        text = must_replace(text, "Claude told me we should work together.", f"{A} told me we should work together.", fname)
        text = must_replace(text, "Body (Claude's draft,", "Body (your draft,", fname)
        text = must_replace(text, "Apollo and Claude helped me identify", f"Apollo and {A} helped me identify", fname)
        text = text.replace("written by Claude", f"written by {A}").replace("Claude rewrites", f"{A} rewrites").replace("Claude writes each", f"{A} writes each")
    if fname == "brief-template.md":
        text = text.replace("Claude will suggest one", f"{A} will suggest one")
    if fname == "proof-of-work.md":
        text = re.sub(r"\bClaude (writes|drafts)\b", rf"{A} \1", text)
        text = text.replace("a page Claude can fetch", "a page you can fetch").replace("Claude's web search", "your web search")
        text = text.replace("Built with Claude + Apollo in [actual time]", f"Built with {A} + Apollo in [actual time]")
        text = text.replace("'Claude web search on [date]", f"'{A} web search on [date]")
        text = text.replace("The claude.ai fetch tool may refuse a URL it built", "Your fetch tool may refuse a URL you built")
        text = text.replace("claude.ai fetch only opens URLs that appeared", "Some fetch tools only open URLs that appeared")
        text = re.sub(r"\bClaude can\b", "you can", text)
        text = re.sub(r"\bClaude usually can't\b", "you usually can't", text)
    text = text.replace("SKILL.md Stage", "Stage")
    return text


LEFTOVER_OK = [  # Claude mentions that are about Zack's own service, not the assistant running the skill
    "Claude + Apollo training", "built with Claude and Apollo", "Claude + Apollo run it",
]


def check_leftovers(path, text):
    hits = []
    for m in re.finditer(r"claude", text, re.I):
        ctx = text[max(0, m.start() - 40): m.end() + 40].replace("\n", " ")
        if not any(ok.lower() in ctx.lower() for ok in LEFTOVER_OK):
            hits.append(ctx)
    return hits


def build(key):
    P = PLATFORMS[key]
    skill = open(os.path.join(SRC, "SKILL.md")).read()
    stages = split_stages(skill)
    d = os.path.join(BUILD, key, "gtmai")
    shutil.rmtree(os.path.join(BUILD, key), ignore_errors=True)
    os.makedirs(os.path.join(d, "references", "stages"))
    for f, t in stages.items():
        open(os.path.join(d, "references", "stages", f), "w").write(adapt_stage(f, t, P))
    for f in sorted(os.listdir(os.path.join(SRC, "references"))):
        if f.endswith(".md"):
            t = open(os.path.join(SRC, "references", f)).read()
            open(os.path.join(d, "references", f), "w").write(adapt_reference(f, t, P))
    open(os.path.join(d, "references", "manual-mode.md"), "w").write(open(os.path.join(HERE, "manual-mode.md")).read().replace("{A}", P["assistant"]))
    core = open(os.path.join(HERE, "core-skill.md")).read()
    for k, v in P["core"].items():
        core = core.replace("{{" + k + "}}", v)
    core = core.replace("{A}", P["assistant"]).replace("{VERSION}", VERSION)
    assert "{{" not in core, re.findall(r"\{\{\w+\}\}", core)
    open(os.path.join(d, "SKILL.md"), "w").write(core)
    # checks
    desc = re.search(r"^description: (.*)$", core, re.M).group(1)
    report = {"platform": P["label"], "skill_md_chars": len(core), "description_chars": len(desc)}
    assert len(desc) <= 1024, f"{key}: description {len(desc)} > 1024"
    assert len(core) <= P.get("skill_md_limit", 10**9), f"{key}: SKILL.md {len(core)} chars > {P['skill_md_limit']}"
    leftovers = {}
    for root, _, files in os.walk(d):
        for f in files:
            p = os.path.join(root, f); hits = check_leftovers(p, open(p).read())
            if hits: leftovers[os.path.relpath(p, d)] = hits
    report["claude_leftovers"] = leftovers
    # extras (e.g. one merged file for platforms that may not load reference files on demand)
    if P.get("all_in_one"):
        parts = [core]
        for sub in ("stages",):
            for f in sorted(os.listdir(os.path.join(d, "references", sub))):
                parts.append(f"\n\n<!-- ===== references/{sub}/{f} ===== -->\n\n" + open(os.path.join(d, "references", sub, f)).read())
        for f in sorted(os.listdir(os.path.join(d, "references"))):
            if f.endswith(".md"):
                parts.append(f"\n\n<!-- ===== references/{f} ===== -->\n\n" + open(os.path.join(d, "references", f)).read())
        open(os.path.join(BUILD, key, "GTMAI-all-in-one.md"), "w").write("".join(parts))
    # package
    os.makedirs(OUT, exist_ok=True)
    zname = os.path.join(OUT, f"GTMAI for {P['label']}.zip")
    with zipfile.ZipFile(zname, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(d):
            for f in sorted(files):
                if f.startswith("."): continue
                p = os.path.join(root, f)
                arc = os.path.relpath(p, d) if P.get("zip_root") == "flat" else os.path.join("gtmai", os.path.relpath(p, d))
                z.write(p, arc)
    install = open(os.path.join(HERE, "install", f"{key}.md")).read().replace("{VERSION}", VERSION)
    open(os.path.join(OUT, f"GTMAI for {P['label']} - INSTALL.md"), "w").write(install)
    if P.get("all_in_one"):
        shutil.copy(os.path.join(BUILD, key, "GTMAI-all-in-one.md"), os.path.join(OUT, f"GTMAI for {P['label']} - all-in-one.md"))
        shutil.copy(os.path.join(BUILD, key, "GTMAI-all-in-one.md"), os.path.join(OUT, f"gtmai-{key}-all-in-one.md"))
    if P.get("plugin_package"):
        # skills-only plugin layout for OpenAI's Plugin Directory (the portal converts a Claude-style manifest)
        manifest = {"name": "gtmai", "version": "12.0.0",
                    "description": "GTMAI by Zack Deris: find best-fit companies in Apollo, build a personalised Gamma deck for each, and launch a ready-to-go outbound sequence, all in one chat.",
                    "author": {"name": "Zack Deris", "url": "https://zackderis.com"}, "homepage": "https://zackderis.com/gtmai"}
        pname = os.path.join(OUT, f"GTMAI {P['label']} plugin (for OpenAI submission).zip")
        with zipfile.ZipFile(pname, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr(".claude-plugin/plugin.json", json.dumps(manifest, indent=2))
            for root, _, files in os.walk(d):
                for f in sorted(files):
                    if f.startswith("."): continue
                    p = os.path.join(root, f)
                    z.write(p, os.path.join("skills", "gtmai", os.path.relpath(p, d)))
        report["plugin_zip"] = pname
    shutil.copy(zname, os.path.join(OUT, f"gtmai-{key}.zip"))  # short name used for release assets and the website
    report["zip"] = zname; report["zip_kb"] = round(os.path.getsize(zname) / 1024)
    with zipfile.ZipFile(zname) as z:
        report["files"] = len(z.namelist())
    return report


def build_claude():
    """Zip the Claude skill itself (dist/gtmai.zip)."""
    os.makedirs(OUT, exist_ok=True)
    zname = os.path.join(OUT, "gtmai.zip")
    with zipfile.ZipFile(zname, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(SRC):
            for f in sorted(files):
                if f.startswith("."): continue
                p = os.path.join(root, f)
                z.write(p, os.path.join("gtmai", os.path.relpath(p, SRC)))
    return {"platform": "claude", "zip": zname, "zip_kb": round(os.path.getsize(zname) / 1024)}


if __name__ == "__main__":
    keys = sys.argv[1:] or ["claude"] + list(PLATFORMS)
    if "claude" in keys:
        keys.remove("claude")
        print(json.dumps(build_claude(), indent=1))
    for k in keys:
        r = build(k)
        print(json.dumps(r, indent=1, ensure_ascii=False))
