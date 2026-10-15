# Teradata OA

## 2026-09-28 · IIT BHU · FTE

### Q1. Minimum Jumps to Reach End via Prime Teleportation

(LeetCode 3629) You are given an integer array nums of length n. You start at index 0 and your goal is to reach index n - 1. From any index i you may do one of these operations:
- Adjacent step: jump to index i + 1 or i - 1, if that index is within bounds.
- Prime teleportation: if nums[i] is a prime number p, you may jump instantly to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps needed to reach index n - 1.

Example 1: nums = [1,2,4,6] -> 2 (step 0->1, nums[1]=2 is prime, teleport to index 3 since 6 % 2 == 0).
Example 2: nums = [2,3,4,7,9] -> 2 (step 0->1, nums[1]=3 is prime, teleport to index 4 since 9 % 3 == 0).
Example 3: nums = [4,6,5,8] -> 3 (no useful teleport, so take adjacent steps 0->1->2->3).

Constraints: 1 <= n == nums.length <= 10^5, 1 <= nums[i] <= 10^6.
Link: https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

Topics: Graphs, Math, Hashing  
📎 source: [msg 1728](../archive/inter-iit/2026-09.jsonl), [msg 1729](../archive/inter-nit/2026-09.jsonl), [msg 1743](../archive/inter-nit/2026-09.jsonl)

### Q2. Minimum Cost to Hire K Workers

(LeetCode 857) There are n workers. You are given two integer arrays quality and wage, where quality[i] is the quality of the i-th worker and wage[i] is that worker's minimum wage expectation. You want to hire exactly k workers to form a paid group. When you hire a group of k workers, you must pay them by these rules:
1. Each worker in the group is paid in proportion to their quality compared with the other workers in the group.
2. Each worker in the group must be paid at least their minimum wage expectation.
Given k, return the least amount of money needed to form a paid group that meets these conditions. Answers within 10^-5 of the actual answer are accepted.

Example 1: quality = [10,20,5], wage = [70,50,30], k = 2 -> 105.00000 (pay 70 to worker 0 and 35 to worker 2).
Example 2: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3 -> 30.66667 (pay 4 to worker 0 and 13.33333 each to workers 2 and 3).

Constraints: n == quality.length == wage.length, 1 <= k <= n <= 10^4, 1 <= quality[i], wage[i] <= 10^4.
Link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

Topics: Greedy, Heaps, Sorting  
📎 source: [msg 1728](../archive/inter-iit/2026-09.jsonl), [msg 1729](../archive/inter-nit/2026-09.jsonl), [msg 1743](../archive/inter-nit/2026-09.jsonl)
