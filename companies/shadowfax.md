# Shadowfax

**2 questions** · 1 drive · latest 3 Nov 2026 · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 1 · [Math](../topics/math.md) 1 · [Greedy](../topics/greedy.md) 1 · [Other](../topics/other.md) 1  
**Seen at:** IIT Guwahati

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-03 · IIT Guwahati · FTE](#2026-11-03--iit-guwahati--fte)
  - [Shadowfax OA pattern](#q1-shadowfax-oa-pattern)
  - [Manpower Roster Optimisation (AI-assisted assignment)](#q2-manpower-roster-optimisation-ai-assisted-assignment)

</details>

---

## 2026-11-03 · IIT Guwahati · FTE

### Q1. Shadowfax OA pattern

Round 1: 20 minutes, 21 MCQs on company/corporate ethics (basically a psychometric test).

Round 2: 40 minutes, 39 questions on logical reasoning / aptitude (very, very easy). Try to finish all questions as fast as possible.

Round 3 (AI activity round, 45 minutes, can be given from the room): use any available LLM to solve the given problem. Evaluators judge how good your prompts are, so the chat history must be submitted. Deliverables: 3 Excel sheets and 1 PDF (the PDF is the chat history).

<sub>Topics: OA Format · Source: [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L103), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L104), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L105), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L106), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L107), [Manpower Roster Optimisation - Assignment.pdf](../archive/files/20067-Manpower_Roster_Optimisation_-_Assignment.pdf), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L109), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L110), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L111)</sub>

### Q2. Manpower Roster Optimisation (AI-assisted assignment)

Campus-placement assignment for the NCR distribution centre. Across a 7-day week, a Forward shipment stream is processed in two sequential stages, Primary then Secondary, with a one-hour gap between them. Design an optimised **monthly** manpower roster across FTC, Flex and PT that processes the entire volume at the **lowest monthly cost**. Any AI tool may be used and the full prompt history must be submitted.

**Daily incoming Forward volume** (week starts Monday = Day 1; repeats every week of the month, about 4.33 weeks, roughly 8,57,000 shipments a month):

| Day | Volume |
|---|---|
| Monday | 30,000 |
| Tuesday | 35,000 |
| Wednesday | 25,000 |
| Thursday | 27,000 |
| Friday | 36,000 |
| Saturday | 35,000 |
| Sunday | 10,000 |

Weekly total: 1,98,000. Peak day: Friday.

**Hourly distribution** (hourly volume = day total x hourly %, same profile every day):

```
00:00 2.73   01:00 2.73   02:00 1.82   03:00 1.82
04:00 0.91   05:00 0.91   06:00 1.82   07:00 2.73
08:00 3.64   09:00 4.55   10:00 5.45   11:00 5.45
12:00 4.55   13:00 3.64   14:00 3.64   15:00 4.55
16:00 5.45   17:00 6.36   18:00 7.27   19:00 8.18
20:00 7.27   21:00 6.36   22:00 4.55   23:00 3.64
```

**Processing flow:**
- Primary: every shipment is scanned and sorted into 4 directional bins (North, South, East, West), a 1:4 sort. Per-person capacity is higher.
- Secondary: shipments move to Secondary one hour after Primary and are sorted into 30 bins by destination hub area, a 1:30 sort. Per-person capacity is lower.
- The model must respect the Primary-before-Secondary sequence, the one-hour gap and the capacity difference.

**Manpower categories:**

| Category | Working hours | Primary cap/day | Secondary cap/day | Cost |
|---|---|---|---|---|
| FTC (Full-Time Contractual) | 8 h | 1,000 | 500 | Rs 20,000 / month |
| Flex | 8 h | 800 | 400 | Rs 700 / day |
| PT (Part-Time) | 4 h | 600 | 300 | Rs 12,000 / month |

Capacity is shipments processed per person per day at the stage the employee is assigned. Weekly offs apply to FTC only. Flex and PT may each be deployed up to a maximum of 10% of total manpower on particular (peak) days; FTC forms the remaining base (at least 80%). The 7-day pattern repeats each week; build the roster and cost at monthly level (FTC and PT monthly, Flex per deployment day).

**Mandatory outputs:**
1. Manpower Roster (Format 1): employee-level, day-on-day (D1-D30) Present / Off across the month. Columns: Emp ID, Category, Stage (Primary/Secondary), Shift, D1..D30, Mo. Days. P = present, O = weekly off (FTC only), - = not engaged (Flex).
2. Hourly Volume Planning (Format 2): one row per Day x Hour with Incoming, Primary processed, Secondary processed and Pending (volume awaiting the next stage at the end of the hour).
3. Monthly Cost Calculation (Format 3): per category headcount, deployment days, rate, monthly cost and total, plus a short cost-optimisation note giving the chosen FTC/Flex/PT mix and the saving versus an all-FTC baseline.
4. AI Prompt History (Format 4): the complete AI conversation exported as a PDF.

Evaluation considers accuracy of calculations, operational understanding, roster optimisation, cost efficiency, quality of the problem-solving approach, and whether the outputs follow the standard formats. (Per the poster, 3 Excel sheets and 1 PDF of chat history were submitted.)

<sub>Topics: Math, Greedy, Other · Source: [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L103), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L104), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L105), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L106), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L107), [Manpower Roster Optimisation - Assignment.pdf](../archive/files/20067-Manpower_Roster_Optimisation_-_Assignment.pdf), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L109), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L110), [chat, 3 Nov](../archive/campus-iit-guwahati-placements/2026-11.jsonl#L111)</sub>
