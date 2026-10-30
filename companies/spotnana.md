# Spotnana

**8 questions** · 4 drives · latest 12 Oct 2026 · [7 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Binary Search](../topics/binary-search.md) 4 · [Trees](../topics/trees.md) 3 · [Greedy](../topics/greedy.md) 3 · [Graphs](../topics/graphs.md) 2 · [Bit Manipulation](../topics/bit-manipulation.md) 2 · [Heaps](../topics/heaps.md) 1 · [Strings](../topics/strings.md) 1 · [Two Pointers](../topics/two-pointers.md) 1 · +1 more  
**Seen at:** IIT Delhi, IIT Kanpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-12 · IIT Delhi · FTE](#2026-10-12--iit-delhi--fte)
  - [Spotnana OA format](#q1-spotnana-oa-format)
- [2026-10-10 · IIT Delhi · FTE](#2026-10-10--iit-delhi--fte)
  - [Minimize Tree Height by Re-attaching Edges](#q1-minimize-tree-height-by-re-attaching-edges)
  - [Maximum Profit with Bitwise OR at Most K](#q2-maximum-profit-with-bitwise-or-at-most-k)
  - [Subsequence With the Minimum Score](#q3-subsequence-with-the-minimum-score)
- [2026-10-10 · IIT Delhi · FTE · SDE](#2026-10-10--iit-delhi--fte--sde)
  - [Minimum travel distance visiting required tree nodes](#q1-minimum-travel-distance-visiting-required-tree-nodes)
- [2026-10-09 · IIT Kanpur · FTE](#2026-10-09--iit-kanpur--fte)
  - [Shortest walk covering all required nodes in a tree](#q1-shortest-walk-covering-all-required-nodes-in-a-tree)
  - [Train then execute: minimum days (or -1)](#q2-train-then-execute-minimum-days-or--1)
  - [k-th largest OR over all subarrays](#q3-k-th-largest-or-over-all-subarrays)

</details>

---

## 2026-10-12 · IIT Delhi · FTE

### Q1. Spotnana OA format

The OA is 1.5 hours long with 3 questions.

<sub>Topics: OA Format · Source: [chat, 12 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L158)</sub>

## 2026-10-10 · IIT Delhi · FTE

### Q1. Minimize Tree Height by Re-attaching Edges

You are given a tree with n vertices rooted at vertex 1, and an integer max_operations. One operation: choose an edge (v, u), where v is the parent of u, remove it, and connect u (with its whole subtree) directly to the root. You may perform at most max_operations operations. The height of the tree is the maximum depth of any vertex (depth = number of edges from the root). Return the minimum possible height of the tree. (Same as Codeforces 1739D - Reset K Edges.)

<sub>Topics: Trees, Binary Search, Greedy · Same problem: [Codeforces 1739D. Reset K Edges](https://codeforces.com/problemset/problem/1739/D) (rated 1900), binary search height, greedy edge cuts · Source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [chat, 10 Oct](../archive/inter-nit/2026-10.jsonl#L588) · Also asked at: IIT Delhi (2026-10-10)</sub>

### Q2. Maximum Profit with Bitwise OR at Most K

You are given two arrays a and profits of length n, and an integer k. Item i has number a[i] and profit profits[i]. Choose any subset of items such that the bitwise OR of their a values is at most k. The profit of a subset is the sum of profits[i] over the chosen items. Return the maximum total profit. (Same as AtCoder Tenka1 2017 D - IntegerotS.)

<sub>Topics: Bit Manipulation, Greedy · Same problem: [AtCoder TENKA1-2017 D. IntegerotS](https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_d), bitwise OR at most K via prefix-bit candidates · Source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [chat, 10 Oct](../archive/inter-nit/2026-10.jsonl#L588) · Also asked at: IIT Delhi (2026-10-10)</sub>

### Q3. Subsequence With the Minimum Score

You are given two strings one and two. You may remove any number of characters from two; after the removals, two must be a subsequence of one. Score: if no character is removed, the score is 0. Otherwise, let first and last be the smallest and largest indices (in the original two) of the removed characters; the score is last - first + 1. Return the minimum possible score. (Same as LeetCode 2565 - Subsequence With the Minimum Score.)

<sub>Topics: Strings, Two Pointers, Binary Search · Similar: [LeetCode 2565. Subsequence With the Minimum Score](https://leetcode.com/problems/subsequence-with-the-minimum-score/) (Hard) · Source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [chat, 10 Oct](../archive/inter-nit/2026-10.jsonl#L588) · Also asked at: IIT Delhi (2026-10-10)</sub>

## 2026-10-10 · IIT Delhi · FTE · SDE

### Q1. Minimum travel distance visiting required tree nodes

Given an undirected, unweighted, unrooted tree of 10^5 nodes. Given a list `required` of size m. You have to travel from node 1 to node n while also visiting every node in the `required` list at least once. Any node or edge can be used multiple times. Find the minimum distance for this.

<sub>Topics: Trees, Graphs · Close variant: [Codeforces 592D. Super M](https://codeforces.com/problemset/problem/592/D) (rated 2200), min walk visiting required tree nodes via diameter · Source: [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L224), [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L225), [Spotnana - OA_iitd_SDE.pdf](../archive/files/4936-Spotnana_-_OA_iitd_SDE.pdf) · Also asked at: IIT Kanpur (2026-10-09)</sub>

## 2026-10-09 · IIT Kanpur · FTE

### Q1. Shortest walk covering all required nodes in a tree

You are given an unweighted tree and a set of required vertices. Find the length of the shortest path that visits every required vertex. This is not a plain BFS/DFS: when the path backtracks, the backtracked steps also count. Example: the path 1-2-3-2-4 covers the required vertices, so the answer is 5. (Similar to Codeforces 592D Super M.)

<sub>Topics: Trees, Graphs · Same problem: [Codeforces 592D. Super M](https://codeforces.com/problemset/problem/592/D) (rated 2200), shortest walk covering required tree vertices via diameter · Source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [chat, 9 Oct](../archive/inter-nit/2026-10.jsonl#L616), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf)</sub>

### Q2. Train then execute: minimum days (or -1)

There are N ML algorithms. Each has a training time and must be fully trained before it can be executed. You are given a list of M days saying which algorithm can be executed on each day (the time slots in which each task must be completed). Find the minimum number of days needed to train and execute every algorithm, or return -1 if it is impossible. (Similar to LeetCode 3048 Earliest Second to Mark Indices I and Codeforces 732D Exams.)

<sub>Topics: Binary Search, Greedy · Similar: [LeetCode 3048. Earliest Second to Mark Indices I](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) (Medium) · Source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [chat, 9 Oct](../archive/inter-nit/2026-10.jsonl#L616), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf) · Also asked at: IIT Kanpur (2026-10-09), IIT Delhi (2026-10-10)</sub>

### Q3. k-th largest OR over all subarrays

You are given an array. Take the bitwise OR of every contiguous subarray and return the k-th largest of these OR values. Generating every subarray's OR by brute force ran out of time or memory on 5 hidden test cases.

<sub>Topics: Bit Manipulation, Binary Search, Heaps · Same idea: [LeetCode 898. Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/) (Medium), distinct subarray ORs per endpoint set · Source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [chat, 9 Oct](../archive/inter-nit/2026-10.jsonl#L616), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf) · Also asked at: IIT Kanpur (2026-10-09), IIT Delhi (2026-10-10)</sub>
