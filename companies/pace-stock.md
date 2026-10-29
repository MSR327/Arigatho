# Pace Stock

**8 questions** from 2 OA drives · seen at IIT Kharagpur · latest 2026-10-07

**Topics:** [Math](../topics/math.md) (4) · [Greedy](../topics/greedy.md) (4) · [Hashing](../topics/hashing.md) (3) · [Bit Manipulation](../topics/bit-manipulation.md) (2) · [Arrays](../topics/arrays.md) (2) · [Binary Search](../topics/binary-search.md) (2) · [Graphs](../topics/graphs.md) (2) · [Sorting](../topics/sorting.md) (1)

**LeetCode matches:** 2 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-07 · IIT Kharagpur · FTE](#2026-10-07--iit-kharagpur--fte) · 4 questions
- [2026-10-06 · IIT Kharagpur · FTE](#2026-10-06--iit-kharagpur--fte) · 4 questions

[← all companies](../README.md#companies)

---

## 2026-10-07 · IIT Kharagpur · FTE

### Q1. Subarrays whose bitwise OR is present in the subarray

Given array `a` of size n, find the number of subarrays for which the bitwise OR of that subarray is present in that subarray. E.g. for `[1, 6, 7]` the bitwise OR is 7 which is present in this array.

Constraints: N < 1e5, A[i] < 1e6

<sub>Topics: Bit Manipulation, Arrays · Source: [chat, 7 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L208)</sub>

### Q2. Maximum pairs with non-perfect-square product after K changes

There are N students. The i-th student is assigned number A[i]. We can pair up any two students if the product of their assigned numbers is NOT a perfect square. One student can belong to at most 1 pair. We are given an integer K. We can change at most K elements of this array to any other positive number of our choice. Find the maximum number of pairs we can achieve by doing at most K operations.

Constraints: N < 1e5, A[i] < 1e6

<sub>Topics: Math, Greedy, Hashing · Source: [chat, 7 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L208)</sub>

### Q3. Train and execute ML algorithms in minimum days

There are N machine learning algorithms. The i-th algorithm needs `train[i]` days for its training. Each algorithm can be executed only on some specific days out of M days. We are given an N * M array `executionDays` where `executionDays[i]` contains the days on which the i-th algorithm can be executed. On each day we can do one of the following:
- Train some algorithm
- Execute one of the algorithms if its training is completed and it is eligible to be executed on that day
- Do nothing

Find the minimum number of days it will take to train and execute all algorithms. Return -1 if it is impossible.

Constraints: N < 1e5, N * M < 1e5, executionDay[i][j] < 1e9, train[i] < 1e9 (poster says constraints were close to these, not exact).

<sub>Topics: Binary Search, Greedy, Sorting · Source: [chat, 7 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L208)</sub>

### Q4. Number of connected servers via gcd > 1

There are N servers. Server i and server j are connected if gcd of server[i] and server[j] is greater than 1. For each server return the number of servers to which it is connected (indirect connection is also a connection).

Constraints: N < 1e5, A[i] < 1e6

<sub>Topics: Graphs, Math, Hashing · Source: [chat, 7 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L208)</sub>

## 2026-10-06 · IIT Kharagpur · FTE

### Q1. Subarrays whose bitwise OR is present in the subarray

Given an array a of size n, find the number of subarrays for which the bitwise OR of that subarray is present in that subarray. E.g. for [1, 6, 7] the bitwise OR is 7, which is present in this array. Constraints: N &lt; 1e5, A[i] &lt; 1e6.

<sub>Topics: Bit Manipulation, Arrays · Source: [chat, 6 Oct](../archive/inter-iit/2026-10.jsonl#L393)</sub>

### Q2. Maximum pairs with non-perfect-square product after K changes

There are N students. The i-th student is assigned number A[i]. We can pair up any two students if the product of their assigned numbers is NOT a perfect square. One student can belong to at most 1 pair. We are given an integer K. We can change at most K elements of this array to any other positive number of our choice. Find the maximum number of pairs we can achieve by doing at most K operations. Constraints: N &lt; 1e5, A[i] &lt; 1e6.

<sub>Topics: Math, Greedy, Hashing · Source: [chat, 6 Oct](../archive/inter-iit/2026-10.jsonl#L393)</sub>

### Q3. Minimum days to train and execute all ML algorithms

There are N machine learning algorithms. The i-th algorithm needs train[i] days for its training. Each algorithm can be executed only on certain specific days out of the M days, given as an N * M array where executionDays[i] contains the days on which the i-th algorithm can be executed. On each day we can do one of the following: train some algorithm; execute one of the algorithms if its training is complete and it is eligible to be executed on that day; or do nothing. Find the minimum number of days it will take to train and execute all algorithms. Return -1 if it is impossible. Constraints (approximate): N &lt; 1e5, N * M &lt; 1e5, executionDays[i][j] &lt; 1e9, train[i] &lt; 1e9.

<sub>Topics: Binary Search, Greedy · Similar: [LeetCode 3048. Earliest Second to Mark Indices I](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) (Medium) · Source: [chat, 6 Oct](../archive/inter-iit/2026-10.jsonl#L393)</sub>

### Q4. Server connectivity via GCD > 1

There are N servers. Server i and server j are connected if gcd(server[i], server[j]) > 1. For each server, return the number of servers it is connected to (indirect connections also count). Constraints: N &lt; 1e5, A[i] &lt; 1e6.

<sub>Topics: Graphs, Math · Similar: [LeetCode 952. Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) (Hard) · Source: [chat, 6 Oct](../archive/inter-iit/2026-10.jsonl#L393)</sub>
