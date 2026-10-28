# InMobi

**14 questions** from 7 OA drives · seen at IIT BHU, IIT Bombay, IIT Delhi, IIT Guwahati, IIT Roorkee · latest 2026-10-23

**Topics:** [Arrays](../topics/arrays.md) (8) · [Graphs](../topics/graphs.md) (3) · [Binary Search](../topics/binary-search.md) (2) · [Recursion/Backtracking](../topics/recursion-backtracking.md) (2) · [DP](../topics/dp.md) (2) · [Hashing](../topics/hashing.md) (2) · [Heaps](../topics/heaps.md) (1) · [Bit Manipulation](../topics/bit-manipulation.md) (1) · [Greedy](../topics/greedy.md) (1) · [Sliding Window](../topics/sliding-window.md) (1) · [Stack/Queue](../topics/stack-queue.md) (1) · [OA Format](../topics/oa-format.md) (1) · [Strings](../topics/strings.md) (1)

**LeetCode matches:** 8 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-22 · IIT Delhi · FTE](#2026-10-22--iit-delhi--fte) · 2 questions
- [2026-10-14 · IIT BHU · FTE](#2026-10-14--iit-bhu--fte) · 3 questions
- [2026-10-08 · IIT BHU · FTE](#2026-10-08--iit-bhu--fte) · 1 question
- [2026-10-07 · IIT Roorkee · FTE](#2026-10-07--iit-roorkee--fte) · 1 question
- [2026-10-05 · IIT BHU · FTE](#2026-10-05--iit-bhu--fte) · 3 questions
- [2026-10-04 · IIT Bombay · Intern](#2026-10-04--iit-bombay--intern) · 1 question
- [2026-09-26 · IIT Guwahati · FTE](#2026-09-26--iit-guwahati--fte) · 3 questions

[← all companies](../README.md#companies)

---

## 2026-10-22 · IIT Delhi · FTE

### Q1. Word Ladder II variant with costs

Very long problem statement. Similar to the Word Ladder II problem (find transformation sequences from a begin word to an end word changing one letter at a time using a dictionary), but with a cost attached to transformations.

<sub>Topics: Graphs, Strings · Source: [chat, 22 Oct](../archive/inter-nit/2026-10.jsonl#L2027), [chat, 22 Oct](../archive/inter-nit/2026-10.jsonl#L2028), [chat, 22 Oct](../archive/inter-nit/2026-10.jsonl#L2029) · Also asked at: IIT Delhi (2026-10-23)</sub>

### Q2. Graph dependencies problem

Second question was a long, somewhat confusing problem about dependencies modeled as a graph (dependency resolution / ordering).

<sub>Topics: Graphs · Source: [chat, 22 Oct](../archive/inter-nit/2026-10.jsonl#L2027), [chat, 22 Oct](../archive/inter-nit/2026-10.jsonl#L2028), [chat, 22 Oct](../archive/inter-nit/2026-10.jsonl#L2029) · Also asked at: IIT Delhi (2026-10-23)</sub>

## 2026-10-14 · IIT BHU · FTE

### Q1. Check Array Formation Through Concatenation (LeetCode 1640)

LeetCode 1640. You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i]. Return true if it is possible to form arr from pieces, otherwise return false.  
Example 1: arr = [15,88], pieces = [[88],[15]] -> true.  
Example 2: arr = [49,18,16], pieces = [[16,18,49]] -> false.  
Example 3: arr = [91,4,64,78], pieces = [[78],[4,64],[91]] -> true.  
Constraints: 1 &lt;= pieces.length &lt;= arr.length &lt;= 100; sum(pieces[i].length) == arr.length; 1 &lt;= arr[i], pieces[i][j] &lt;= 100; integers in arr are distinct; integers in pieces are distinct.  
(Platform: DoSelect, 3 DSA problems in 1 hr 30 min, LeetCode medium-hard.)

<sub>Topics: Arrays, Hashing · Similar: [LeetCode 1640. Check Array Formation Through Concatenation](https://leetcode.com/problems/check-array-formation-through-concatenation/) (Easy) · Source: [chat, 14 Oct](../archive/inter-nit/2026-10.jsonl#L125)</sub>

### Q2. Recursion + backtracking problem

One of the 3 DSA problems was a recursion + backtracking problem (exact statement not shared). Platform: DoSelect; difficulty LeetCode medium-hard; 1 hr 30 min total.

<sub>Topics: Recursion/Backtracking · Source: [chat, 14 Oct](../archive/inter-nit/2026-10.jsonl#L125)</sub>

### Q3. Very easy problem with unusual input format

One very easy problem (statement not shared). The catch was the input: the array size n was not given, so the array elements had to be read until end of input.

<sub>Topics: Arrays, OA Format · Source: [chat, 14 Oct](../archive/inter-nit/2026-10.jsonl#L125)</sub>

## 2026-10-08 · IIT BHU · FTE

### Q1. Trionic Array II (LeetCode 3640)

You are given an integer array nums of length n. A trionic subarray is a contiguous subarray nums[l...r] (with 0 &lt;= l &lt; r &lt; n) for which there exist indices l &lt; p &lt; q &lt; r such that:  
- nums[l...p] is strictly increasing,  
- nums[p...q] is strictly decreasing,  
- nums[q...r] is strictly increasing.  
Return the maximum sum of any trionic subarray in nums.

Example 1: nums = [0,-2,-1,-3,0,2,-1] -> Output: -4 (l=1, p=2, q=3, r=5: [-2,-1] increasing, [-1,-3] decreasing, [-3,0,2] increasing; sum = -4).  
Example 2: nums = [1,4,2,7] -> Output: 14.

Constraints: 4 &lt;= n &lt;= 10^5; -10^9 &lt;= nums[i] &lt;= 10^9; at least one trionic subarray is guaranteed to exist.

(Shared as link: https://leetcode.com/problems/trionic-array-ii/description/)

<sub>Topics: DP, Arrays · Similar: [LeetCode 3640. Trionic Array II](https://leetcode.com/problems/trionic-array-ii/) (Hard) · Source: [chat, 8 Oct](../archive/inter-nit/2026-10.jsonl#L753), [chat, 8 Oct](../archive/inter-nit/2026-10.jsonl#L754), [chat, 8 Oct](../archive/inter-nit/2026-10.jsonl#L755), [chat, 8 Oct](../archive/inter-iit/2026-10.jsonl#L345)</sub>

## 2026-10-07 · IIT Roorkee · FTE

### Q1. Maximum Sum of Subarray Maximums

Given an integer array arr of size N, consider every possible contiguous subarray of arr. For each subarray, find its maximum element. Return the sum of these maximum elements over all possible subarrays.  
Input Format: The first line contains an integer N, the size of the array. The second line contains N space-separated integers representing the array.  
Output Format: Print a single integer representing the sum of the maximum element of every possible contiguous subarray.

<sub>Topics: Stack/Queue, Arrays · Similar: [LeetCode 907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) (Medium) · Source: [chat, 7 Oct](../archive/inter-nit/2026-10.jsonl#L813)</sub>

## 2026-10-05 · IIT BHU · FTE

### Q1. Circular Defense

There are N defense towers arranged in a circle. Each tower i has a power P[i] and a range R[i]. A tower can neutralize any tower that lies within its range (in both directions on the circle). The distance between adjacent towers is 1 unit. Find the minimum number of towers required to keep active so that all towers are neutralized (either the tower itself is active, or it is within range of an active tower).

Key points:  
- Towers are arranged in a circle (tower 0 and tower N-1 are adjacent).  
- Tower i with range R[i] covers towers at distance &lt;= R[i] in both clockwise and counter-clockwise directions.  
- An active tower neutralizes itself.  
- Find the minimum number of active towers needed to neutralize all N towers.

Input format:  
First line: N (number of towers)  
Next N lines: Pi Ri (power and range of tower i)

Output format: Print a single integer: the minimum number of towers needed to neutralize all towers.

Constraints:  
1 &lt;= N &lt;= 20  
1 &lt;= Pi &lt;= 1000  
0 &lt;= Ri &lt;= N

Example: N = 6, every tower has range 1. Tower 0 covers [5,0,1], tower 1 covers [0,1,2], tower 2 covers [1,2,3], tower 3 covers [2,3,4], tower 4 covers [3,4,5], tower 5 covers [4,5,0]. Activating towers 0 and 3 (or 1 and 4, or 2 and 5) covers all positions {0..5}. No single tower with range 1 can cover all 6 positions. Output: 2

<sub>Topics: Bit Manipulation, Recursion/Backtracking, Greedy · Source: [image.png](../archive/files/3191-image.png), [image.png](../archive/files/3192-image.png), [image.png](../archive/files/3193-image.png), [image.png](../archive/files/3194-image.png), [image.png](../archive/files/3195-image.png)</sub>

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
4 &lt;= n &lt;= 10^5  
-10^9 &lt;= engagementScores[i] &lt;= 10^9

Input format: First line contains the size of the engagementScores array. Second line contains the engagementScores array.  
Output format: Print the total engagement for the wave.  
Execution time limit: 1.00 seconds

<sub>Topics: DP, Arrays · Similar: [LeetCode 3640. Trionic Array II](https://leetcode.com/problems/trionic-array-ii/) (Hard) · Source: [image.png](../archive/files/3191-image.png), [image.png](../archive/files/3192-image.png), [image.png](../archive/files/3193-image.png), [image.png](../archive/files/3194-image.png), [image.png](../archive/files/3195-image.png)</sub>

### Q3. Count Nice Sub Array

Given an array of integers nums and an integer k, a continuous subarray is called nice if it contains exactly k odd numbers. Return the number of nice subarrays.

Input format: Two lines:  
1. An integer k, the required number of odd numbers  
2. A line of space-separated integers, the array nums

Output format: A single integer, the number of nice subarrays.

Constraints:  
1 &lt;= nums.length &lt;= 50000  
1 &lt;= nums[i] &lt;= 10^5  
1 &lt;= k &lt;= nums.length

TestCase 1:  
Input:  
3  
1 1 2 1 1  
Output: 2

<sub>Topics: Sliding Window, Hashing, Arrays · Similar: [LeetCode 1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) (Medium) · Source: [image.png](../archive/files/3191-image.png), [image.png](../archive/files/3192-image.png), [image.png](../archive/files/3193-image.png), [image.png](../archive/files/3194-image.png), [image.png](../archive/files/3195-image.png)</sub>

## 2026-10-04 · IIT Bombay · Intern

### Q1. Teemo Attacking (LeetCode 495)

Shared as a link: https://algo.monster/liteproblems/495 (LeetCode 495, Teemo Attacking), described as asked in the InMobi intern OA.

Teemo attacks an enemy, Ashe, with poison. An attack at second t poisons Ashe for exactly `duration` seconds, i.e. during the inclusive interval [t, t + duration - 1]. If Teemo attacks again before the poison wears off, the timer resets and the poison ends `duration` seconds after the new attack.

Given a non-decreasing integer array timeSeries, where timeSeries[i] is the second of the i-th attack, and an integer duration, return the total number of seconds that Ashe is poisoned.

Example: timeSeries = [1,4], duration = 2 -> 4; timeSeries = [1,2], duration = 2 -> 3.  
Constraints: 1 &lt;= timeSeries.length &lt;= 10^4; 0 &lt;= timeSeries[i], duration &lt;= 10^7; timeSeries is sorted in non-decreasing order.

<sub>Topics: Arrays · Similar: [LeetCode 495. Teemo Attacking](https://leetcode.com/problems/teemo-attacking/) (Easy) · Source: [chat, 4 Oct](../archive/inter-iit/2026-10.jsonl#L353)</sub>

## 2026-09-26 · IIT Guwahati · FTE

### Q1. DSU-based problem

A question that used Disjoint Set Union (Union-Find). The poster did not give the full problem.

<sub>Topics: Graphs · Source: [chat, 26 Sep](../archive/inter-nit/2026-09.jsonl#L183)</sub>

### Q2. Median of 3 sorted arrays

Given three sorted arrays, find the median of all their elements combined.

<sub>Topics: Binary Search, Arrays · Similar: [LeetCode 4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) (Hard) · Source: [chat, 26 Sep](../archive/inter-nit/2026-09.jsonl#L183)</sub>

### Q3. Kth smallest element in sum matrix

You are given two arrays X and Y. They define a matrix where A[i][j] = X[i] + Y[j]. Find the k-th smallest element in this matrix.

<sub>Topics: Heaps, Binary Search · Similar: [LeetCode 373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) (Medium) · Source: [chat, 26 Sep](../archive/inter-nit/2026-09.jsonl#L183)</sub>
