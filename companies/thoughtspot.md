# ThoughtSpot

**12 questions** · 7 drives · latest 4 Nov 2026 · [7 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [DP](../topics/dp.md) 4 · [Math](../topics/math.md) 4 · [Recursion/Backtracking](../topics/recursion-backtracking.md) 3 · [Graphs](../topics/graphs.md) 3 · [Greedy](../topics/greedy.md) 1 · [Sorting](../topics/sorting.md) 1 · [OA Format](../topics/oa-format.md) 1 · [Binary Search](../topics/binary-search.md) 1 · +1 more  
**Seen at:** IIT BHU, IIT Guwahati, IIT Roorkee

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-04 · IIT BHU · FTE](#2026-11-04--iit-bhu--fte)
  - [Count ways to choose k pairs with distinct a, b and no equal diagonal differences](#q1-count-ways-to-choose-k-pairs-with-distinct-a-b-and-no-equal-diagonal-differences)
  - [Simple BFS problem](#q2-simple-bfs-problem)
  - [Max constant speed path from node 0 to n-1](#q3-max-constant-speed-path-from-node-0-to-n-1)
- [2026-11-03 · IIT Roorkee · FTE](#2026-11-03--iit-roorkee--fte)
  - [Shortest path with constrained edge relaxations](#q1-shortest-path-with-constrained-edge-relaxations)
  - [Array transformation by removing two elements](#q2-array-transformation-by-removing-two-elements)
  - [Minimum operations to make x equal to y](#q3-minimum-operations-to-make-x-equal-to-y)
- [2026-10-30 · IIT Guwahati · FTE](#2026-10-30--iit-guwahati--fte)
  - [Coupled recurrence relations F, G, H](#q1-coupled-recurrence-relations-f-g-h)
- [2026-10-30 · IIT BHU · FTE](#2026-10-30--iit-bhu--fte)
  - [N-Queens](#q1-n-queens)
- [2026-10-27 · IIT Guwahati · FTE](#2026-10-27--iit-guwahati--fte)
  - [Nth number with digit sum x](#q1-nth-number-with-digit-sum-x)
  - [Count permutations where Alice wins chocolate trays game](#q2-count-permutations-where-alice-wins-chocolate-trays-game)
- [2026-10-26 · IIT BHU · FTE](#2026-10-26--iit-bhu--fte)
  - [Minimum Files to Change for Protection](#q1-minimum-files-to-change-for-protection)
- [2026-10-25 · IIT Guwahati · FTE](#2026-10-25--iit-guwahati--fte)
  - [ThoughtSpot OA pattern](#q1-thoughtspot-oa-pattern)

</details>

---

## 2026-11-04 · IIT BHU · FTE

### Q1. Count ways to choose k pairs with distinct a, b and no equal diagonal differences

Given n, k. Find the number of ways of choosing k pairs (a, b) with 0 <= a, b < n. Every a has to be unique across all pairs, and the same for b. There should not be any 2 pairs such that abs(a1 - a2) = abs(b1 - b2).

<sub>Topics: DP, Math, Recursion/Backtracking · Same idea: [LeetCode 52. N-Queens II](https://leetcode.com/problems/n-queens-ii/) (Hard), unique rows/columns, no equal diagonal differences · Source: [chat, 4 Nov](../archive/thoughtspot-oa/2026-11.jsonl#L9)</sub>

### Q2. Simple BFS problem

A simple BFS problem. The poster did not give the statement.

<sub>Topics: Graphs · Source: [chat, 4 Nov](../archive/thoughtspot-oa/2026-11.jsonl#L9)</sub>

### Q3. Max constant speed path from node 0 to n-1

An MST variant. Find the maximum constant speed at which you can travel from node 0 to node n - 1. You can revisit any node any number of times. Edges have a weight (speed).

<sub>Topics: Graphs, Binary Search · Same idea: [LeetCode 1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) (Medium), minimize the maximum edge on path; MST/bottleneck · Source: [chat, 4 Nov](../archive/thoughtspot-oa/2026-11.jsonl#L9)</sub>

## 2026-11-03 · IIT Roorkee · FTE

### Q1. Shortest path with constrained edge relaxations

Given a weighted undirected graph and two vertices s and t, find the minimum shortest-path distance between them after at most k relaxations.

In one relaxation, an edge of weight w can be changed to ceil(w/2). Two relaxations cannot be performed consecutively; there must be at least one gap between them.

<sub>Topics: Graphs · Same idea: [LeetCode 787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Medium), shortest path with limited number of special steps · Source: [chat, 3 Nov](../archive/campus-iit-roorkee-placements/2026-11.jsonl#L133)</sub>

### Q2. Array transformation by removing two elements

Given an array a of size n >= 3 and an array b of size n-2, remove exactly two elements from a and add the same positive integer k to all remaining elements to obtain b.

Find the minimum possible value of k.

<sub>Topics: Arrays · Source: [chat, 3 Nov](../archive/campus-iit-roorkee-placements/2026-11.jsonl#L133)</sub>

### Q3. Minimum operations to make x equal to y

Given two integers x and y, find the minimum number of operations required to make x equal to y.

In each operation, you can:
- Divide x by 11 or 5, if perfectly divisible.
- Increment x by 1.
- Decrement x by 1.

The problem is to be solved using Dynamic Programming.

<sub>Topics: DP · Same idea: [LeetCode 991. Broken Calculator](https://leetcode.com/problems/broken-calculator/) (Medium), min operations transforming x to y with divide/inc/dec · Source: [chat, 3 Nov](../archive/campus-iit-roorkee-placements/2026-11.jsonl#L133)</sub>

## 2026-10-30 · IIT Guwahati · FTE

### Q1. Coupled recurrence relations F, G, H

You are given integers a, b, c, d, e, f, and n. Three sequences F, G, and H are defined by:

```
F(n) = a × F(n − 1) + b × G(n − 2)
G(n) = c × G(n − 1) + d × H(n − 2)
H(n) = e × H(n − 1) + f × F(n − 2)
```

The initial values required to calculate the three sequences are also given. Find F(n) modulo 10^9 + 7.

Input: seven integers a, b, c, d, e, f, n, followed by the initial values required.

Output: print F(n) modulo 1,000,000,007.

Constraints: 0 ≤ n ≤ 10^9. The constraints on the coefficients and initial values are as specified in the original problem (not given).

<sub>Topics: Math, DP · Same idea: [LeetCode 1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) (Easy), linear recurrence, solvable by matrix exponentiation · Source: [Thoughtspot_IIT_Guwahati_Problem_Statements.pdf](../archive/files/16264-Thoughtspot_IIT_Guwahati_Problem_Statements.pdf)</sub>

## 2026-10-30 · IIT BHU · FTE

### Q1. N-Queens

The poster only said the ThoughtSpot OA at IIT BHU had the N-Queens question. Full statement not given.

<sub>Topics: Recursion/Backtracking · Similar: [LeetCode 51. N-Queens](https://leetcode.com/problems/n-queens/) (Hard) · Source: [chat, 30 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L666)</sub>

## 2026-10-27 · IIT Guwahati · FTE

### Q1. Nth number with digit sum x

Given n and x, find the nth number of the sequence of numbers whose sum of digits is x. Example: for x = 5 the sequence is 5, 14, 23, 32, 41, 50, 104, ...

(Poster recalled this only roughly; constraints not given.)

<sub>Topics: DP, Math · Source: [chat, 27 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L23), [chat, 27 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L28), [chat, 28 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L37)</sub>

### Q2. Count permutations where Alice wins chocolate trays game

Given an array where each number represents the number of chocolates in a tray. Alice and Bob take turns, Alice first. In one move a player can pick any number of chocolates from the tray at the top. If the tray becomes empty it is discarded and the next tray comes at the top. The one who picks the last chocolate from the last tray wins. Find the total number of permutations of the given array that ensure Alice always wins (both play optimally).

Example:
```
Input: [1,2,1]
Output: 2
```
Permutations: (2,1,1) Alice wins (picks 2, Bob picks 1 from next tray, Alice picks 1 and wins); (1,1,2) Alice wins; (1,2,1) Alice loses if both play optimally.

<sub>Topics: Math, Recursion/Backtracking · Same idea: [LeetCode 292. Nim Game](https://leetcode.com/problems/nim-game/) (Easy), impartial game winning-position analysis · Source: [chat, 27 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L23), [chat, 27 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L28), [chat, 28 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L37) · Also asked at: IIT Guwahati (2026-10-30)</sub>

## 2026-10-26 · IIT BHU · FTE

### Q1. Minimum Files to Change for Protection

There are n files stored in a system, where the size of the i-th file is fileSize[i]. To protect the files from getting hacked, the minimum size of the i-th file should be minSize[i]. All files must be protected. To do so, the contents of some files can be transferred to another such that the total number of bytes remains the same. Find the minimum number of files whose size must be changed such that all files become protected. If it is not possible to protect all the files, return -1.

<sub>Topics: Greedy, Sorting · Source: [chat, 26 Oct](../archive/inter-nit/2026-10.jsonl#L2454)</sub>

## 2026-10-25 · IIT Guwahati · FTE

### Q1. ThoughtSpot OA pattern

The OA had 3 DSA questions. Details not given.

<sub>Topics: OA Format · Source: [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L119) · Also asked at: IIT Guwahati (2026-10-25), IIT BHU ×2 (last 2026-11-02)</sub>
