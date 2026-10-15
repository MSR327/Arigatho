# Honda OA

## 2026-10-09 · VIT Vellore · FTE

### Q1. Maximum GCD of Any Pair

Given an integer n (n ≥ 2), consider every pair of distinct integers (a, b) with 1 ≤ a < b ≤ n. Return the maximum value of gcd(a, b) over all such pairs.

Example
Input: n = 5
Pairs: (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)
Output: 2, from the pair (2, 4)

Topics: Math  
📎 source: [msg 4303](../archive/inter-iit/2026-10.jsonl)

### Q2. Unique Pairs with Target Sum

Given an integer array nums and an integer target, return all unique pairs (a, b) from the array such that a + b = target.
- Each pair uses two different indices.
- Pairs are unordered, so (a, b) and (b, a) count as the same pair.
- Duplicate values in the array must not produce duplicate pairs in the output.

Example
Input: nums = [1, 5, 7, -1, 5], target = 6
Output: [(1, 5), (7, -1)], where (1, 5) appears only once even though 5 occurs twice

Topics: Arrays, Hashing, Two Pointers  
📎 source: [msg 4303](../archive/inter-iit/2026-10.jsonl)

### Q3. Maximum Jumps to Reach the Last Index

You are given an array nums of length n and an integer limit. You start at index 0 and want to reach index n - 1.

From index i, you may jump to any index j that satisfies both conditions:
- i < j (you can only jump forward)
- |nums[j] - nums[i]| ≤ limit

Return the maximum number of jumps you can make to reach index n - 1. If the last index cannot be reached, return -1.

Example
Input: nums = [1, 3, 6, 4, 1, 2], limit = 2
Output: 3, using the path 0 → 1 → 3 → 5 (values 1 → 3 → 4 → 2)

This is the same problem as LeetCode 2770, "Maximum Number of Jumps to Reach the Last Index."

Topics: DP, Arrays  
📎 source: [msg 4303](../archive/inter-iit/2026-10.jsonl)

### Q4. Remove Suspicious Nodes from a Directed Graph

You are given n nodes labeled 0 to n - 1, a list of directed edges edges where [a, b] means node a points to node b, and a node k that is suspicious.

Suspicious set: node k, plus every node reachable from k (directly or indirectly) by following the edges.

Rule:
- If no node outside the suspicious set has an edge into any node inside it, remove the entire suspicious set.
- If at least one outside node points into the suspicious set, removing it is not allowed, so no nodes are removed.

Return the remain[ing nodes] ... (message text was cut off here in the source)

Topics: Graphs  
📎 source: [msg 4303](../archive/inter-iit/2026-10.jsonl)
