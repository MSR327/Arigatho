# Pace Stock OA

## 2026-10-06 · IIT Kharagpur · FTE

### Q1. Subarrays whose bitwise OR is present in the subarray

Given an array a of size n, find the number of subarrays for which the bitwise OR of that subarray is present in that subarray. E.g. for [1, 6, 7] the bitwise OR is 7, which is present in this array. Constraints: N < 1e5, A[i] < 1e6.

Topics: Bit Manipulation, Arrays  
📎 source: [msg 3362](../archive/inter-iit/2026-10.jsonl)

### Q2. Maximum pairs with non-perfect-square product after K changes

There are N students. The i-th student is assigned number A[i]. We can pair up any two students if the product of their assigned numbers is NOT a perfect square. One student can belong to at most 1 pair. We are given an integer K. We can change at most K elements of this array to any other positive number of our choice. Find the maximum number of pairs we can achieve by doing at most K operations. Constraints: N < 1e5, A[i] < 1e6.

Topics: Math, Greedy, Hashing  
📎 source: [msg 3362](../archive/inter-iit/2026-10.jsonl)

### Q3. Minimum days to train and execute all ML algorithms

There are N machine learning algorithms. The i-th algorithm needs train[i] days for its training. Each algorithm can be executed only on certain specific days out of the M days, given as an N * M array where executionDays[i] contains the days on which the i-th algorithm can be executed. On each day we can do one of the following: train some algorithm; execute one of the algorithms if its training is complete and it is eligible to be executed on that day; or do nothing. Find the minimum number of days it will take to train and execute all algorithms. Return -1 if it is impossible. Constraints (approximate): N < 1e5, N * M < 1e5, executionDays[i][j] < 1e9, train[i] < 1e9.

Topics: Binary Search, Greedy  
📎 source: [msg 3362](../archive/inter-iit/2026-10.jsonl)

### Q4. Server connectivity via GCD > 1

There are N servers. Server i and server j are connected if gcd(server[i], server[j]) > 1. For each server, return the number of servers it is connected to (indirect connections also count). Constraints: N < 1e5, A[i] < 1e6.

Topics: Graphs, Math  
📎 source: [msg 3362](../archive/inter-iit/2026-10.jsonl)
