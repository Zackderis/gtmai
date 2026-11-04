# Manual mode (when a tool isn't connected)

GTMAI never stops because a tool won't connect. If Apollo, Gamma, Fireflies or web search isn't available after Stage 1, switch **that tool only** to manual mode: {A} does the thinking and writing, and the user does the clicks in that tool's own website. Tell the user in one line what changes, e.g. *"Gamma isn't connected, so I'll write each deck's prompt and you'll paste it into Gamma. It takes about a minute per deck."*

Everything else in the stage files still applies: the order of the stages, the approvals, the accuracy rules and the Campaign card. Add **Manual: [tool]** to the card's Stage line so a resumed chat knows.

## Apollo in manual mode
- **Stage 2 (Context Center):** send the manual steps in the stage file. Skip reading it back; use the brief and the user's answers as the business context.
- **Stage 3 (company search):** give the user the exact filters to set in Apollo's **Companies** search (look-alike companies, locations, employee range, technologies, buying-intent topics, "exclude companies in my CRM"), one per line. They run it, save the search, select all, **Add to list → Create new list**, then open the list and **Export** it as CSV. Ask them to attach the CSV here.
- **Stage 4 (top 5):** read the companies from the CSV instead of the API. Do the same ICP-fit, competitor and net-new checks, the same web research and scoring.
- **Stage 5 (people):** give the exact job titles and seniorities to search in Apollo's **People** search, filtered to the 5 companies and to verified emails. The user picks up to 2 per company, clicks **Access email** (this uses their Apollo credits, so say so once), adds them to a new list, and exports it as CSV. Read the CSV and check every email shows as verified.
- **Stage 6 (deck numbers):** give the user the three people searches for each prospect's market (total market, ideal customers, low-hanging fruit) as exact filters; they paste back the three counts and 5 company names from the last search. Use only the numbers they paste.
- **Stage 8 (sequence):** give the step-by-step build for Apollo's **Sequences → Create**: LinkedIn connection task, LinkedIn engage task, **Email 1 and Email 2 as *manual* email steps** (so each lead's own copy can be pasted before it sends), the waits, and the stop rules. Then give a table with every lead's own Email 1 and Email 2, ready to paste into each task. Never tell them to activate before the pre-launch check: ask them to confirm every lead is in, and every manual email has its own copy.

## Gamma in manual mode
1. Build the full outline exactly as `references/gamma-decks.md` describes, every blank filled, and give it in one code block.
2. Tell the user:
   > 1. Open [gamma.app](https://gamma.app) and click **Create new → Paste in text**.
   > 2. Paste the text below.
   > 3. Choose **Social** (4:5) and **5 cards** for an outreach deck (**Presentation** and **9 cards** for a closing deck), then **Generate**.
   > 4. Click **Share** and set it to **Anyone with the link can view**.
   > 5. Copy the deck's link (it starts with gamma.app/docs/) and paste it here.
3. When they paste it, strip anything after `?`, record it on the Campaign card, and ask them to check the 5 cards against the confirmed contents. If something's off, write the exact fix for them to make in Gamma.

## Fireflies in manual mode
Ask the user to open the call in Fireflies, copy the transcript (or download it as .txt) and paste or attach it here. Then continue Stage 9 from the extraction step.

## Web search unavailable
Ask the user to paste the prospect's homepage text and any page you need (services, about, careers), or carry on with Apollo data only and label the research as "Apollo data only, no web check".
