# The sequence (Stage 8)

## 1. Overview: show this first, with no email copy yet

> Here's how your sequence works:
> 1. **Connection request** (LinkedIn task, done by you), with a short personal note I write for each lead.
> 2. **Engage with their content** (LinkedIn task, done by you): like their latest post and leave a comment that adds value.
> 3. **Email 1** (automatic): goes out as soon as you mark the engage task complete.
> 4. **Email 2: the breakdown** (automatic, a reply in the same thread): 4 hours after Email 1, only if they haven't replied. It shows the numbers from their market and links to their Gamma deck.

Then ask: *"Do you want to write the two emails yourself, or do you want me to help you?"* Use the first name confirmed in Stage 0e for subject lines; don't ask again.

## 2. The steps and their exact content

### Step 1: Connection request (`linkedin_step_connect`)
- Wait: 0 days.
- **Each lead gets their own note**, Zack's exact wording, with the first two of their 5 companies:
  > [First name], has anyone in your team reached out to [Company 1] or [Company 2]?
- Claude writes it onto each lead's connection task right after the sequence is activated (section 4, "After activating"). The step's **message template body** is only the fallback:
  > Hey {{contact.first_name}}, Claude told me we should work together. I'll send you an email.
- If the campaign doesn't use the 5 companies, use the fallback note for everyone.

### Step 2: Engage with content (`linkedin_step_interact_post`)
- Wait: 0 days after step 1.
- Task note, Zack's exact words:
  > Engage in content and add value in the comments. Don't use AI. Use your brain.

### Step 3: Email 1 (`auto_email`, new thread)
- Wait: **0 minutes** after step 2 (engage) is marked complete. It sends at the next slot in their sending schedule.

