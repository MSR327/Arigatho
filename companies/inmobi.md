# InMobi OA

## 2026-10-08 · IIT BHU · FTE

### Q1. Trionic Array II (LeetCode 3640)

You are given an integer array nums of length n. A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:
- nums[l...p] is strictly increasing,
- nums[p...q] is strictly decreasing,
- nums[q...r] is strictly increasing.
Return the maximum sum of any trionic subarray in nums.

Example 1: nums = [0,-2,-1,-3,0,2,-1] -> Output: -4 (l=1, p=2, q=3, r=5: [-2,-1] increasing, [-1,-3] decreasing, [-3,0,2] increasing; sum = -4).
Example 2: nums = [1,4,2,7] -> Output: 14.

Constraints: 4 <= n <= 10^5; -10^9 <= nums[i] <= 10^9; at least one trionic subarray is guaranteed to exist.

(Shared as link: https://leetcode.com/problems/trionic-array-ii/description/)

Topics: Arrays, DP  
📎 source: [msg 3835](../archive/inter-nit/2026-10.jsonl), [msg 3836](../archive/inter-nit/2026-10.jsonl), [msg 3837](../archive/inter-nit/2026-10.jsonl), [msg 3841](../archive/inter-iit/2026-10.jsonl)

## 2026-10-07 · IIT Roorkee · FTE

### Q1. Maximum Sum of Subarray Maximums

Given an integer array arr of size N, consider every possible contiguous subarray of arr. For each subarray, find its maximum element. Return the sum of these maximum elements over all possible subarrays.
Input Format: The first line contains an integer N, the size of the array. The second line contains N space-separated integers representing the array.
Output Format: Print a single integer representing the sum of the maximum element of every possible contiguous subarray.

Topics: Stack/Queue, Arrays  
📎 source: [msg 3669](../archive/inter-nit/2026-10.jsonl)

## 2026-10-05 · IIT BHU · FTE

### Q1. Circular Defense

There are N defense towers arranged in a circle. Each tower i has a power P[i] and a range R[i]. A tower can neutralize any tower that lies within its range (in both directions on the circle). The distance between adjacent towers is 1 unit. Find the minimum number of towers required to keep active so that all towers are neutralized (either the tower itself is active, or it is within range of an active tower).

Key points:
- Towers are arranged in a circle (tower 0 and tower N-1 are adjacent).
- Tower i with range R[i] covers towers at distance <= R[i] in both clockwise and counter-clockwise directions.
- An active tower neutralizes itself.
- Find the minimum number of active towers needed to neutralize all N towers.

Input format:
First line: N (number of towers)
Next N lines: Pi Ri (power and range of tower i)

Output format: Print a single integer: the minimum number of towers needed to neutralize all towers.

Constraints:
1 <= N <= 20
1 <= Pi <= 1000
0 <= Ri <= N

Example: N = 6, every tower has range 1. Tower 0 covers [5,0,1], tower 1 covers [0,1,2], tower 2 covers [1,2,3], tower 3 covers [2,3,4], tower 4 covers [3,4,5], tower 5 covers [4,5,0]. Activating towers 0 and 3 (or 1 and 4, or 2 and 5) covers all positions {0..5}. No single tower with range 1 can cover all 6 positions. Output: 2

Topics: Bit Manipulation, Recursion/Backtracking, Greedy  
📎 source: [image.png](../archive/files/3191-image.png), [image.png](../archive/files/3192-image.png), [image.png](../archive/files/3193-image.png), [image.png](../archive/files/3194-image.png), [image.png](../archive/files/3195-image.png)

### Q2. Campaign Wave Analyzer

IX Analytics, a digital ad-effectiveness platform, helps marketers visualize campaign effectiveness over time through engagement scores. Campaigns often follow a wave pattern: Initial Curiosity (engagement rises as new creatives launch), Fatigue (engagement drops as ads become repetitive), and Reinvigoration (engagement rises again through retargeting or fresh creatives).

A campaign wave is a continuous series of days, from Day l to Day r, that fits this structure:
- Between Day l and Day p, engagement climbs.
- Between Day p and Day q, engagement declines.
- Between Day q and Day r, engagement recovers (increases).

Given an integer array engagementScores of length n, where each element is the net user engagement (positive or negative) for a given day, find the maximum sum over all possible campaign waves.

Sample: Input: [0,-2,-1,-3,0,2,-1], Output: -4
Explanation: Days 1 to 5 form a wave: Days 1-2 rise from -2 to -1, Days 2-3 fall from -1 to -3, Days 3-5 rise from -3 to 0 to 2. Total = (-2)+(-1)+(-3)+0+2 = -4.

Constraints:
4 <= n <= 10^5
-10^9 <= engagementScores[i] <= 10^9

Input format: First line contains the size of the engagementScores array. Second line contains the engagementScores array.
Output format: Print the total engagement for the wave.
Execution time limit: 1.00 seconds

Topics: DP, Arrays  
📎 source: [image.png](../archive/files/3191-image.png), [image.png](../archive/files/3192-image.png), [image.png](../archive/files/3193-image.png), [image.png](../archive/files/3194-image.png), [image.png](../archive/files/3195-image.png)

### Q3. Count Nice Sub Array

Given an array of integers nums and an integer k, a continuous subarray is called nice if it contains exactly k odd numbers. Return the number of nice subarrays.

Input format: Two lines:
1. An integer k, the required number of odd numbers
2. A line of space-separated integers, the array nums

Output format: A single integer, the number of nice subarrays.

Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

TestCase 1:
Input:
3
1 1 2 1 1
Output: 2

Topics: Sliding Window, Hashing, Arrays  
📎 source: [image.png](../archive/files/3191-image.png), [image.png](../archive/files/3192-image.png), [image.png](../archive/files/3193-image.png), [image.png](../archive/files/3194-image.png), [image.png](../archive/files/3195-image.png)

## 2026-10-04 · IIT Bombay · Intern

### Q1. Teemo Attacking (LeetCode 495)

Shared as a link: https://algo.monster/liteproblems/495 (LeetCode 495, Teemo Attacking), described as asked in the InMobi intern OA.

Teemo attacks an enemy, Ashe, with poison. An attack at second t poisons Ashe for exactly `duration` seconds, i.e. during the inclusive interval [t, t + duration - 1]. If Teemo attacks again before the poison wears off, the timer resets and the poison ends `duration` seconds after the new attack.

Given a non-decreasing integer array timeSeries, where timeSeries[i] is the second of the i-th attack, and an integer duration, return the total number of seconds that Ashe is poisoned.

Example: timeSeries = [1,4], duration = 2 -> 4; timeSeries = [1,2], duration = 2 -> 3.
Constraints: 1 <= timeSeries.length <= 10^4; 0 <= timeSeries[i], duration <= 10^7; timeSeries is sorted in non-decreasing order.

Topics: Arrays  
📎 source: [msg 2747](../archive/inter-iit/2026-10.jsonl)

## 2026-09-26 · IIT Guwahati · FTE

### Q1. DSU-based problem

A question that used Disjoint Set Union (Union-Find). The poster did not give the full problem.

Topics: Graphs  
📎 source: [msg 1345](../archive/inter-nit/2026-09.jsonl)

### Q2. Median of 3 sorted arrays

Given three sorted arrays, find the median of all their elements combined.

Topics: Arrays, Binary Search  
📎 source: [msg 1345](../archive/inter-nit/2026-09.jsonl)

### Q3. Kth smallest element in sum matrix

You are given two arrays X and Y. They define a matrix where A[i][j] = X[i] + Y[j]. Find the k-th smallest element in this matrix.

Topics: Heaps, Binary Search, Sorting  
📎 source: [msg 1345](../archive/inter-nit/2026-09.jsonl)
