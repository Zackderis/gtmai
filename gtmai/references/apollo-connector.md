# Apollo connector

Tool names can change. Use whichever Apollo action matches; the names below are the current ones. Tell the user what you're doing in plain words.

## Actions, costs and notes

| Need | Action (current name) | Cost | Notes |
|---|---|---|---|
| User's name, credits, waterfall capability | `apollo_users_api_profile` (`include_credit_usage: true`, `include_waterfall_capability: true`) | free | Call once per chat, before the first enrichment |
| Mailbox connected? | `apollo_email_accounts_index` | free | Use the account where `default` is true unless the user picks another |
| AI Context Center | `apollo_context_center_show` | free | 404 = not set up yet. Check whether it's a draft or live |
| Find a list by name | `apollo_labels_index` | free | Lists have a modality: `accounts` (companies) or `contacts` (people). Names are unique per modality |
| Companies in an account list | `apollo_mixed_companies_search` with `account_label_ids: [list id]`, **`per_page: 10`**, paging through | **1 credit per request** with results | Each company record is about 5,000 characters, so 100 per page overflows the chat. Required wording for 1 request: *"This will consume 1 credit. Do you want to proceed?"* For several pages, confirm the total first. Saved companies come back in `accounts`, with `organization_id`, `domain`, location, `organization_revenue_printed`, `organization_headcount_twelve_month_growth` and `has_intent_signal_account`. Industry, employee count and description are **not** included, so get those from web research |
| Free company lookup | `apollo_organizations_lookup` | free | No list filter |
| Company enrich / job postings | `apollo_organizations_enrich`, `apollo_organizations_job_postings` | 1 credit each | Only if the user asks. Use web search for hiring signals instead |
| People at a company | `apollo_mixed_people_api_search` with `organization_ids` (or `q_organization_domains_list`), `person_titles`, `person_seniorities`, `contact_email_status: ["verified"]` | free | Use a confirmed filter set (the user approved the titles). No emails in the results |
| Enrich people | `apollo_people_bulk_match` with `details: [{id: <person id from search>}]` | 1 credit per match | Max 10 per call. See the wording below |
| Save people as contacts | `apollo_contacts_bulk_create` / `apollo_contacts_create` with `label_names: [leads list]` | free | Then read back with `apollo_contacts_search` (`contact_label_ids`) |
| Custom fields | `apollo_fields_index` | free | No create-field action; the user creates fields in the UI. GTMAI needs no contact fields (no deck-link field): per-person emails carry the deck link. The only fields are the two account backup fields (row "Backup email fields") |
| Phone numbers | `apollo_people_bulk_match` with `reveal_phone_number` or `run_waterfall_phone`, then poll `apollo_webhook_result_show` | extra credits | See "Phone numbers" below |
| Find an existing sequence | `apollo_emailer_campaigns_search` | free | Check for a duplicate name before creating |
| Create the sequence | `apollo_sequences_create` (`active: false`) | free | See the step mapping in `sequence.md` |
| Read a sequence or step | `apollo_emailer_campaigns_show` | free | Use it to read back the merge tag after a fix |
| Enroll | `apollo_emailer_campaigns_add_contact_ids` | sends email | `sequence_same_company_in_same_campaign: true`, `sequence_unverified_email: false`. Report enrolled vs. skipped |
| Per-person emails | `step_content_overrides` on the enroll call: `[{contact_id, step_overrides: [{emailer_step_id, subject, body_html}]}]` | free | Email steps only (not LinkedIn or call). Subject and body are both required, even on a reply step. Sent verbatim, no merge tags. Check `step_content_overrides_result.written_contact_count` |
| Read stored per-person emails | `apollo_emailer_campaigns_step_content` (`id`, `contact_ids`, optional `emailer_step_id`) | free | Pre-launch check |
| Fix one lead's stored email | `apollo_emailer_campaigns_update_step_content` | free | Works while enrolled; not on an email already sent |
| Sequence headcount | `apollo_emailer_campaigns_show` → `contact_statuses` | free | Compare with the number of personalised leads |
| Personalise a LinkedIn connection note | `apollo_tasks_search` (`emailer_campaign_id`) → `apollo_tasks_update` (`standalone_outreach_task_message.body_text`) | free | Only after activation, once the task exists. Tested live: the Apollo task shows the new note |
| Backup email fields | `apollo_fields_index` (`modality: account`) → `apollo_accounts_update` (`typed_custom_fields`) | free | "Email template 1" / "Email template 2", created by the user in Stage 3g |
| Activate | `apollo_emailer_campaigns_approve` | sends email | Only after an explicit yes in that turn |

## Apollo's AI agent: market research on a prospect's own customers

Use this when the deck recipe needs the **prospect's** market: their TAM, ICP, buying-intent topics, or the technologies their customers use. It never touches the user's Context Center.

- **Create:** call `apollo_agent_find_prospects` with the recipe's approved request, word for word, then a separate "Context:" line. Template, tested live:

  ```
  For [prospect domain]: identify their TAM, their total ICP, a list of strong buying intent topics for them, and the technologies their ICP companies use.

  Context: this is research about [Prospect]'s own customers (who they sell to), not my ICP. I'm preparing a deck for [Prospect] to show them I know how to find their customers. Don't save, enrich or spend credits without asking me.
  ```

