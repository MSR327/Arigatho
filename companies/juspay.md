# Juspay

**4 questions** from 2 OA drives · seen at IIIT Allahabad, IIT BHU, MNNIT Allahabad · latest 2026-10-24

**Topics:** [Other](../topics/other.md) (3) · [Trees](../topics/trees.md) (1) · [Hashing](../topics/hashing.md) (1)

**Drives:**

- [2026-10-24 · IIT BHU · Unknown](#2026-10-24--iit-bhu--unknown) · 3 questions
- [2026-10-18 · IIIT Allahabad · FTE](#2026-10-18--iiit-allahabad--fte) · 1 question

[← all companies](../README.md#companies)

---

## 2026-10-24 · IIT BHU · Unknown

### Q1. Corporate Restructuring

Past Juspay OA question recommended for practice. The poster says Juspay OA questions repeat every year, so 1 of the 3 questions will be a repeat. Only the title "Corporate Restructuring" was shared, with no statement.

<sub>Topics: Other · Source: [chat, 24 Oct](../archive/inter-nit/2026-10.jsonl#L2244)</sub>

### Q2. Power Grid Management

Past Juspay OA question recommended for practice (Juspay reportedly repeats 1 of its 3 OA questions each year). Only the title "Power Grid Management" was shared, with no statement.

<sub>Topics: Other · Source: [chat, 24 Oct](../archive/inter-nit/2026-10.jsonl#L2244)</sub>

### Q3. The Magical Sequence

Past Juspay OA question recommended for practice (Juspay reportedly repeats 1 of its 3 OA questions each year). Only the title "The Magical Sequence" was shared, with no statement.

<sub>Topics: Other · Source: [chat, 24 Oct](../archive/inter-nit/2026-10.jsonl#L2244)</sub>

## 2026-10-18 · IIIT Allahabad · FTE

### Q1. Sync Engine

You are building a Sync Engine for applications that maintain an offline copy of server data on users' devices.

The server contains a single table called orders. Each client stores a query (filter), and its local copy must contain exactly the rows satisfying that query.

Whenever the server's orders table changes, the Sync Engine must determine which clients could have an outdated copy and notify them.

Client Queries  
There are n client queries, numbered from 1 to n. These queries remain unchanged throughout the input.  
Each query is equivalent to:  
SELECT * FROM orders WHERE &lt;expression>  
The expression is represented as a tree rather than SQL text.

1. COND Node: A leaf condition compares the value of one column with a fixed value. Examples: amount > 500, status = "completed", quantity &lt;= 10. The allowed comparison operators are: =, >, &lt;, >=, &lt;=  
2. AND Node: An AND node evaluates to true if all of its children evaluate to true.  
3. OR Node: An OR node evaluates to true if at least one of its children evaluates to true.

False Conditions  
A COND condition evaluates to false if:  
- The row does not contain the column being evaluated.  
- The two values being compared have different types.  
For example, comparing amount > 500 against amount = "600" is always false, even though the textual value could represent a number. This type mismatch rule applies to all operators, including =.

Write Operations  
There are q write operations, applied in the given order. Each operation is one of: INSERT, DELETE, UPDATE.  
You are not given the initial contents of the orders table. Each write contains all information about the row(s) affected, and every write must be evaluated independently.

INSERT: An INSERT adds a new row. Notify query i if the new row satisfies query i.  
DELETE: A DELETE removes an existing row. Notify query i if the removed row satisfies query i.  
UPDATE: An UPDATE provid... [message truncated here]

(Pattern: 3 hours, one question.)

<sub>Topics: Trees, Hashing · Source: [chat, 18 Oct](../archive/inter-nit/2026-10.jsonl#L1539), [chat, 18 Oct](../archive/inter-iit/2026-10.jsonl#L560) · Also asked at: MNNIT Allahabad ×2 (last 2026-10-18), IIIT Allahabad ×2 (last 2026-10-23)</sub>
