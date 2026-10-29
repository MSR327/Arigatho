# NPCI

**2 questions** from 2 OA drives · seen at IIT BHU, IIT Jodhpur · latest 2026-10-23

**Topics:** [Graphs](../topics/graphs.md) (1) · [Greedy](../topics/greedy.md) (1) · [OA Format](../topics/oa-format.md) (1) · [Aptitude](../topics/aptitude.md) (1)

**Drives:**

- [2026-10-23 · IIT Jodhpur · FTE](#2026-10-23--iit-jodhpur--fte) · 1 question
- [2026-10-18 · IIT BHU · FTE](#2026-10-18--iit-bhu--fte) · 1 question

[← all companies](../README.md#companies)

---

## 2026-10-23 · IIT Jodhpur · FTE

### Q1. NPCI OA aptitude round

The first round is a 30-minute aptitude test with 3 subsections and a very high absolute cutoff (possibly 27 correct, i.e. 9x3); over 90% of students couldn't clear it. Each round is eliminatory.

<sub>Topics: OA Format, Aptitude · Source: [chat, 23 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L167)</sub>

## 2026-10-18 · IIT BHU · FTE

### Q1. Rogue Packet Filters

There are N servers. Server i forwards every packet to server a[i] after one second. A packet may start at any server. Installing a filter on server i costs c[i]; a packet is neutralized as soon as it visits a filtered server.

Find the minimum total cost of filters that guarantees every possible packet is eventually neutralized.

Input:
The first line contains N.
The second line contains N costs c[1] ... c[N].
The third line contains N destinations a[1] ... a[N].

Output: Print the minimum total cost.

Constraints:
- 1 <= N <= 200000
- 1 <= c[i] <= 10000
- 1 <= a[i] <= N
- Use a 64-bit integer for the answer.

Hint from poster: functional graph; every cycle needs a filter, so the answer is the sum of the minimum c[i] over all cycles, in O(N).

<sub>Topics: Graphs, Greedy · Source: [chat, 18 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L315), [chat, 18 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L317)</sub>
