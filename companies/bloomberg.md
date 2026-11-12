# Bloomberg

**2 questions** · 2 drives · latest 11 Nov 2026 · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 1 · [SQL](../topics/sql.md) 1 · [Python & Pandas](../topics/python-pandas.md) 1 · [Graphs](../topics/graphs.md) 1 · [Hashing](../topics/hashing.md) 1 · [Trees](../topics/trees.md) 1  
**Seen at:** IIT BHU

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-11 · IIT BHU · FTE · Interview](#2026-11-11--iit-bhu--fte--interview)
  - [Bloomberg interview rounds overview](#q1-bloomberg-interview-rounds-overview)
- [2026-11-11 · IIT BHU · FTE](#2026-11-11--iit-bhu--fte)
  - [Sync engine: queries affected by writes](#q1-sync-engine-queries-affected-by-writes)

</details>

---

## 2026-11-11 · IIT BHU · FTE · Interview

### Q1. Bloomberg interview rounds overview

Reported (second-hand, from a Glassdoor poster) rounds:

- Round 1 (Technical): Core programming and data manipulation, such as writing Python or PySpark code to process CSV files, basic-to-intermediate SQL queries, and project architecture discussions.
- Round 2 (Deep Dive / Tech): In-depth evaluation of past projects, big data concepts, and domain-specific problem solving (e.g., GCP, machine learning pipelines, or data quality).
- Round 3 (Managerial / Scenario): Scenario-based troubleshooting and technical leadership or system design questions.
- HR / Compensation Discussion: Some candidates report friction or conservative compensation offers during final negotiations, so align salary expectations early.

<sub>Topics: OA Format, SQL, Python & Pandas · Source: [chat, 11 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L342)</sub>

## 2026-11-11 · IIT BHU · FTE

### Q1. Sync engine: queries affected by writes

Variant of a Bloomberg OA question ("sync engine"), as remembered.

Input format:
- First line has 2 integers `n`, `q`.
- Then `n` query blocks follow (ids 1 to n in input order). Each block is: a line with the table name, a line with integer `T` (the number of nodes in the condition tree), then `T` lines describing nodes 1 to T, where node 1 is the root.
- Each node line is one of:
  - `AND k c1 c2 ...`
  - `OR k c1 c2 ...`
  - `COND column= value`
- Then `q` write blocks follow. Each starts with a line holding the write type (INSERT, DELETE, UPDATE) and table name, followed by a row: an integer `c` followed by `c` lines of `column value`.

Output: print `q` lines. Line `i` contains the ids of the queries affected by the i-th write, in increasing order, space separated. If no query is affected, print `-1`.

The exact semantics of when a write affects a query are not given.

<sub>Topics: Graphs, Hashing, Trees · Source: [chat, 11 Nov](../archive/campus-mnnit-allahabad-placements/2026-11.jsonl#L197)</sub>
