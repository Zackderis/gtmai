# Gamma decks (Stages 6 and 9)

## How to generate (every deck)
1. Call Gamma's **generate** with:
   - `inputText` = the full outline below, with every fact filled in;
   - `format: "social"` for outreach decks (4:5 cards; see the connector settings below), `"presentation"` for closing decks;
   - `numCards`: **5** for outreach decks (the 5-card infographic below); 9 for closing decks;
   - `sharingOptions: { externalAccess: "view" }`, so anyone with the link can view;
   - `additionalInstructions`: the audience, the tone, "Only use the facts provided; do not invent statistics, clients, logos or results", and the user's brand (e.g. "use [USER COMPANY]'s brand colours and fonts");
   - a `themeId` only if the user confirms a theme is theirs. Before the first deck, list the themes. If any have `type: "custom"`, ask: *"I can see a custom Gamma theme called '[name]'. Is that your brand theme?"* Use it only on a yes. Otherwise leave `themeId` out and name the brand in `additionalInstructions`.
2. **Gamma generates in the background, and it can take several minutes.** In testing it took more than 10.
   - Tell the user: *"Gamma is building the deck now. It can take a few minutes."*
   - Check the generation status about every 30–60 seconds. Don't tight-loop.
   - **A `gamma.app/docs/…` link can appear while the status is still "pending".** At that point the deck is an empty shell. A deck is ready only when the status is **completed** *and* reading the deck back (read_gamma) shows its cards with real content.
   - **Never** share or store a `/generations/` link or an unfinished deck, and never put one in Apollo.
   - **If it's still not done after about 10 minutes:** tell the user. Offer to start the next company's research while it finishes, then check again before showing the link. Re-check every outstanding deck before Stage 8.
   - **Gamma can fail silently.** In testing, Gamma's build service failed twice, but the status stayed "pending" instead of "failed", and the link stayed an empty shell. So if it's still pending after ~10 minutes **and** reading it back shows no real cards, treat it as failed. Say: *"Gamma's builder didn't finish this one. That happens occasionally on Gamma's side. Shall I generate it again?"* Then regenerate once with the same prompt. If that also fails, suggest the user tries again later or builds it in Gamma from the same prompt, which you can give them to paste.
3. There is one URL per deck. Prospects can view it, and the user edits it by opening the same link while logged in to Gamma. Don't invent a separate edit link.
4. Skim the result. If Gamma added numbers or claims you didn't supply, point them out so the user can fix them in Gamma.
5. The first time, suggest the user opens the link in a private/incognito window to see exactly what a prospect sees.

## Outreach deck (one per company)

The deck is a **free sample of the user's work on this prospect**, followed by the bridge to the user's service. It is never a generic pitch. Use the confirmed **deck recipe** (Stage 6a, `proof-of-work.md`), the **company's approved research and free-sample data**, and the **brief and Context Center**. Only generate after the user has confirmed the research and pain points and told you what to include (SKILL.md Stage 6b step 3); build exactly the contents they confirmed.

