# Teradata

**3 questions** · 1 drive · latest 28 Sep 2026 · [3 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Graphs](../topics/graphs.md) 1 · [Math](../topics/math.md) 1 · [Heaps](../topics/heaps.md) 1 · [Greedy](../topics/greedy.md) 1 · [Sorting](../topics/sorting.md) 1 · [DP](../topics/dp.md) 1  
**Seen at:** IIT BHU

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-09-28 · IIT BHU · FTE](#2026-09-28--iit-bhu--fte)
  - [Standard knapsack DP (sum of power of subsequences)](#q1-standard-knapsack-dp-sum-of-power-of-subsequences)
  - [Minimum Jumps to Reach End via Prime Teleportation](#q2-minimum-jumps-to-reach-end-via-prime-teleportation)
  - [Minimum Cost to Hire K Workers](#q3-minimum-cost-to-hire-k-workers)

</details>

---

## 2026-09-28 · IIT BHU · FTE

### Q1. Standard knapsack DP (sum of power of subsequences)

Standard knapsack DP question. The poster later identified it as LeetCode 3082, Find the Sum of the Power of All Subsequences.

The full statement was not shared.

<sub>Topics: DP · Similar: [LeetCode 3082. Find the Sum of the Power of All Subsequences](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/) (Hard) · Source: [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L29), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L30), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L31), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L32), [chat, 28 Sep](../archive/teradata-oa/2026-09.jsonl#L33)</sub>

### Q2. Minimum Jumps to Reach End via Prime Teleportation

(LeetCode 3629) You are given an integer array nums of length n. You start at index 0 and your goal is to reach index n - 1. From any index i you may do one of these operations:  
- Adjacent step: jump to index i + 1 or i - 1, if that index is within bounds.  
- Prime teleportation: if nums[i] is a prime number p, you may jump instantly to any index j != i such that nums[j] % p == 0.  
Return the minimum number of jumps needed to reach index n - 1.

Example 1: nums = [1,2,4,6] -> 2 (step 0->1, nums[1]=2 is prime, teleport to index 3 since 6 % 2 == 0).  
Example 2: nums = [2,3,4,7,9] -> 2 (step 0->1, nums[1]=3 is prime, teleport to index 4 since 9 % 3 == 0).  
Example 3: nums = [4,6,5,8] -> 3 (no useful teleport, so take adjacent steps 0->1->2->3).

Constraints: 1 &lt;= n == nums.length &lt;= 10^5, 1 &lt;= nums[i] &lt;= 10^6.  
Link: https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

<sub>Topics: Graphs, Math · Similar: [LeetCode 3629. Minimum Jumps to Reach End via Prime Teleportation](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/) (Medium) · Source: [chat, 28 Sep](../archive/inter-iit/2026-09.jsonl#L9), [chat, 28 Sep](../archive/inter-nit/2026-09.jsonl#L177), [chat, 28 Sep](../archive/inter-nit/2026-09.jsonl#L80) · Also asked at: IIT BHU (2026-09-28)</sub>

### Q3. Minimum Cost to Hire K Workers

(LeetCode 857) There are n workers. You are given two integer arrays quality and wage, where quality[i] is the quality of the i-th worker and wage[i] is that worker's minimum wage expectation. You want to hire exactly k workers to form a paid group. When you hire a group of k workers, you must pay them by these rules:  
1. Each worker in the group is paid in proportion to their quality compared with the other workers in the group.  
2. Each worker in the group must be paid at least their minimum wage expectation.  
Given k, return the least amount of money needed to form a paid group that meets these conditions. Answers within 10^-5 of the actual answer are accepted.

Example 1: quality = [10,20,5], wage = [70,50,30], k = 2 -> 105.00000 (pay 70 to worker 0 and 35 to worker 2).  
Example 2: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3 -> 30.66667 (pay 4 to worker 0 and 13.33333 each to workers 2 and 3).

Constraints: n == quality.length == wage.length, 1 &lt;= k &lt;= n &lt;= 10^4, 1 &lt;= quality[i], wage[i] &lt;= 10^4.  
Link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

<sub>Topics: Heaps, Greedy, Sorting · Similar: [LeetCode 857. Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) (Hard) · Source: [chat, 28 Sep](../archive/inter-iit/2026-09.jsonl#L9), [chat, 28 Sep](../archive/inter-nit/2026-09.jsonl#L177), [chat, 28 Sep](../archive/inter-nit/2026-09.jsonl#L80) · Also asked at: IIT BHU (2026-09-28)</sub>