**If the campaign uses the "5 perfect-fit companies" free sample** (the default when the user's offer helps prospects win customers), Email 1 is Zack's exact message:
- Body:

  > Hi [first name], are these companies a fit for [their company]:
  >
  > - [Company 1]
  > - [Company 2]
  > - [Company 3]
  > - [Company 4]
  > - [Company 5]
  >
  > I'd love to tap you in with them

- The 5 companies are different for every prospect, so this email is written per person (section 3): the lead's real first name, their company name and their 5 confirmed companies. Both leads at the same company get the same 5.
- **Subject:** suggest one that teases the content, e.g. `[best-known of the 5] + [their company]?` when one of the 5 is well known to them, otherwise `5 clients for [their company]`. Let the user pick.

**Otherwise,** use the email below.
- Subject: `Invitation: [first name] <> [confirmed first name]`.
- Body (Claude's draft, shown only if they asked for help; keep it this short). Written per person (section 3), so the bracketed parts are filled in with real values:

  > Hey [first name],
  >
  > Apollo and Claude helped me identify that [their company] could benefit from working with me. I sent you a connection request on LinkedIn in case it's easier to chat there.
  >
  > Tomorrow I'm going to send you over a personalised deck breaking down why I think it'll be great for us to have a chat and how I can help. I just have to finish the research first.

### Step 4: Email 2 (`auto_email`, reply to thread)
- Wait: **4 hours** after email 1 (`wait_time: 4`, `wait_mode: hour`). Apollo stops the sequence when someone replies, so it only goes to people who haven't.

**If the campaign uses the "5 perfect-fit companies" free sample,** Email 2 is Zack's exact message, with the numbers from that prospect's Stage 6b search:

  > It's not just those 5. I've built an AI agent workflow for you that has produced:
  >
  > - [number of leads] leads
  > - All of them in [their ICP location]
  > - [headcount range] company headcount
  > - All of them are using either: [tech 1], [tech 2] or [tech 3]
  >
  > <a href="[their deck link]">Click here for a full breakdown</a>

  "full breakdown" is the hyperlink to their Gamma deck. Every number must come from Apollo's results for that prospect; if one is missing, drop that line rather than guess. "All of them are using either…" must be literally true, so the lead count has to come from the search **with** those technologies applied as a filter (any of them).

**Otherwise,** use the email below.
- Type: reply to the previous thread.
- Written per person (section 3). Subject: `Re: ` + that person's exact Email 1 subject (Apollo requires a subject on personalised emails; tested live, it still lands as a reply in the same thread).
- Body:

  > [First name], as promised, I put this together for you: [their company's deck link]
  >
  > If you like it, please <a href="[BOOKING LINK]">click here</a> to have a quick chat with me this week.
  >
  > Thanks

- Wait for this version: **1 day** after email 1.

**Signature**
- Never ask for a sign-off name, and never put a sign-off in the email body. The signature comes from the user's Apollo mailbox settings (Stage 1), so always set `include_signature: true` on both emails.

**If the user writes their own emails,** keep their words but check that:
- email 2 contains a place for the deck link and the booking link;
- email 2 is short.

Point out anything missing before building.

### Optional step 5: Phone call (`call`): offer this after email 2 is agreed

> Do you want to add a phone call task as the final step, 24 hours after the deck email? It's just a quick call to confirm they got your email and the deck, **not** a pitch. For this you'll need their phone numbers. I can find them in Apollo, and it uses extra credits.

**If yes:**
- Wait: **1 day** after email 2. Priority: high.
- Task note:

  > THE PURPOSE OF THIS CALL IS NOT TO PITCH. DO NOT SELL.
  > The only goal is to get a meeting in the diary.
  >
  > Say: "Hey [their first name], it's [your name] from [your company]. I emailed you a deck I built yesterday explaining why I think it's good for us to work together. Did you have a chance to open it? If not, I'll call back in a couple of days."
  >
  > - They've seen it: great. Now get a meeting in the diary while you're on the call.
  > - They haven't: "No worries, I'll call back in a couple of days."
  > - If they give you the opportunity to pitch, great. Otherwise, the meeting is the win. That's it.

- **Phone enrichment.** Follow `apollo-connector.md` → "Phone numbers": the waterfall check, the exact wording, polling, Do Not Call handling, and saving the numbers on the contacts.

**If no:** the sequence stays at 4 steps.

## 3. Per-person emails (no custom field needed)

Every lead gets their **own finished Email 1 and Email 2**, written by Claude and stored in Apollo at enrollment (`step_content_overrides` on `apollo_emailer_campaigns_add_contact_ids`). Apollo sends that text exactly as written, so there are no merge tags to break and no deck-link custom field to create. Tested live on 29 Oct 2026: 3 of 3 stored and read back; a self-test delivered Email 1 and the personalised Email 2 as one Gmail thread.

1. **Master table, keyed by company.** For each company keep: Apollo organization id, its deck link, and (if used) its 5 fit companies. Match each lead to their company by `organization_id`, never by name, so two leads at the same company always get the same content.
2. **Write each lead's emails** with real values and no merge tags: their first name, their company, their 5 companies, their deck link, the booking link. Email 2's subject is `Re: ` + their Email 1 subject.
3. **Show the user one review table before enrolling:** lead, company, Email 1 subject, the 5 companies (if used), deck link. Apply any fixes.
4. **Templates are only a fallback**, sent only to someone with no personal email stored. They pull each company's backup copy from the two company fields (below), so even a fallback carries the right content:
   - Email 1: subject `Invitation: {{contact.first_name}} <> [user's first name]` (e.g. "Invitation: Ryan <> Zack"; the user's name from Stage 0e, written in as plain text), body `Hi {{contact.first_name}}, {{account.Email Template 1}}`.
   - Email 2 (reply, empty subject): body `{{account.Email Template 2}}` (the 5-companies version has no greeting; for the other version use `{{contact.first_name}}, {{account.Email Template 2}}`).
   - Apollo's tag format, confirmed by Zack: `{{contact.first_name}}` and `{{account.[field label]}}`, using the field's exact label. After creating the sequence, read the steps back with `apollo_emailer_campaigns_show` and check the tags survived; if Apollo shows them in red in the preview, have the user re-insert them with the dynamic-variable picker (**{ }**). If the user skipped the backup fields, use the plain fallbacks instead: Email 1 subject `Invitation: {{contact.first_name}} <> [user's first name]`, body "Hi {{contact.first_name}}, who's the best person at your company to talk to about new clients?"; Email 2 "{{contact.first_name}}, just checking you saw my note above."
5. **Never pass merge tags inside personalised content.** They are not substituted there.

**LinkedIn note:** LinkedIn steps can't take per-person content at enrollment (Apollo allows that only on email steps). Instead, once the sequence is active, Claude rewrites each lead's connection task with `apollo_tasks_update` (`standalone_outreach_task_message.body_text`). Tested live: Apollo shows the rewritten note on the task. That's why the connection request is step 1: its task exists the moment the sequence goes live.

**Backup: the "Email template 1" and "Email template 2" company fields.** The user creates these two account fields when the account list is saved (SKILL.md Stage 3g). Before enrolling, Claude writes each company's email copy into them. It's a failsafe: the fallback templates pull from these fields, so a lead without a stored personal email still gets their company's content.
- **Body only, no subject line** (a subject would show up as the email's first line).
- **No first name or greeting.** The fields belong to the company and are shared by both leads there; the template adds `Hi {{contact.first_name}}, ` in front. So Email Template 1 starts *"are these companies a fit for [Company]:"* and Email Template 2 is the full Email 2 (*"It's not just those 5…"*), with the deck link written out as a plain URL after "Click here for a full breakdown:" (fields are plain text, so no hyperlinks).
- Keep the line breaks (they're multi-line fields). Find the fields with `apollo_fields_index` (`modality: account`), match the labels case-insensitively, and write with `apollo_accounts_update` (`typed_custom_fields` keyed by field id). If the fields don't exist, remind the user once, then carry on; the sequence doesn't depend on them.

## 4. Build, preview, enroll, activate

**Create** the sequence:
- Name: suggest `GTMAI – [account list name]`; first check that no sequence already has that name.
- Status: **inactive**. Use the team's default sending schedule.
- Keep these defaults on: finish on reply, finish on interested, pause on out-of-office.

Step mapping:

| Step | type | wait | content |
|---|---|---|---|
| 1 | `linkedin_step_connect` | 0, day | touch `emailer_template.body_html` = fallback connection note |
| 2 | `linkedin_step_interact_post` | 0, day | `note` = task note; no touches |
| 3 | `auto_email` | 0, **minute** | touch `type: new_thread`, the safe fallback template (section 3); `include_signature: true` |
| 4 | `auto_email` | 4, **hour** (1, day for the non-5-companies version) | touch `type: reply_to_thread`, subject `""`, the safe fallback body; `include_signature: true` |
| 5 (optional) | `call` | 1, day | `note` = call note, `priority: high` |

After creating it, show only the name and a one-line summary per step.

**Enroll:**
1. List email accounts. Use the default mailbox unless the user picks another.
2. Show a summary: sender email, sequence name, number of contacts, status.
3. *"Okay, I'm now going to go ahead and add these leads to the sequence. Do I have your permission?"*
4. Enroll them, with the sequence still **inactive**, passing each lead's Email 1 and Email 2 in `step_content_overrides` (both `subject` and `body_html` for each step), plus:
   - **allow contacts from the same company in the same sequence = on** (up to 2 per company);
   - **allow unverified emails = off**.
5. Report enrolled vs. skipped, with Apollo's reasons. Then read `step_content_overrides_result`: `written_contact_count` must equal the number enrolled. Anyone in `not_written` would get the fallback template; fix them with `apollo_emailer_campaigns_update_step_content` before going on. If someone was skipped as unverified even though enrichment said verified, explain that and ask before retrying.

**Pre-launch check (hard rule, right before activating):**
1. Read every lead's stored emails with `apollo_emailer_campaigns_step_content` (all lead ids, both email steps). Each lead must have content for Email 1 **and** Email 2, with the right company's names and deck link.
2. Read the sequence's headcount (`contact_statuses` from `apollo_emailer_campaigns_show`) and compare it with the number of personalised leads. More people in the sequence than personalised leads means someone was added by hand: say *"[N] person/people in this sequence don't have a personalised email. Open the sequence's Contacts tab in Apollo and remove anyone who isn't on your GTMAI leads list."* and don't activate until the numbers match.
3. Show the result in one line: *"✅ [N] of [N] leads have their own Email 1 and Email 2. Nobody gets the fallback."*

**Activate:**
- Ask: *"Ready to activate? Once it's active, Apollo creates your LinkedIn tasks straight away and sends the emails on schedule."*
- Activate only after a yes, and only after the pre-launch check passed.

**After activating: personalise the connection notes (straight away).**
1. Tell the user: *"Give me a minute before you do your LinkedIn tasks. I'm writing each person's connection note."*
2. Find the connection tasks with `apollo_tasks_search` (`emailer_campaign_id`). Apollo can take a few seconds to create them; search again if the list is empty or short.
3. For each task, match the lead by `contact.id` and update it with `apollo_tasks_update`: `standalone_outreach_task_message.body_text` = that lead's note.
4. Check: number of connection tasks = number of leads, and every update returned the new note. Then: *"✅ All [N] connection notes are ready. Your LinkedIn tasks are in Apollo under Tasks."*
- In the congratulations message, add: *"Don't add leads to this sequence by hand in Apollo. Come back here and I'll add them with their own emails."*

**If the user's Apollo plan blocks LinkedIn or call steps:**
- Build the sequence without steps 1–2, with email 1 at a 0-minute wait.
- Give the user each lead's connection note in the chat, and tell them to send the request and like a post by hand on day 1.
