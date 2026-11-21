# Axtria

**2 questions** · 2 drives · latest 20 Nov 2026 · [1 practice problem](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 1 · [DP](../topics/dp.md) 1 · [Math](../topics/math.md) 1 · [Arrays](../topics/arrays.md) 1  
**Seen at:** IIT BHU, IIT Delhi, IIT Kanpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-20 · Unknown · FTE](#2026-11-20--unknown--fte)
  - [Highest partition score under a block cost ceiling](#q1-highest-partition-score-under-a-block-cost-ceiling)
- [2026-10-28 · IIT Kanpur · FTE](#2026-10-28--iit-kanpur--fte)
  - [Axtria OA pattern](#q1-axtria-oa-pattern)

</details>

---

## 2026-11-20 · Unknown · FTE

### Q1. Highest partition score under a block cost ceiling

You are given an integer array nums of length n, an integer k and an integer threshold.

Split nums into at most k contiguous, non-empty blocks so that every element belongs to exactly one block.

For a block S, its cost is

```
cost(S) = (max(S) - min(S))^2 + (sum of the elements of S)
```

A split is valid only when no block has a cost strictly greater than threshold. Note that elements may be negative, so a cost may be negative as well.

The score of a valid split is

```
score = the sum, over all blocks S, of gcd(len(S), cost(S))
```

where gcd(a, b) is the greatest common divisor of |a| and |b|, with gcd(a, 0) = |a|.

Return the largest score achievable by any valid split into at most k blocks. If no valid split exists, return -1.

Function description: Complete the function maxPartitionScore, which takes the array nums, the integer k and the integer threshold and returns the largest achievable score, or -1.

Input Format:
The first line contains three integers n, k and threshold.
The second line contains n space-separated integers, the array nums.

Output Format:
Print one integer: the largest achievable score, or -1 if there is no valid split.

Constraints:
```
1 <= k <= n <= 60
-10000 <= nums[i] <= 10000
-100000 <= threshold <= 1000000000
```

Sample Input 1:
```
6 3 12
6 6 6 6 6 6
```
Sample Output 1:
```
6
```
Explanation: Every block here has max = min, so its cost is just its sum. A block of three sixes costs 18, which is above the ceiling of 12, so no block may hold three or more elements. Six elements in at most three blocks therefore forces three blocks of two. Each block of two costs 12, which is allowed, and gcd(2, 12) = 2. The score is 2 + 2 + 2 = 6.

Sample Input 2:
```
3 1 9
9 9 9
```
Sample Output 2:
```
-1
```
Explanation: With k = 1 the only split is the whole array as one block. Its cost is (9 - 9)^2 + 27 = 27, which is greater than the ceiling of 9, so there is no valid split at all.

<sub>Topics: DP, Math, Arrays · Same idea: [LeetCode 410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) (Hard), DP over contiguous partitions into at most k blocks · Source: [chat, 20 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L622)</sub>

## 2026-10-28 · IIT Kanpur · FTE

### Q1. Axtria OA pattern

Mostly MCQs on aptitude, C++, MS Word and MS PowerPoint. Aptitude has pattern questions, English grammar etc. Total of 75 questions, drawn from a shuffled pool (not the previously repeated ones).

<sub>Topics: OA Format · Source: [chat, 28 Oct](../archive/campus-iit-kanpur-placements/2026-10.jsonl#L50) · Also asked at: IIT BHU (2026-11-14), IIT Delhi (2026-11-15)</sub>
