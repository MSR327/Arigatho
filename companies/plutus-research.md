# Plutus Research

**12 questions** from 2 OA drives · seen at IIT Guwahati, IIT Kharagpur · latest 2026-10-28

**Topics:** [Greedy](../topics/greedy.md) (4) · [Graphs](../topics/graphs.md) (2) · [Trees](../topics/trees.md) (2) · [DP](../topics/dp.md) (2) · [Strings](../topics/strings.md) (2) · [Binary Search](../topics/binary-search.md) (2) · [Puzzles](../topics/puzzles.md) (2) · [Math](../topics/math.md) (2) · [Arrays](../topics/arrays.md) (2) · [Hashing](../topics/hashing.md) (1)

**LeetCode matches:** 1 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-28 · IIT Kharagpur · FTE](#2026-10-28--iit-kharagpur--fte) · 6 questions
- [2026-10-28 · IIT Guwahati · FTE · Quant](#2026-10-28--iit-guwahati--fte--quant) · 6 questions

[← all companies](../README.md#companies)

---

## 2026-10-28 · IIT Kharagpur · FTE

### Q1. Sum of components after removing each node

Given an undirected graph, compute the sum over all nodes v of f(v), where f(v) = number of connected components after removing v from the graph and keeping the rest intact. This had to be computed for every test case.

Constraints: around 10^5 to 10^6.

(Exact input format not given.)

<sub>Topics: Graphs · Source: [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L38), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L39), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L40), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L42), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L43), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L44)</sub>

### Q2. Min splits so no component has product divisible by 6

Given an undirected tree where each node has a value 1, 2 or 3, find the minimum number of splits needed such that no component has (product of node values) % 6 == 0.

<sub>Topics: Trees, DP · Source: [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L38), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L39), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L40), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L42), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L43), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L44)</sub>

### Q3. Longest common substring across k strings

Given k strings with 2 <= k <= 6, each of length up to 10^7 (poster not sure of this), find the longest common substring (not subsequence) across all the strings and return its length, not the string.

<sub>Topics: Strings, Binary Search, Hashing · Source: [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L38), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L39), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L40), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L42), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L43), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L44)</sub>

### Q4. High-constraint greedy question

A greedy question whose constraints were very high, so DP was not feasible. The poster remembered only that it was greedy; the statement is missing.

<sub>Topics: Greedy · Source: [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L38), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L39), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L40), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L42), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L43), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L44)</sub>

### Q5. ATM withdraw and deposit queries

Simulate an ATM with notes of 20, 50, 100, 200, 500. There are two query types:

- Withdraw: `250 -1 -1 -1 -1 -1`, where the first number is the amount to withdraw.
- Deposit: `-1 1 0 0 1 1`, where -1 marks a deposit and the next 5 numbers are the counts of notes of 20, 50, 100, 200, 500.

Notes can only be extracted from highest to lowest denomination, and you must take a note if it is present. If the amount can be fulfilled, return the count of each note extracted. Otherwise return `-1 -1 -1 -1 -1`. The ATM balance changes only if money is actually extracted.

Example: withdraw 600 when the ATM holds [20:0, 50:1, 100:0, 200:3, 500:1]. Take 500 first, 100 more is needed, but no 100 note is present and the remaining 50 and 20 cannot cover it, so the answer is `-1 -1 -1 -1 -1`.

<sub>Topics: Arrays, Greedy · Similar: [LeetCode 2241. Design an ATM Machine](https://leetcode.com/problems/design-an-atm-machine/) (Medium) · Source: [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L38), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L39), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L40), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L42), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L43), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L44)</sub>

### Q6. Card game with spades then hearts: should you play?

There are 52 cards and each game costs 3 dollars to play. The game ends when you get a spade then a heart. You draw cards without replacement.

- Every spade gives 3 dollars.
- Every heart gives 2 dollars.
- Every club or diamond loses 1 dollar.

Decide whether you should play the game.

<sub>Topics: Math, Puzzles · Source: [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L38), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L39), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L40), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L42), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L43), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L44)</sub>

## 2026-10-28 · IIT Guwahati · FTE · Quant

### Q1. Sum of connected components after removing each node

Given an undirected graph, compute the sum over all nodes v of f(v), where f(v) is the number of connected components after removing v from the graph and keeping the rest intact. Compute this sum for each test case.

Constraints: around 10^5 to 10^6 (exact constraints not remembered).

<sub>Topics: Graphs · Source: [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L10), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L11), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L12), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L13), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L14), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L15)</sub>

### Q2. Minimum splits of tree so no component product divisible by 6

Given an undirected tree where each node has value 1, 2 or 3. Find the minimum number of splits needed such that no component has (product of node values) % 6 == 0.

<sub>Topics: Trees, DP · Source: [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L10), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L11), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L12), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L13), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L14), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L15)</sub>

### Q3. Longest common substring across k strings

Given k strings (2 <= k <= 6), each of length up to 10^7 (poster not sure of this). Find the length of the longest common substring (not subsequence) across all the strings. Return only the length, not the string.

<sub>Topics: Strings, Binary Search · Source: [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L10), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L11), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L12), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L13), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L14), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L15)</sub>

### Q4. High-constraint greedy problem

A greedy problem with very high constraints where DP was not feasible, so greedy was the intended solution. Rest of the statement not remembered.

<sub>Topics: Greedy · Source: [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L10), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L11), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L12), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L13), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L14), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L15)</sub>

### Q5. Card game with spades and hearts: should you play?

There are 52 cards and each game costs 3 dollars to play. The game ends when you get a spade and then a heart. You draw cards without replacement.
- For every spade you get 3 dollars
- For every heart you get 2 dollars
- For clubs/diamonds you lose 1 dollar

Decide whether you should play the game or not.

<sub>Topics: Puzzles, Math · Source: [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L10), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L11), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L12), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L13), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L14), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L15)</sub>

### Q6. ATM withdraw and deposit simulation

Implement an ATM with two types of queries.

Withdraw query: `250 -1 -1 -1 -1 -1` (250 is the amount to withdraw).
Deposit query: `-1 1 0 0 1 1` (the leading -1 means deposit, followed by 5 numbers: the count of notes of 20, 50, 100, 200, 500).

Notes can only be extracted from highest to lowest denomination, and you must extract a note if it is present.

Example: withdraw 600 when the ATM has `[20:0, 50:1, 100:0, 200:3, 500:1]`. Extract 500 first. 100 more is needed, but no 100 note is present and the remaining 50 and 20 cannot fulfill it, so return `-1 -1 -1 -1 -1`.
If the withdrawal can be fulfilled, return the count of each note extracted.
The ATM balance changes only if the money can be, and is actually, extracted.

<sub>Topics: Arrays, Greedy · Source: [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L10), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L11), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L12), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L13), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L14), [chat, 28 Oct](../archive/plutus-research-oa/2026-10.jsonl#L15)</sub>