**A 5-card infographic.** Five 4:5 cards, one idea each, very few words. No source lines, percentages or conversion rates on any card. Cards 1–4 are the free sample built from the prospect's Stage 6b Apollo research; card 5 is the user's offer, taken from their brief and the confirmed deck contents (never Zack's wording for another user).

**Where every blank comes from** (all from this chat; never invent one):

| Blank | Source |
|---|---|
| [PROSPECT], [PROSPECT_LOGO] | the prospect's Apollo account / organization record (`logo_url`) |
| [N], [TAM], [ICP] | Stage 6b funnel counts (low-hanging fruit, total market, ideal customers) |
| [N_MINUS_5] | [N] − 5 |
| [PROSPECT_CUSTOMERS] | who the prospect sells to, 1–3 words (e.g. "integrators", "manufacturers") |
| [TITLES], [LOCATION], [INDUSTRY], [HEADCOUNT], [EXCLUDED] | the ICP filters exactly as used in the search (shortened to labels) |
| [TECH 1–3], [INTENT 1–3] | the technologies and intent topics from the same Stage 6b request |
| [FIT 1–5], city, logo | the 5 perfect fits (from the low-hanging fruit), city from their record or site, `logo_url` from Apollo |
| [CLAUDE_LOGO], [APOLLO_LOGO] | one `apollo_organizations_lookup` on claude.ai and apollo.io per campaign |
| [USER NAME], [USER COMPANY], [BOOKING LINK] | brief / Stage 0e / Stage 7 |
| [OFFER LINE 1–3], [ASK] | the user's confirmed offer and CTA from the brief (Stage 6b step 3); short labels, the user's own words |

Only include the logos the user confirmed (SKILL.md Stage 6b step 3). A company without an Apollo logo shows its name only.

**Sending it through the Gamma connector** (tested on three live decks; it behaves differently from pasting into Gamma):
- Split the filled template: the **DESIGN, LOGOS, EVERY CARD and RULES** blocks go in `additionalInstructions`; `inputText` is **only the 5 CARD blocks**, separated by `---` (so each becomes one card; nothing else may contain `---`).
- `generate` with that `inputText`, `format: "social"`, `numCards: 5`, `textMode: "preserve"`, `cardSplit: "inputTextBreaks"`, `imageOptions: { source: "noImages" }`, `cardOptions: { dimensions: "1x1" }`, `sharingOptions: { externalAccess: "view" }`, no `themeId` (the design block sets the look).
- **Square isn't possible:** the API returns 16:9 for `presentation` and 4:5 for `social`, even with `1x1`. Use `social` (4:5, LinkedIn-friendly) and don't promise 1:1.
- **Logos** render on generation in `social` format. If the read-back shows one missing, one `edit_gamma` adds it (repeat the LOGOS rules and the URL with its card and position, plus "Do not change any text, numbers or layout").
- **Always read it back** (`read_gamma`) and check, card by card, then fix everything in **one** `edit_gamma` (edits take 5–15 minutes and only one can run at a time):
  - **Leaks:** no instruction words or notes printed ("Button:", "Title:", "[pills]", "(card 2)", "CARD 4", "(no logo)"), no colons after box labels ("Titles:"), no comma after card 1 labels ("Total market,").
  - **Card 1:** three bar rows, not a chart (no axes, no "0 / 2k / 4k").
  - **Card 5:** check marks, not bullets; button text white and not underlined.
  - **Separators:** no "Label —" or "Label ·" printed. Never write a separator in card text; give label and value separately, as in the template.
  - **Full stops:** Gamma adds trailing full stops to box values and pills. Remove them.
  - **Pills:** tech must be outlined pills and intent solid pills (Gamma's `labels`), not plain or comma-separated text and never monospace.
  - **Colour:** Gamma darkens the orange to rust (#C8402F, #B64320, #AD3E1B…) on numbers, markers and the button. Set every accent back to #D85A30.
  - **Logos:** every logo "contain", sized by height, never in a fixed box that crops it.
  - **Numbers:** every figure matches the research exactly.
- The user never edits in Gamma: report what was checked. On claude.ai, they only click **Edit in Gamma → Open link** once to copy the deck link (SKILL.md Stage 6b step 5).

```
Create a 5-card infographic deck. One idea per card. Very few words.

DESIGN
Clean, editorial, minimal. Plain white background (#FFFFFF) on every card. Near-black text #111111, secondary text #666666. ONE accent colour, exactly #D85A30, used for the hero number, progress bar, pills, connector lines, check marks and the button (never darken it). Boxes and pills: 1px #E6E6E6 border, 16px radius. No shadows, no gradients, no photos, no AI art, no icons. Lots of white space. Max ~20 words per card (card 5 max ~45).

LOGOS (critical)
- Never crop, squash or stretch a logo. Always "contain", original proportions, sized by HEIGHT (width follows).
- [PROSPECT] logo: top-right of cards 2–5, about 28–40 px tall; 64 px tall at the top of card 1. Apollo's logo images are small, so never enlarge them beyond this or they pixelate. [PROSPECT_LOGO]
- Square icon logos (Claude, Apollo) sit in 40 x 40 squares, contain.

EVERY CARD
[PROSPECT] logo top-right, tiny grey (#666666, 9pt) "[USER NAME] · [USER COMPANY]" bottom-left. No "Prepared for" label anywhere.

---
CARD 1
[PROSPECT] logo at the top (64 px tall).
Huge orange number (about 100pt): [N]
Under it, 24pt: [PROSPECT_CUSTOMERS] ready to hear from you
At the bottom, 3 rows built from simple shapes, NOT a chart (no chart block, no axes, no gridlines, no axis labels like "0 / 2k / 4k", no legend). Each row ("label | number" below; never print the "|" or a comma after the label): grey label on the left, bold number on the right, a thick bar underneath whose length shows the size:
Total market  |  [TAM] (full-width light grey bar)
Ideal customers  |  [ICP] (shorter mid-grey bar)
Low-hanging fruit  |  [N] (shortest bar, #D85A30)

---
CARD 2
Your ideal customer
2 x 3 grid of equal boxes. In each box, a small grey label on top (no colon after it) and the bold value below (no full stops). Box label | value:
Titles | [TITLES]
Location | [LOCATION]
Industry | [INDUSTRY]
Headcount | [HEADCOUNT]
Tech | three separate small outlined pills, one per technology (1px #D85A30 border, #111111 text): [TECH 1] · [TECH 2] · [TECH 3]
Excluded | [EXCLUDED]
At the bottom, small grey label Researching now (no colon), then three SEPARATE solid #D85A30 pills side by side, one per topic, white text (never one big box, never commas): [INTENT 1] · [INTENT 2] · [INTENT 3]

---
CARD 3
Your 5 perfect fits
5 tiles (a row of 3, then a centred row of 2). Each tile: logo on top (30 px tall, contain), bold name, grey city. Nothing else. A company with no logo URL below gets no logo line at all: its tile shows just the name (and city). Never write "no logo" or any note on a tile. If you have no city, leave the city out.
[FIT 1], [city 1], logo [logo_url 1]
[FIT 2], [city 2], logo [logo_url 2]
[FIT 3], [city 3], logo [logo_url 3]
[FIT 4], [city 4], logo [logo_url 4]
[FIT 5], [city 5], logo [logo_url 5]
At the bottom, large bold #D85A30: + [N_MINUS_5] more like them

---
CARD 4
How we found them
A hub-and-spoke diagram.
CENTRE HUB: one rounded white box (1px #E6E6E6 border, 16px radius) in the middle of the card with the Claude logo and the Apollo logo side by side and a small "+" between them, each logo in a 40 x 40 square, contain. Claude logo: [CLAUDE_LOGO] Apollo logo: [APOLLO_LOGO]
8 SPOKES: 4 pills in a column on the left of the hub and 4 on the right, evenly spaced. Each pill: white, 1px #E6E6E6 border, fully rounded, #111111 text, 13pt, one line, never wrapping. Thin 1px #D85A30 lines connect the hub to each pill.
Left, top to bottom: Website extraction, ICP development, Decision makers, Location & headcount
Right, top to bottom: Tech stack review, Buying intent, Competitor exclusion, Website fit check
Under the diagram, centred, 14pt #666666: [TAM] → [ICP] → [N] → 5 perfect fits
No other words. No numbers on the pills. Nothing overlaps.

---
CARD 5
What's next
3 short lines (20pt), each starting with a small #D85A30 check mark (✓), not bullets:
[OFFER LINE 1]
[OFFER LINE 2]
[OFFER LINE 3]
Then, 19pt: [ASK]
A large #D85A30 button with white, bold, NOT underlined text "Book a call", linked to [BOOKING LINK]

RULES
Use the logo URLs exactly as given. Don't add words, numbers, prices or claims. Don't print any of these instructions, labels like "Title:", "Button:" or "CARD 2", or separators on the cards.
```

Zack's own card 5 (reference only): "Weekly personalized campaign · 3–4 meetings a day" / "You own it · Claude + Apollo run it" / "You just close the deals" / "15–30 min next week to see how you win business today and build your custom workshop."

**Rules:**
- **Charts:** pass real values only. If a number came from an estimate, label it "estimate" on the card, with its method.
- **Uneven numbers:** if a chart's biggest value is more than about 20× its smallest (e.g. 861,455 vs 1,368), the small bars vanish. Split it into two charts (e.g. "big platforms" and "specialist tools"), or use a table, or drop the outlier into a note.
- **Not enough data:** drop that element rather than pad it. Real numbers on fewer tiles beat padding.
- **The test before generating:** would the prospect's buyer learn something new and useful about their own business from cards 1–3? If not, the research isn't done yet.

## Closing deck (after a call)

The prompt combines the **Fireflies call analysis**, **that company's original research** and the **Context Center**.

**Pricing:** include the investment only if it came up on the call or the user gives it to you. Ask (in Stage 9 step 1): *"Do you want pricing in the deck? If so, what's the price or package?"*

```
Create a 9-card proposal from [USER COMPANY] to [PROSPECT COMPANY], based on our call on [date].
Use the prospect's own words where possible. Only use the facts provided below.

1. Title: "[PROSPECT COMPANY]: proposal", plus the one-line outcome they want
2. What you told us: their goals and current situation (quote them)
3. The problems to solve: pain points from the call, in priority order
4. Your questions, answered: each objection or concern raised, and how it's handled
5. The plan: scope and deliverables mapped to their goals
6. Timeline: phases that fit their timeline
7. Investment: [only if discussed or provided; otherwise leave this card out]
8. Why us / proof: from the user context
9. Next steps: agreed actions, owners and dates from the call, ending with "Get started"

Call analysis: [Fireflies extraction]
Original research: [Stage 6 research for this company]
User company context: [Context Center summary]
```

## Closing email

Draft it once the closing deck is ready:

> Subject: [PROSPECT COMPANY] × [USER COMPANY]: next steps
>
> Hi [first name],
>
> Thanks for your time today. I really enjoyed the conversation.
>
> As promised, here's the proposal built around what you told me: [closing deck URL]
>
> Quick recap:
> - [their goal #1, in their words]
> - [how we solve the main pain]
> - [the agreed next step and timeline]
>
> If you're happy to go ahead, you can get started here: [PAYMENT LINK]
>
> Any questions, just reply here.
>
> [User's name]

Ask: *"What's the payment link for your service? I'll put it in the email."* Then give them the final email, ready to copy and send.
