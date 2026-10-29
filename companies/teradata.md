# Teradata

**14 questions** · 4 drives · latest 28 Sep 2026 · [9 LeetCode matches](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Graphs](../topics/graphs.md) 4 · [DP](../topics/dp.md) 3 · [Math](../topics/math.md) 2 · [Heaps](../topics/heaps.md) 2 · [Sorting](../topics/sorting.md) 2 · [Strings](../topics/strings.md) 2 · [Arrays](../topics/arrays.md) 2 · [OOP](../topics/oop.md) 2 · +7 more  
**Seen at:** IIT BHU, NIT Warangal

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-09-28 · IIT BHU · FTE](#2026-09-28--iit-bhu--fte)
  - [Standard knapsack DP (sum of power of subsequences)](#q1-standard-knapsack-dp-sum-of-power-of-subsequences)
  - [Subsequences satisfying a sum condition / hire K workers](#q2-subsequences-satisfying-a-sum-condition--hire-k-workers)
  - [Minimum jumps via prime teleportation](#q3-minimum-jumps-via-prime-teleportation)
  - [Minimum Jumps to Reach End via Prime Teleportation](#q4-minimum-jumps-to-reach-end-via-prime-teleportation)
  - [Minimum Cost to Hire K Workers](#q5-minimum-cost-to-hire-k-workers)
- [2026-09-23 · NIT Warangal · Intern · SDE · Interview](#2026-09-23--nit-warangal--intern--sde--interview)
  - [Stock buy and sell with 2 transactions](#q1-stock-buy-and-sell-with-2-transactions)
- [2026-09-21 · Unknown · Intern · SDE Intern · Interview](#2026-09-21--unknown--intern--sde-intern--interview)
  - [Balanced parentheses](#q1-balanced-parentheses)
  - [Stock trading with two transactions](#q2-stock-trading-with-two-transactions)
  - [OOP concepts](#q3-oop-concepts)
  - [Adjacency list vs adjacency matrix](#q4-adjacency-list-vs-adjacency-matrix)
  - [Hash map internals](#q5-hash-map-internals)
  - [Serialize and deserialize a binary tree](#q6-serialize-and-deserialize-a-binary-tree)
  - [Parking lot / payment interface design](#q7-parking-lot--payment-interface-design)
- [2026-09-21 · Unknown · Intern · AI/ML Intern · Other round](#2026-09-21--unknown--intern--aiml-intern--other-round)
  - [AI/ML intern OA and interview overview](#q1-aiml-intern-oa-and-interview-overview)

</details>

---

## 2026-09-28 · IIT BHU · FTE

### Q1. Standard knapsack DP (sum of power of subsequences)

Standard knapsack DP question. The poster later identified it as LeetCode 3082, Find the Sum of the Power of All Subsequences.

The full statement was not shared.

<sub>Topics: DP · Similar: [LeetCode 3082. Find the Sum of the Power of All Subsequences](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/) (Hard) · Source: [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L29), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L30), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L31), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L32), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L33)</sub>

### Q2. Subsequences satisfying a sum condition / hire K workers

Described as basically a replica of "Number of Subsequences That Satisfy the Given Sum Condition". The poster later cited LC 857 (Minimum Cost to Hire K Workers) for this question.

The full statement was not shared.

<sub>Topics: Sorting, Heaps · Similar: [LeetCode 857. Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) (Hard) · Source: [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L29), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L30), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L31), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L32), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L33)</sub>

### Q3. Minimum jumps via prime teleportation

A stone-game-like variation. At each step there are 2 choices: jump to the next element, or, if currently on a prime number, jump to an index whose value is a multiple of (divisible by) that prime. The poster identified it as LC 3629, Minimum Jumps to Reach End via Prime Teleportation.

The exact statement was not shared.

<sub>Topics: Graphs, Math · Similar: [LeetCode 3629. Minimum Jumps to Reach End via Prime Teleportation](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/) (Medium) · Source: [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L29), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L30), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L31), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L32), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L33)</sub>

### Q4. Minimum Jumps to Reach End via Prime Teleportation

(LeetCode 3629) You are given an integer array nums of length n. You start at index 0 and your goal is to reach index n - 1. From any index i you may do one of these operations:  
- Adjacent step: jump to index i + 1 or i - 1, if that index is within bounds.  
- Prime teleportation: if nums[i] is a prime number p, you may jump instantly to any index j != i such that nums[j] % p == 0.  
Return the minimum number of jumps needed to reach index n - 1.

Example 1: nums = [1,2,4,6] -> 2 (step 0->1, nums[1]=2 is prime, teleport to index 3 since 6 % 2 == 0).  
Example 2: nums = [2,3,4,7,9] -> 2 (step 0->1, nums[1]=3 is prime, teleport to index 4 since 9 % 3 == 0).  
Example 3: nums = [4,6,5,8] -> 3 (no useful teleport, so take adjacent steps 0->1->2->3).

Constraints: 1 &lt;= n == nums.length &lt;= 10^5, 1 &lt;= nums[i] &lt;= 10^6.  
Link: https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

<sub>Topics: Graphs, Math · Similar: [LeetCode 3629. Minimum Jumps to Reach End via Prime Teleportation](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/) (Medium) · Source: [chat, 28 Sep](../archive/inter-iit/2026-09.jsonl#L9), [chat, 28 Sep](../archive/inter-nit/2026-09.jsonl#L177), [chat, 28 Sep](../archive/inter-nit/2026-09.jsonl#L80)</sub>

### Q5. Minimum Cost to Hire K Workers

(LeetCode 857) There are n workers. You are given two integer arrays quality and wage, where quality[i] is the quality of the i-th worker and wage[i] is that worker's minimum wage expectation. You want to hire exactly k workers to form a paid group. When you hire a group of k workers, you must pay them by these rules:  
1. Each worker in the group is paid in proportion to their quality compared with the other workers in the group.  
2. Each worker in the group must be paid at least their minimum wage expectation.  
Given k, return the least amount of money needed to form a paid group that meets these conditions. Answers within 10^-5 of the actual answer are accepted.

Example 1: quality = [10,20,5], wage = [70,50,30], k = 2 -> 105.00000 (pay 70 to worker 0 and 35 to worker 2).  
Example 2: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3 -> 30.66667 (pay 4 to worker 0 and 13.33333 each to workers 2 and 3).

Constraints: n == quality.length == wage.length, 1 &lt;= k &lt;= n &lt;= 10^4, 1 &lt;= quality[i], wage[i] &lt;= 10^4.  
Link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

<sub>Topics: Heaps, Greedy, Sorting · Similar: [LeetCode 857. Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) (Hard) · Source: [chat, 28 Sep](../archive/inter-iit/2026-09.jsonl#L9), [chat, 28 Sep](../archive/inter-nit/2026-09.jsonl#L177), [chat, 28 Sep](../archive/inter-nit/2026-09.jsonl#L80)</sub>

## 2026-09-23 · NIT Warangal · Intern · SDE · Interview

### Q1. Stock buy and sell with 2 transactions

Stock buy and sell problem allowing at most 2 transactions (asked in the interview). The poster gave no further details.

<sub>Topics: DP, Arrays · Similar: [LeetCode 123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (Hard) · Source: [chat, 23 Sep](../archive/intern-2027/2026-09.jsonl#L10)</sub>

## 2026-09-21 · Unknown · Intern · SDE Intern · Interview

### Q1. Balanced parentheses

Balanced parentheses problem (check whether a string of brackets is balanced). Only named in a digest; the full statement is not given.

<sub>Topics: Stack/Queue, Strings · Similar: [LeetCode 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) · Source: [chat, 21 Sep](../archive/teradata-oa/2026-09.jsonl#L37)</sub>

### Q2. Stock trading with two transactions

The two-transaction stock-trading problem (maximize profit from buying and selling a stock with at most two transactions). Only named in a digest; constraints and examples are not given.

<sub>Topics: DP, Arrays · Similar: [LeetCode 123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (Hard) · Source: [chat, 21 Sep](../archive/teradata-oa/2026-09.jsonl#L37)</sub>

### Q3. OOP concepts

Object-oriented programming questions were asked. Specific questions are not given.

<sub>Topics: OOP · Source: [chat, 21 Sep](../archive/teradata-oa/2026-09.jsonl#L37)</sub>

### Q4. Adjacency list vs adjacency matrix

Compare adjacency lists versus adjacency matrices for graph representation.

<sub>Topics: Graphs · Source: [chat, 21 Sep](../archive/teradata-oa/2026-09.jsonl#L37)</sub>

### Q5. Hash map internals

Explain how hash maps work internally. Specific sub-questions are not given.

<sub>Topics: Hashing · Source: [chat, 21 Sep](../archive/teradata-oa/2026-09.jsonl#L37)</sub>

### Q6. Serialize and deserialize a binary tree

Design round: binary-tree serialization/deserialization. Only named in a digest; the full statement is not given.

<sub>Topics: Trees, Strings · Similar: [LeetCode 297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (Hard) · Source: [chat, 21 Sep](../archive/teradata-oa/2026-09.jsonl#L37)</sub>

### Q7. Parking lot / payment interface design

Design round exercise: a parking-lot and payment-interface design problem. Details are not given.

<sub>Topics: OOP, Software Engineering · Source: [chat, 21 Sep](../archive/teradata-oa/2026-09.jsonl#L37)</sub>

## 2026-09-21 · Unknown · Intern · AI/ML Intern · Other round

### Q1. AI/ML intern OA and interview overview

The OA had three coding tasks plus a written explanation of the solution. Broad areas were two pointers and graphs. The interviews covered factorial implementations, boundary traversal of a binary tree, project design, and logging and error handling. The writer said ML knowledge was not needed. Exact questions are not given.

<sub>Topics: OA Format, Two Pointers, Graphs · Source: [chat, 21 Sep](../archive/teradata-oa/2026-09.jsonl#L37)</sub>