- **Poll:** call `apollo_agent_poll_task` with the `task_id` and `cursor`, waiting `poll_after_ms` between calls. It takes about 3–6 minutes. Do the web research for the same company while it runs.
- **Cost:** the live test spent **zero credits**. If the agent asks to spend credits (`awaiting_input`), relay its exact question to the user and never answer it yourself.
- **What comes back:** a brief with live Apollo counts; ICP firmographics and buyer personas; use cases, triggers and bad fits; Bombora intent topics checked against Apollo's catalogue, tiered; and technology counts within the ICP. Use these numbers on the deck. Say "Apollo count" in the research summary you show the user, but never print a source line (e.g. "Source: Apollo, Oct 2026") on the deck itself.
- **Stalls happen.** In testing, a task sat on its final scoring step for 15+ minutes with no new messages.
  - If nothing new arrives for about 8 minutes, tell the user. Use what the agent already reported (pool sizes, filters).
  - Then take a narrower route: re-ask for fewer companies on the same `task_id`, or do the qualification yourself with web research on a shortlist.
- **Sanity-check the numbers.** If one looks odd (e.g. one CRM count far smaller than a similar one), say so or leave it out rather than chart it.
- **Follow-ups:** continue the **same** `task_id`, e.g. "break the TAM down by company size" or "give me 10 example accounts".

## Getting company and organisation ids right
- In `apollo_mixed_companies_search` results, saved companies come back in the **`accounts`** bucket.
- For people search, use each account's **`organization_id`**, not its `id`. Passing the account `id` matches nothing, and no error is raised.
- New (unsaved) companies come back in the `organizations` bucket. For those, use `id`.

## Enrich people (search results)
1. Call `apollo_users_api_profile` once with `include_credit_usage` and `include_waterfall_capability`.
2. **Waterfall email off**, the usual case. Say exactly:
   *"Found [N] contacts. Enriching all will use up to [N] credits. You have [X] credits remaining. Do you want to proceed?"* Format X with thousands separators.
   Then run `apollo_people_bulk_match` with person ids, in batches of up to 10.
3. **Waterfall email on.** Say exactly:
   *"Found [N] contacts. Enriching all with waterfall enrichment may use additional credits that vary by your plan and data provider and can be substantially more than a standard match (no charge for people where nothing is found). You have [X] credits remaining. Do you want to proceed?"*
   Then set `run_waterfall_email: true` and poll `apollo_webhook_result_show` with the top-level `request_id`. Retry with back-off for up to about 3 minutes.
4. If the response includes an `mcp_credits` block, show the estimate, the spend and the balance.
5. Keep only verified emails, then save those people as contacts in the leads list.
6. If an Apollo agent tool quotes its own cost question, pass it on word for word instead.

## Phone numbers (optional call step only)
1. Reuse the waterfall check from above.
2. Ask with the exact wording for the path that applies:
   - **Waterfall phone on:** *"This will enrich [N] people with waterfall enrichment, which may use additional credits that vary by your plan and data provider and can be substantially more than a standard match (no charge for people where nothing is found). Do you want to proceed?"* Then use `run_waterfall_phone: true`.
   - **Otherwise:** *"This will enrich [N] people and use up to [N] credits (1 credit per match, no charge for unmatched), plus additional credits for each phone number successfully revealed (no charge if a number isn't found). Do you want to proceed?"* Then use `reveal_phone_number: true`.
3. The results are asynchronous. Poll `apollo_webhook_result_show` with the top-level `request_id`. If that tool isn't available, don't spend credits; ask the user to reconnect Apollo.
4. **Do Not Call:** if a number is flagged DNC, show a clear warning, don't save it, and tell the user to skip that call task.
5. Save the other numbers with `apollo_contacts_update` (`mobile_phone` or `direct_phone`).

## Gotchas
- **Verified only, no catch-alls.** Search with `contact_email_status: ["verified"]`, keep only verified people after enrichment, and never enroll unverified contacts. Apollo can return `email_status: "verified"` with `email_domain_catchall: true` (verdict "warn"). Zack's standard is "safe to send": verified **and** not catch-all. Drop catch-all contacts, or ask the user before keeping one. Apollo's sending protection may block catch-all addresses at send time anyway.
- **Lists have 3 modalities:** `accounts` (companies), `contacts` (people) and `emailer_campaigns` (sequences). Match account lists only in Stage 4, and contacts lists only for the leads list.
- **Saved contacts vs. enrichment.** Contacts created from enrichment data may not link to Apollo's person record (`person_id` null). After saving, read the contacts back and check the email status and LinkedIn URL. Note any missing LinkedIn URL on the Campaign card so the user can find the person by hand.
- **Buying-intent topic scores** aren't available through the connector. Use intent only if a result includes it, or if the user reads it from Apollo and tells you.
- **Sequences are created inactive.** Enrolling into an inactive sequence sends nothing. Activation sends real emails.
- **LinkedIn steps are manual.** Apollo creates the tasks, and the user does them and marks them complete. Email 1 then goes out at the next scheduled slot.
- **Upgrade-required errors** (plan limits): explain them plainly and offer the workaround. For blocked LinkedIn or call steps, see the end of `sequence.md`.
