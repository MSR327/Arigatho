# NPCI

**5 questions** · 5 drives · latest 4 Nov 2026 · [1 practice problem](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 4 · [Graphs](../topics/graphs.md) 1 · [Greedy](../topics/greedy.md) 1 · [Aptitude](../topics/aptitude.md) 1 · [Arrays](../topics/arrays.md) 1  
**Seen at:** IIT BHU, IIT Bombay, IIT Jodhpur, IIT Kanpur, VNIT Nagpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-04 · VNIT Nagpur · FTE · AI · Other round](#2026-11-04--vnit-nagpur--fte--ai--other-round)
  - [NPCI AI round contents](#q1-npci-ai-round-contents)
- [2026-11-04 · IIT Kanpur · FTE](#2026-11-04--iit-kanpur--fte)
  - [NPCI AI round: traverse and modify array](#q1-npci-ai-round-traverse-and-modify-array)
- [2026-11-04 · IIT Bombay · FTE](#2026-11-04--iit-bombay--fte)
  - [NPCI OA pattern](#q1-npci-oa-pattern)
- [2026-10-23 · IIT Jodhpur · FTE](#2026-10-23--iit-jodhpur--fte)
  - [NPCI OA aptitude round](#q1-npci-oa-aptitude-round)
- [2026-10-18 · IIT BHU · FTE](#2026-10-18--iit-bhu--fte)
  - [Rogue Packet Filters](#q1-rogue-packet-filters)

</details>

---

## 2026-11-04 · VNIT Nagpur · FTE · AI · Other round

### Q1. NPCI AI round contents

The AI round asks a data science related coding question and some MCQs on core subjects. The exact questions were not shared.

<sub>Topics: OA Format · Source: [chat, 4 Nov](../archive/campus-iit-patna-placements/2026-11.jsonl#L14)</sub>

## 2026-11-04 · IIT Kanpur · FTE

### Q1. NPCI AI round: traverse and modify array

The poster said the NPCI AI round was very easy: they had to traverse an array and modify it with a little logic. The exact problem statement was not shared.

<sub>Topics: Arrays, OA Format · Source: [chat, 4 Nov](../archive/campus-iit-kanpur-placements/2026-11.jsonl#L83)</sub>

## 2026-11-04 · IIT Bombay · FTE

### Q1. NPCI OA pattern

- Aptitude: 30 questions
- Coding: 2 questions
- Vibe coding round

All rounds were eliminative.

<sub>Topics: OA Format · Source: [chat, 4 Nov](../archive/campus-iit-bhubaneswar-placements/2026-11.jsonl#L23)</sub>

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

<sub>Topics: Graphs, Greedy · Same idea: [LeetCode 2360. Longest Cycle in a Graph](https://leetcode.com/problems/longest-cycle-in-a-graph/) (Hard), find cycles in functional graph · Source: [chat, 18 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L315), [chat, 18 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L317)</sub>
