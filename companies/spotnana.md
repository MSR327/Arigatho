# Spotnana OA

## 2026-10-10 · IIT Delhi · FTE

### Q1. Minimize Tree Height by Re-attaching Edges

You are given a tree with n vertices rooted at vertex 1, and an integer max_operations. One operation: choose an edge (v, u), where v is the parent of u, remove it, and connect u (with its whole subtree) directly to the root. You may perform at most max_operations operations. The height of the tree is the maximum depth of any vertex (depth = number of edges from the root). Return the minimum possible height of the tree. (Same as Codeforces 1739D - Reset K Edges.)

Topics: Trees, Binary Search, Greedy  
📎 source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [msg 4842](../archive/inter-nit/2026-10.jsonl)

### Q2. Maximum Profit with Bitwise OR at Most K

You are given two arrays a and profits of length n, and an integer k. Item i has number a[i] and profit profits[i]. Choose any subset of items such that the bitwise OR of their a values is at most k. The profit of a subset is the sum of profits[i] over the chosen items. Return the maximum total profit. (Same as AtCoder Tenka1 2017 D - IntegerotS.)

Topics: Bit Manipulation, Greedy  
📎 source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [msg 4842](../archive/inter-nit/2026-10.jsonl)

### Q3. Subsequence With the Minimum Score

You are given two strings one and two. You may remove any number of characters from two; after the removals, two must be a subsequence of one. Score: if no character is removed, the score is 0. Otherwise, let first and last be the smallest and largest indices (in the original two) of the removed characters; the score is last - first + 1. Return the minimum possible score. (Same as LeetCode 2565 - Subsequence With the Minimum Score.)

Topics: Strings, Two Pointers, Binary Search  
📎 source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [msg 4842](../archive/inter-nit/2026-10.jsonl)

## 2026-10-09 · IIT Kanpur · FTE

### Q1. Shortest walk covering all required nodes in a tree

You are given an unweighted tree and a set of required vertices. Find the length of the shortest path that visits every required vertex. This is not a plain BFS/DFS: when the path backtracks, the backtracked steps also count. Example: the path 1-2-3-2-4 covers the required vertices, so the answer is 5. (Similar to Codeforces 592D Super M.)

Topics: Trees, Graphs  
📎 source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [msg 4587](../archive/inter-nit/2026-10.jsonl), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf)

### Q2. Train then execute: minimum days (or -1)

There are N ML algorithms. Each has a training time and must be fully trained before it can be executed. You are given a list of M days saying which algorithm can be executed on each day (the time slots in which each task must be completed). Find the minimum number of days needed to train and execute every algorithm, or return -1 if it is impossible. (Similar to LeetCode 3048 Earliest Second to Mark Indices I and Codeforces 732D Exams.)

Topics: Binary Search, Greedy  
📎 source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [msg 4587](../archive/inter-nit/2026-10.jsonl), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf)

### Q3. k-th largest OR over all subarrays

You are given an array. Take the bitwise OR of every contiguous subarray and return the k-th largest of these OR values. Generating every subarray's OR by brute force ran out of time or memory on 5 hidden test cases.

Topics: Bit Manipulation, Arrays, Sorting  
📎 source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [msg 4587](../archive/inter-nit/2026-10.jsonl), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf)
