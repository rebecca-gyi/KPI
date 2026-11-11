# KPI repo: motor quote tracking (Rebecca, HM Partners)

This repo tracks Rebecca's ad hoc motor insurance quotes for HM Partners: how many she submits, how many are right or wrong, what she earns, and how fast she works. When she says **"update the data"**, **"mid day check"** or **"update my speed"**, follow the workflow below.

## Sources of truth

- **Google Sheet:** "Ad Hoc Motor Quotes", id `1rYJFK94gDPXPRrKAPYcCToLr0PzFGewH3RUipeBTeYA`
  - **Rabies Reference** tab: Rebecca's own log of quotes. Data starts at row 3 (row 2 is blank). Columns B–K:
    No · Road Tax Expiry · Insurance Expiry · License Plate · Client · Cert of Merit · NCD Check · Source · Category · Quote Date
  - **Sheet1** tab: Keith's payout sheet. Columns A–F:
    S/N · Plate · Quoted · Settled · Amount Due · Remarks
- **Gmail:** quotes Rebecca sends to Keith (`keithongyn.gi@gmail.com`). Use `to:keithongyn.gi@gmail.com after:YYYY/MM/DD`.

Read the sheet with the Sheets API (`values.get`) or the export CSV. **Never use gviz**: it follows filters and hides rows.

## Counting quotes (Rabies Reference)

- A row counts as a quote if it has a **plate and a Quote Date**, even when No is blank.
- Dates are DD/MM/YYYY. Zero-pad single digits ("3/11/2026" → 03/11/2026). Fix obvious typos such as "28/10/20269" → 28/10/2026.
- Category values: Private, Commercial, PHV, Private Comp Car (show as "Company car"), BUS (show as "Bus").
- A plate can be quoted twice (a requote). Count each dated row separately.

## Matching to payouts (Sheet1)

- Match by plate. Strip a trailing "(n)" (e.g. `SNT4753M (2)` → SNT4753M). The "(2)" row pays the second quote of that plate.
- Remarks meanings:
  - `Verified` = right, $18
  - `Requote` = right, $18
  - `Errors` = wrong, $6
  - `Errors (Paid previously)` = a −$12 clawback on a quote already paid at $18. That quote becomes wrong. Count the clawback as a correction, not as a quote.
  - `Commission` = travel insurance commission. It is not a quote.
- Known aliases:
  - Sheet1 `Triumph Electrical System Engineering Pte Ltd (NEW)` = ABC1234D
  - Sheet1 `SDV6660S` = Rabies SNR5368X
- Known special cases:
  - GBJ220C (27/08): plate typo of GBJ8220C, not paid.
  - GBM35H (26/08): duplicate, paid once on 27/08.
  - WC9469J (18/09): never paid (Income block).
  - SJE3885Z: 04/11 quote is right ($18); 05/11 requote is wrong ($6).
- A quote with no Sheet1 row yet = **Not paid yet** (not wrong).
- **Settled** column = the month the payout was made (Sep, Oct, Nov…). Blank = not paid yet. Quotes are paid the month after they're quoted.
- Ignore Sheet1 rows with no plate. Keith pre-fills rows with a date, $18 and Verified.

## Keeping the sheet tidy (Rebecca wants this every update)

1. **Renumber the No column** in Rabies Reference: 1…N top to bottom, no blanks, no repeats. Rows stay sorted by road tax expiry.
2. **Check Gmail for quotes sent to Keith that aren't in Rabies Reference.** Add them with plate, client, Cert of Merit (yes if "Eligible for certificate of merit"), Source, Category and Quote Date, plus insurance expiry if the email gives it. Append them at the bottom; Rebecca moves them into place.
3. If a quote was emailed but its row has **no Quote Date**, fill in the date it was sent.
4. **Source:**
   - Email = Keith sent the request by email.
   - Whatsapp = Rebecca started the thread herself (WhatsApp images, "From Meyer Motors/Gerald", or Keith's bulk emails with several log cards).
5. Never delete rows or change Sheet1. Sheet1 is Keith's. Flag odd values (e.g. a $69.25 typo, or a "Slack" source) instead of fixing them.

## Dashboard rules

- **Targets:**
  - 10 quotes per working day, 5 days a week (50 a week).
  - Monthly goal = 10 × working days × $18.
- **Averages are per working day** (Mon–Fri, including zero days, from the first quote to the latest).
- **Accuracy is month by month:** right ÷ (right + wrong). Not-paid-yet quotes are excluded. The headline tile shows the current month, with all-time underneath.
- **Income:**
  - The headline tile is **"Earned in <current month>"**: payouts for quotes made that month, including clawbacks.
  - Also show already paid, still to be paid, and lost to errors.
- **Pay comparison (current month only, quote fees only):** Rabies quotes × $18 vs Sheet1 quote fees. Show the difference only, no detail list.
- **"Wrong or not paid" list:** only months whose payout is not settled yet. Hide past paid months.
- **No weekly table** (Rebecca removed it as too much). The weekly target bar stays.
- **By vehicle type:** donut of share plus accuracy bars per type.

## Speed (from Gmail)

- **Times:** take each sent email's timestamp and convert to Singapore time (UTC+8).
- **Minutes per quote:** the gap between consecutive quote emails on the same day. Gaps over 2 hours are breaks and left out. Report the median.
- **Turnaround** (only when Keith's request can be found): working days from the **ready day** to the reply.
  - Ready day = the later of Keith's request and (road tax expiry − 60 days). Insurers won't quote earlier.
  - Weekends don't count.
- Threads Rebecca started (WhatsApp, bulk emails) count toward minutes per quote only.
- A re-sent quote email counts for speed but is not a new quote unless she says it was paid twice.

## When reporting back

Keep it short:

- Today's count vs the target of 10, as a small table of time sent, plate and status.
- What changed in the sheet.
- November (current month) quotes, accuracy and earnings.
- Any differences, explained by plate.

Don't paste personal details (NRIC, phone numbers, addresses) from emails anywhere.
