# Research and ranking (Stages 4 and 6)

## Sources and budget
- **Apollo company data:** whatever came back with the list search. That includes industry, size, location, technologies, funding and headcount growth. **Don't** call paid company enrichment or job-posting tools unless the user asks.
- **Web search (free):** the company site, careers page, news, press, executives' LinkedIn posts, podcasts and reviews.
- **The user's Context Center** defines what counts as "fit": the offer, the buyer, the problems it solves.

**Research caps**, to stay within the chat's limits:
- **Stage 4:** do a quick pass on the Apollo data for every company, then deep web research on the best **8**, with at most **3 searches each**.
  - **Keep going until the top 5 are strong (hard rule).** A pick is strong at **60/100 or more**. If fewer than 5 of the first 8 reach 60, research the next best companies from the quick pass, 4 at a time (at most 8 more, 3 searches each), before you present anything. Never put a company under 60 in the top 5 while researched-able candidates remain, and never leave the runners-up unresearched when a top-5 pick is weaker than them.
  - If you still have fewer than 5 at 60+, present only the strong ones, say plainly how many fell short and why, and offer to read more companies.
- **Stage 6:** at most **5 searches** per company.

**Sources:** cite a link for every web signal. Label Apollo-sourced facts "Apollo data". If you couldn't verify something, leave it out or mark it "unconfirmed". If web search isn't available, say so and rank on Apollo data only.

## Buying signals checklist (strongest first)
1. **Hiring for the problem:** open roles tied to the user's offer, or job posts that describe the pain. Check the careers page through web search.
2. **New leader in the buying function:** a VP, Head of or C-level hire in the last 90 days.
3. **Money events:** funding, acquisition, or a revenue or customer milestone.
4. **Expansion:** a new market, office, product line, launch or partnership.
5. **Tech-stack change:** adopting or dropping tools relevant to the offer.
6. **Growth:** fast headcount growth (from Apollo data).
7. **Public statements:** executives posting or talking about the problem.
8. **Visible pain:** reviews or complaints (G2, Trustpilot, Glassdoor) that point at the problem.

## Ranking (Stage 4): score out of 100

| Factor | Weight | What earns points |
|---|---|---|
| ICP fit | 35 | Industry, size, geography and business model match the Context Center |
| Signal strength and recency | 35 | How many signals there are and how recent; the top 3 count most |
| Reachable buyer | 15 | Likely to have a decision-maker at the right seniority |
| Deal potential | 15 | Size and budget signals relative to the user's offer |

Apollo's topic-level buying-intent scores aren't available through the connector. The list search does include a yes/no flag, `has_intent_signal_account`. If it's true, count it as a strong signal ("Apollo shows an active intent signal"). If the Stage 3 search used the intent filter, every company on the list already matched those intent topics: count that as the intent signal for all of them, even when `has_intent_signal_account` is missing, and don't tell the user intent data is missing. If the user tells you a company's intent level from Apollo, use that as a tiebreaker.

The account-list results don't include industry, employee count or a description. Get those from the company's website through web search before you score ICP fit.

Format for each of the top 5:

> **1. [Company]** ([industry], [size], [HQ]): **86/100**
> Why them, why now: [2–3 lines naming the strongest signals, each linked or marked "Apollo data"]

Then the 3 runners-up, one line each.

## Per-company research (Stage 6)

> **[Company]: research**
> **What they do:** one line.
> **Top 3 signals → pain points / opportunities:**
> 1. [Signal] → [what it points to] ([source](link))
> 2. …
> 3. …
>
> **Why now:** one line.
> **How [user's company] helps:** 2–3 bullets mapping the offer (from the Context Center) onto these pains.
> **Deck angle:** one line.
>
> **Free sample** (from your deck recipe):
> - [headline number or finding] ([source])
> - [table / list summary] ([source])
> - …
>
> Does this look right? If not, give me more context.

Keep this block. It's reused for the closing deck, and its deck angle goes on the Campaign card.
