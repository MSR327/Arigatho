# ThoughtSpot

**5 questions** · 4 drives · latest 30 Oct 2026 · [2 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Math](../topics/math.md) 3 · [DP](../topics/dp.md) 2 · [Greedy](../topics/greedy.md) 1 · [Sorting](../topics/sorting.md) 1 · [OA Format](../topics/oa-format.md) 1 · [Recursion/Backtracking](../topics/recursion-backtracking.md) 1  
**Seen at:** IIT BHU, IIT Guwahati

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-30 · IIT Guwahati · FTE](#2026-10-30--iit-guwahati--fte)
  - [Coupled recurrence relations F, G, H](#q1-coupled-recurrence-relations-f-g-h)
- [2026-10-27 · IIT Guwahati · FTE](#2026-10-27--iit-guwahati--fte)
  - [Nth number with digit sum x](#q1-nth-number-with-digit-sum-x)
  - [Count permutations where Alice wins chocolate trays game](#q2-count-permutations-where-alice-wins-chocolate-trays-game)
- [2026-10-26 · IIT BHU · FTE](#2026-10-26--iit-bhu--fte)
  - [Minimum Files to Change for Protection](#q1-minimum-files-to-change-for-protection)
- [2026-10-25 · IIT Guwahati · FTE](#2026-10-25--iit-guwahati--fte)
  - [ThoughtSpot OA pattern](#q1-thoughtspot-oa-pattern)

</details>

---

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

<sub>Topics: OA Format · Source: [chat, 25 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L119) · Also asked at: IIT Guwahati (2026-10-25), IIT BHU (2026-10-27)</sub>
