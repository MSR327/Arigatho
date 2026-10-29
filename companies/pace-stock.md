# Pace Stock

**8 questions** · 2 drives · latest 7 Oct 2026 · [2 LeetCode matches](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Math](../topics/math.md) 4 · [Greedy](../topics/greedy.md) 4 · [Hashing](../topics/hashing.md) 3 · [Bit Manipulation](../topics/bit-manipulation.md) 2 · [Arrays](../topics/arrays.md) 2 · [Binary Search](../topics/binary-search.md) 2 · [Graphs](../topics/graphs.md) 2 · [Sorting](../topics/sorting.md) 1  
**Seen at:** IIT Kharagpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-07 · IIT Kharagpur · FTE](#2026-10-07--iit-kharagpur--fte)
  - [Subarrays whose bitwise OR is present in the subarray](#q1-subarrays-whose-bitwise-or-is-present-in-the-subarray)
  - [Maximum pairs with non-perfect-square product after K changes](#q2-maximum-pairs-with-non-perfect-square-product-after-k-changes)
  - [Train and execute ML algorithms in minimum days](#q3-train-and-execute-ml-algorithms-in-minimum-days)
  - [Number of connected servers via gcd > 1](#q4-number-of-connected-servers-via-gcd--1)
- [2026-10-06 · IIT Kharagpur · FTE](#2026-10-06--iit-kharagpur--fte)
  - [Subarrays whose bitwise OR is present in the subarray](#q1-subarrays-whose-bitwise-or-is-present-in-the-subarray-1)
  - [Maximum pairs with non-perfect-square product after K changes](#q2-maximum-pairs-with-non-perfect-square-product-after-k-changes-1)
  - [Minimum days to train and execute all ML algorithms](#q3-minimum-days-to-train-and-execute-all-ml-algorithms)
  - [Server connectivity via GCD > 1](#q4-server-connectivity-via-gcd--1)

</details>

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
