# Honda

**14 questions** from 4 OA drives · seen at IIT Delhi, IIT Hyderabad, IIT Madras, VIT Vellore · latest 2026-10-17

**Topics:** [Arrays](../topics/arrays.md) (6) · [Math](../topics/math.md) (4) · [DP](../topics/dp.md) (4) · [Hashing](../topics/hashing.md) (2) · [Graphs](../topics/graphs.md) (2) · [Bit Manipulation](../topics/bit-manipulation.md) (2) · [Two Pointers](../topics/two-pointers.md) (1) · [Sorting](../topics/sorting.md) (1) · [Other](../topics/other.md) (1)

**LeetCode matches:** 3 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-17 · IIT Madras · FTE](#2026-10-17--iit-madras--fte) · 2 questions
- [2026-10-15 · IIT Delhi · FTE](#2026-10-15--iit-delhi--fte) · 4 questions
- [2026-10-09 · VIT Vellore · FTE](#2026-10-09--vit-vellore--fte) · 4 questions
- [2026-10-09 · IIT Hyderabad · FTE](#2026-10-09--iit-hyderabad--fte) · 4 questions

[← all companies](../README.md#companies)

---

## 2026-10-17 · IIT Madras · FTE

### Q1. Square with minimum area enclosing k points

Find the square with minimum area enclosing k points among given n points. Reference link: https://stackoverflow.com/questions/30951045/square-with-minimum-area-enclosing-k-points-among-given-n-points

<sub>Topics: Arrays, Sorting · Source: [chat, 17 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L111)</sub>

### Q2. FactSet photo album

Problem from fastprep.io: https://www.fastprep.io/problems/factset-photo-album (statement not given in the message).

<sub>Topics: Other · Source: [chat, 17 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L111)</sub>

## 2026-10-15 · IIT Delhi · FTE

### Q1. Bitwise Recurrence

A sequence is defined using three initial values F0, F1, F2. Subsequent terms use bitwise OR and XOR. The recurrence visible in the screenshot:

F_i = (F_{i-1} | F_{i-2}) ^ F_{i-3}

Given a, b, c and n, return F_n.

Function signature (C):
```
long bitwiseRecurrence(long a, long b, long c, long n)
```
Examples:
- a = 4, b = 1, c = 10, n = 4 → 14
- a = 3, b = 2, c = 5, n = 3 → 2

Note: the second example appears inconsistent with the recurrence as readable.

<sub>Topics: Bit Manipulation, Math · Source: [chat, 15 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L191)</sub>

### Q2. Maximum Gross Value of Any Valid Triple

Given an integer array arr of length n, select a valid triple of indices to maximize the gross value, calculated using sums of array segments: the sum of the selected segment, the sum of elements before it, and the sum of elements after it. Empty segments contribute zero. Return the maximum possible gross value.

Function signature (C):
```
long getMaximumGrossValue(int arr_count, int* arr)
```
Examples:
- arr = [-1, 1, -2, -2] → 6
- arr = [4, -8, 2, -10, 3, -20] → 43

The exact gross value formula is not fully given.

<sub>Topics: Arrays, DP · Source: [chat, 15 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L191)</sub>

### Q3. Bitwise Recurrence

A sequence is defined by three starting values F0 = a, F1 = b, F2 = c. Each later term is F_i = (F_{i-1} | F_{i-2}) ^ F_{i-3}, using bitwise OR and XOR. Given a, b, c and n, return F_n. Function signature (C): long bitwiseRecurrence(long a, long b, long c, long n). Examples: a=4, b=1, c=10, n=4 -> 14; a=3, b=2, c=5, n=3 -> 2. (The poster notes the second example looks inconsistent with the recurrence as read from the screenshot.) This was the OA at IIT Delhi last year.

<sub>Topics: Bit Manipulation, Math · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L1304)</sub>

### Q4. Maximum Gross Value of Any Valid Triple

You are given an integer array arr of length n. Choose a valid triple of indices to maximize the gross value. The gross value is computed from three sums: the sum of the selected segment, the sum of the elements before it, and the sum of the elements after it. Empty segments count as zero. Return the largest possible gross value. Function signature (C): long getMaximumGrossValue(int arr_count, int* arr). Examples: arr = [-1, 1, -2, -2] -> 6; arr = [4, -8, 2, -10, 3, -20] -> 4.

<sub>Topics: Arrays, DP · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L1304)</sub>

## 2026-10-09 · VIT Vellore · FTE

### Q1. Maximum GCD of Any Pair

Given an integer n (n ≥ 2), consider every pair of distinct integers (a, b) with 1 ≤ a &lt; b ≤ n. Return the maximum value of gcd(a, b) over all such pairs.

Example  
Input: n = 5  
Pairs: (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)  
Output: 2, from the pair (2, 4)

<sub>Topics: Math · Source: [chat, 9 Oct](../archive/inter-iit/2026-10.jsonl#L292)</sub>

### Q2. Unique Pairs with Target Sum

Given an integer array nums and an integer target, return all unique pairs (a, b) from the array such that a + b = target.  
- Each pair uses two different indices.  
- Pairs are unordered, so (a, b) and (b, a) count as the same pair.  
- Duplicate values in the array must not produce duplicate pairs in the output.

Example  
Input: nums = [1, 5, 7, -1, 5], target = 6  
Output: [(1, 5), (7, -1)], where (1, 5) appears only once even though 5 occurs twice

<sub>Topics: Arrays, Hashing, Two Pointers · Source: [chat, 9 Oct](../archive/inter-iit/2026-10.jsonl#L292)</sub>

### Q3. Maximum Jumps to Reach the Last Index

You are given an array nums of length n and an integer limit. You start at index 0 and want to reach index n - 1.

From index i, you may jump to any index j that satisfies both conditions:  
- i &lt; j (you can only jump forward)  
- |nums[j] - nums[i]| ≤ limit

Return the maximum number of jumps you can make to reach index n - 1. If the last index cannot be reached, return -1.

Example  
Input: nums = [1, 3, 6, 4, 1, 2], limit = 2  
Output: 3, using the path 0 → 1 → 3 → 5 (values 1 → 3 → 4 → 2)

This is the same problem as LeetCode 2770, "Maximum Number of Jumps to Reach the Last Index."

<sub>Topics: DP, Arrays · Similar: [LeetCode 2770. Maximum Number of Jumps to Reach the Last Index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) (Medium) · Source: [chat, 9 Oct](../archive/inter-iit/2026-10.jsonl#L292)</sub>

### Q4. Remove Suspicious Nodes from a Directed Graph

You are given n nodes labeled 0 to n - 1, a list of directed edges edges where [a, b] means node a points to node b, and a node k that is suspicious.

Suspicious set: node k, plus every node reachable from k (directly or indirectly) by following the edges.

Rule:  
- If no node outside the suspicious set has an edge into any node inside it, remove the entire suspicious set.  
- If at least one outside node points into the suspicious set, removing it is not allowed, so no nodes are removed.

Return the remain[ing nodes] ... (message text was cut off here in the source)

<sub>Topics: Graphs · Similar: [LeetCode 3310. Remove Methods From Project](https://leetcode.com/problems/remove-methods-from-project/) (Medium) · Source: [chat, 9 Oct](../archive/inter-iit/2026-10.jsonl#L292)</sub>

## 2026-10-09 · IIT Hyderabad · FTE

### Q1. Maximum GCD of any pair

Given an integer n (n ≥ 2), consider every pair of distinct integers (a, b) with 1 ≤ a < b ≤ n. Return the maximum value of gcd(a, b) over all such pairs.

Example

```
Input: n = 5
Pairs: (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)
Output: 2, from the pair (2, 4)
```

<sub>Topics: Math · Source: [chat, 9 Oct](../archive/campus-iit-hyderabad-placements/2026-10.jsonl#L153)</sub>

### Q2. Unique pairs with target sum

Given an integer array nums and an integer target, return all unique pairs (a, b) from the array such that a + b = target.

- Each pair uses two different indices.
- Pairs are unordered, so (a, b) and (b, a) count as the same pair.
- Duplicate values in the array must not produce duplicate pairs in the output.

Example

```
Input: nums = [1, 5, 7, -1, 5], target = 6
Output: [(1, 5), (7, -1)]
```
(1, 5) appears only once even though 5 occurs twice.

<sub>Topics: Hashing, Arrays · Source: [chat, 9 Oct](../archive/campus-iit-hyderabad-placements/2026-10.jsonl#L153)</sub>

### Q3. Maximum jumps to reach the last stone

You are given an array nums of length n and an integer limit. You start at index 0 and want to reach index n - 1.

From index i, you may jump to any index j that satisfies both conditions:

- i < j (you can only jump forward)
- |nums[j] - nums[i]| ≤ limit

Return the maximum number of jumps you can make to reach index n - 1. If the last index cannot be reached, return -1.

Example

```
Input: nums = [1, 3, 6, 4, 1, 2], limit = 2
Output: 3, using the path 0 → 1 → 3 → 5 (values 1 → 3 → 4 → 2)
```

The poster notes this is the same as LeetCode 2770.

<sub>Topics: DP · Similar: [LeetCode 2770. Maximum Number of Jumps to Reach the Last Index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) (Medium) · Source: [chat, 9 Oct](../archive/campus-iit-hyderabad-placements/2026-10.jsonl#L153)</sub>

### Q4. Remove suspicious nodes from a directed graph

You are given n nodes labeled 0 to n - 1, a list of directed edges edges where [a, b] means node a points to node b, and a node k that is suspicious.

Suspicious set: node k, plus every node reachable from k (directly or indirectly) by following the edges.

Rule:

- If no node outside the suspicious set has an edge into any node inside it, remove the entire suspicious set.
- If at least one outside node points into the suspicious set, removing it is not allowed, so no nodes are removed.

Return the remain... (the message is cut off here; the rest of the statement is missing).

<sub>Topics: Graphs · Source: [chat, 9 Oct](../archive/campus-iit-hyderabad-placements/2026-10.jsonl#L153)</sub>
