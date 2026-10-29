# Unknown

**7 questions** · 4 drives · latest 27 Oct 2026 · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 3 · [Strings](../topics/strings.md) 1 · [Math](../topics/math.md) 1 · [Trees](../topics/trees.md) 1 · [Recursion/Backtracking](../topics/recursion-backtracking.md) 1 · [Graphs](../topics/graphs.md) 1 · [DP](../topics/dp.md) 1 · [Bit Manipulation](../topics/bit-manipulation.md) 1 · +3 more  
**Seen at:** IIT BHU, IIT Bombay, IIT Delhi, IIT Hyderabad

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-27 · IIT Hyderabad · FTE](#2026-10-27--iit-hyderabad--fte)
  - [IDFC First Bank OA pattern](#q1-idfc-first-bank-oa-pattern)
- [2026-10-27 · IIT BHU · FTE](#2026-10-27--iit-bhu--fte)
  - [MCQ round format](#q1-mcq-round-format)
- [2026-10-25 · IIT Delhi · FTE](#2026-10-25--iit-delhi--fte)
  - [ASCII digit-sum of string characters](#q1-ascii-digit-sum-of-string-characters)
  - [Binary tree alternating subtree sums](#q2-binary-tree-alternating-subtree-sums)
  - [Grid travel with work and 8-hour days (Olly)](#q3-grid-travel-with-work-and-8-hour-days-olly)
- [2026-10-18 · IIT Bombay · FTE](#2026-10-18--iit-bombay--fte)
  - [Sony Japan OA format](#q1-sony-japan-oa-format)
  - [Unique elements up to the kth element](#q2-unique-elements-up-to-the-kth-element)

</details>

---

## 2026-10-27 · IIT Hyderabad · FTE

### Q1. IDFC First Bank OA pattern

The IDFC First Bank OA had pseudocode questions and code output questions. (No further details given.)

<sub>Topics: OA Format, Code Output (C/C++/Java/Python) · Source: [chat, 27 Oct](../archive/campus-iit-hyderabad-placements/2026-10.jsonl#L38)</sub>

## 2026-10-27 · IIT BHU · FTE

### Q1. MCQ round format

The process has 2 rounds. The MCQ round had 16 MCQs in 1 hour, on probability, physics and CS fundamentals. The company is not named in the message.

<sub>Topics: OA Format · Source: [chat, 27 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L21)</sub>

## 2026-10-25 · IIT Delhi · FTE

### Q1. ASCII digit-sum of string characters

Given a single string (may contain lowercase, uppercase, special characters and spaces), convert every character to its ASCII value and pass each value to a function that computes the sum of its digits. Process every character, including spaces (so the whole line must be read, e.g. with `getline()` in C++, not `cin >> string`). No C++ boilerplate was provided for this problem. Exact output format and examples were not given.

<sub>Topics: Strings, Math · Source: [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L112), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L113), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L114), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L115), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L116)</sub>

### Q2. Binary tree alternating subtree sums

Given a root node data value and a list of (position string, value) pairs, where the position is a path of `L`/`R` moves from the root, build the binary tree.

```
10
LL   2
LRL  3
L    4
R    6
```

For every node with exactly two children (special node): compute the sum of values in its left subtree and in its right subtree. If the two sums have opposite parity (one even, one odd), add the node's data value to a global answer. The recursive function should return the subtree sum so the parent can do the same check.

The exact output and constraints were not given.

<sub>Topics: Trees, Recursion/Backtracking · Source: [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L112), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L113), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L114), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L115), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L116)</sub>

### Q3. Grid travel with work and 8-hour days (Olly)

Olly works on an m x n grid, starting at (0, 0). There are several locations with work to do, each with a number of hours required. She moves in the four cardinal directions, and each unit move takes 2 hours, so travel time between (x1,y1) and (x2,y2) is 2 x (|x1-x2| + |y1-y2|).

She must visit every work location exactly once, with no revisits, and need not return to (0,0). The order is her choice; the goal is minimum total time (shortest Hamiltonian path from a fixed start).

She works at most 8 hours per day, spent on either travelling or working. If there is work at (0,0), it must be done first. When the 8-hour day ends mid-travel, she stops at her current position and continues the next day. When it ends mid-work, she stops the current work and continues it the next day.

Edge cases noted: work at the start, zero-work locations, travel or work exceeding 8 hours, day ending exactly at 8 hours.

Suggested approach: bitmask DP dp[mask][i], then simulate the days. A poster says an MST approach passed all test cases except 4.

The statement is truncated: the exact output and constraints were not given.

<sub>Topics: Graphs, DP, Bit Manipulation · Source: [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L112), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L113), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L114), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L115), [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L116)</sub>

## 2026-10-18 · IIT Bombay · FTE

### Q1. Sony Japan OA format

The Sony Japan OA had 1 DSA question and 30 MCQs. The DSA question was fairly easy, and the 30 MCQs were syntax based and very doable. Different candidates got different coding questions.

<sub>Topics: OA Format · Source: [chat, 18 Oct](../archive/campus-iit-bombay-placements/2026-10.jsonl#L139), [chat, 18 Oct](../archive/campus-iit-bombay-placements/2026-10.jsonl#L140), [chat, 18 Oct](../archive/campus-iit-bombay-placements/2026-10.jsonl#L142), [chat, 19 Oct](../archive/campus-iit-bombay-placements/2026-10.jsonl#L144)</sub>

### Q2. Unique elements up to the kth element

Count the number of unique elements encountered till the kth element of an array. (The poster solved it in Python using a set. Exact constraints and examples were not given.)

<sub>Topics: Arrays, Hashing · Source: [chat, 18 Oct](../archive/campus-iit-bombay-placements/2026-10.jsonl#L139), [chat, 18 Oct](../archive/campus-iit-bombay-placements/2026-10.jsonl#L140), [chat, 18 Oct](../archive/campus-iit-bombay-placements/2026-10.jsonl#L142), [chat, 19 Oct](../archive/campus-iit-bombay-placements/2026-10.jsonl#L144)</sub>
