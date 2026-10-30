# Pace Stock

**8 questions** · 2 drives · latest 8 Oct 2026 · [8 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Arrays](../topics/arrays.md) 3 · [Math](../topics/math.md) 3 · [Graphs](../topics/graphs.md) 3 · [Greedy](../topics/greedy.md) 2 · [Hashing](../topics/hashing.md) 2 · [Bit Manipulation](../topics/bit-manipulation.md) 1 · [Binary Search](../topics/binary-search.md) 1 · [Trees](../topics/trees.md) 1 · +3 more  
**Seen at:** IIT Delhi, IIT Kharagpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-08 · IIT Delhi · FTE · Software Engineer / Jr. Quant Researcher](#2026-10-08--iit-delhi--fte--software-engineer--jr-quant-researcher)
  - [Shortest walk through required vertices in a tree](#q1-shortest-walk-through-required-vertices-in-a-tree)
  - [Nearest city on the same line](#q2-nearest-city-on-the-same-line)
  - [Count exactly overlapping regions in two grids](#q3-count-exactly-overlapping-regions-in-two-grids)
  - [Suffix-to-front string transformations](#q4-suffix-to-front-string-transformations)
- [2026-10-06 · IIT Kharagpur · FTE](#2026-10-06--iit-kharagpur--fte)
  - [Subarrays whose bitwise OR is present in the subarray](#q1-subarrays-whose-bitwise-or-is-present-in-the-subarray)
  - [Maximum pairs with non-perfect-square product after K changes](#q2-maximum-pairs-with-non-perfect-square-product-after-k-changes)
  - [Minimum days to train and execute all ML algorithms](#q3-minimum-days-to-train-and-execute-all-ml-algorithms)
  - [Server connectivity via GCD > 1](#q4-server-connectivity-via-gcd--1)

</details>

---

## 2026-10-08 · IIT Delhi · FTE · Software Engineer / Jr. Quant Researcher

### Q1. Shortest walk through required vertices in a tree

A tree has n nodes 1...n and n-1 edges (each costs 1 to walk). You are given k vertices a_1, ..., a_k that must be visited.

- The walk starts at node 1 and must end at node n.
- Every a_i must be visited at least once, in any order. Nodes and edges may be repeated.

Return the minimum number of edges walked.

Practice (same problem, any start/end): Codeforces 1675F - Vlad and Unfinished Business.

<sub>Topics: Trees, Graphs · Same problem: [Codeforces 1675F. Vlad and Unfinished Business](https://codeforces.com/problemset/problem/1675/F) (rated 1800), tree walk visiting required nodes, start 1 end n · Source: [Pace Stock - OA.pdf](../archive/files/4151-Pace_Stock_-_OA.pdf), [chat, 8 Oct](../archive/campus-iit-kanpur-placements/2026-10.jsonl#L156)</sub>

### Q2. Nearest city on the same line

There are n cities: city[i] is at (x_i, y_i), given by city (vector<string>), x, y (vector<int>). No two cities are at the same point. You are given q queries, each a city name.

- For a queried city, the candidates are the other cities with the same x or the same y.
- Answer = the nearest candidate. If two are equally near, the lexicographically smaller name.
- If no other city shares its x or y, the answer is "NONE".

Return a vector<string> with the answer for every query, in order.

<sub>Topics: Hashing, Sorting, Arrays · Close variant: [LeetCode 1779. Find Nearest Point That Has the Same X or Y Coordinate](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/) (Easy), nearest point sharing x or y coordinate · Source: [Pace Stock - OA.pdf](../archive/files/4151-Pace_Stock_-_OA.pdf), [chat, 8 Oct](../archive/campus-iit-kanpur-placements/2026-10.jsonl#L156)</sub>

### Q3. Count exactly overlapping regions in two grids

You are given two binary grids grid1 and grid2 of the same size R x C. A region is a group of 1-cells connected 4-directionally (up, down, left, right).

Place grid2 on top of grid1. A region of grid2 counts if grid1 has a region made of exactly the same cells (no cell more, no cell less).

Return the number of such regions of grid2.

Practice (closest, weaker "inside" condition): LeetCode 1905 - Count Sub Islands.

<sub>Topics: Graphs, Arrays · Close variant: [LeetCode 1905. Count Sub Islands](https://leetcode.com/problems/count-sub-islands/) (Medium), grid2 islands compared against grid1 islands via DFS · Source: [Pace Stock - OA.pdf](../archive/files/4151-Pace_Stock_-_OA.pdf), [chat, 8 Oct](../archive/campus-iit-kanpur-placements/2026-10.jsonl#L156)</sub>

### Q4. Suffix-to-front string transformations

You are given strings s and t of equal length n, and an integer k.

One transformation: remove a suffix of length l (0 < l < n) and append it at the front. E.g. abcd with l = 2 -> cdab.

Perform exactly k transformations.

Return the number of ways to turn s into t, modulo 10^9 + 7.

Practice (same problem): LeetCode 2851 - String Transformation.

<sub>Topics: Strings, DP, Math · Similar: [LeetCode 2851. String Transformation](https://leetcode.com/problems/string-transformation/) (Hard) · Source: [Pace Stock - OA.pdf](../archive/files/4151-Pace_Stock_-_OA.pdf), [chat, 8 Oct](../archive/campus-iit-kanpur-placements/2026-10.jsonl#L156)</sub>

## 2026-10-06 · IIT Kharagpur · FTE

### Q1. Subarrays whose bitwise OR is present in the subarray

Given an array a of size n, find the number of subarrays for which the bitwise OR of that subarray is present in that subarray. E.g. for [1, 6, 7] the bitwise OR is 7, which is present in this array. Constraints: N &lt; 1e5, A[i] &lt; 1e6.

<sub>Topics: Bit Manipulation, Arrays · Same idea: [LeetCode 898. Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/) (Medium), subarray ORs take few distinct values per endpoint · Source: [chat, 6 Oct](../archive/inter-iit/2026-10.jsonl#L393) · Also asked at: IIT Kharagpur (2026-10-07)</sub>

### Q2. Maximum pairs with non-perfect-square product after K changes

There are N students. The i-th student is assigned number A[i]. We can pair up any two students if the product of their assigned numbers is NOT a perfect square. One student can belong to at most 1 pair. We are given an integer K. We can change at most K elements of this array to any other positive number of our choice. Find the maximum number of pairs we can achieve by doing at most K operations. Constraints: N &lt; 1e5, A[i] &lt; 1e6.

<sub>Topics: Math, Greedy, Hashing · Same idea: [Codeforces 1497E1. Square-Free Division (easy version)](https://codeforces.com/problemset/problem/1497/E1) (rated 1700), square-free part reduction for perfect-square products · Source: [chat, 6 Oct](../archive/inter-iit/2026-10.jsonl#L393) · Also asked at: IIT Kharagpur (2026-10-07)</sub>

### Q3. Minimum days to train and execute all ML algorithms

There are N machine learning algorithms. The i-th algorithm needs train[i] days for its training. Each algorithm can be executed only on certain specific days out of the M days, given as an N * M array where executionDays[i] contains the days on which the i-th algorithm can be executed. On each day we can do one of the following: train some algorithm; execute one of the algorithms if its training is complete and it is eligible to be executed on that day; or do nothing. Find the minimum number of days it will take to train and execute all algorithms. Return -1 if it is impossible. Constraints (approximate): N &lt; 1e5, N * M &lt; 1e5, executionDays[i][j] &lt; 1e9, train[i] &lt; 1e9.

<sub>Topics: Binary Search, Greedy · Similar: [LeetCode 3048. Earliest Second to Mark Indices I](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) (Medium) · Source: [chat, 6 Oct](../archive/inter-iit/2026-10.jsonl#L393) · Also asked at: IIT Kharagpur (2026-10-07)</sub>

### Q4. Server connectivity via GCD > 1

There are N servers. Server i and server j are connected if gcd(server[i], server[j]) > 1. For each server, return the number of servers it is connected to (indirect connections also count). Constraints: N &lt; 1e5, A[i] &lt; 1e6.

<sub>Topics: Graphs, Math · Similar: [LeetCode 952. Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) (Hard) · Source: [chat, 6 Oct](../archive/inter-iit/2026-10.jsonl#L393) · Also asked at: IIT Kharagpur (2026-10-07)</sub>
