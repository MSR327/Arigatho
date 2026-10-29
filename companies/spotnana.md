# Spotnana

**13 questions** from 4 OA drives · seen at IIT Delhi, IIT Kanpur · latest 2026-10-12

**Topics:** [Binary Search](../topics/binary-search.md) (7) · [Greedy](../topics/greedy.md) (6) · [Trees](../topics/trees.md) (4) · [Bit Manipulation](../topics/bit-manipulation.md) (4) · [Graphs](../topics/graphs.md) (2) · [Strings](../topics/strings.md) (2) · [Two Pointers](../topics/two-pointers.md) (2) · [Heaps](../topics/heaps.md) (1) · [Arrays](../topics/arrays.md) (1) · [OA Format](../topics/oa-format.md) (1)

**LeetCode matches:** 3 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-12 · IIT Delhi · FTE](#2026-10-12--iit-delhi--fte) · 1 question
- [2026-10-10 · IIT Delhi · FTE](#2026-10-10--iit-delhi--fte) · 3 questions
- [2026-10-10 · IIT Delhi · FTE · SDE](#2026-10-10--iit-delhi--fte--sde) · 6 questions
- [2026-10-09 · IIT Kanpur · FTE](#2026-10-09--iit-kanpur--fte) · 3 questions

[← all companies](../README.md#companies)

---

## 2026-10-12 · IIT Delhi · FTE

### Q1. Spotnana OA format

The OA is 1.5 hours long with 3 questions.

<sub>Topics: OA Format · Source: [chat, 12 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L158)</sub>

## 2026-10-10 · IIT Delhi · FTE

### Q1. Minimize Tree Height by Re-attaching Edges

You are given a tree with n vertices rooted at vertex 1, and an integer max_operations. One operation: choose an edge (v, u), where v is the parent of u, remove it, and connect u (with its whole subtree) directly to the root. You may perform at most max_operations operations. The height of the tree is the maximum depth of any vertex (depth = number of edges from the root). Return the minimum possible height of the tree. (Same as Codeforces 1739D - Reset K Edges.)

<sub>Topics: Trees, Binary Search, Greedy · Source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [chat, 10 Oct](../archive/inter-nit/2026-10.jsonl#L588)</sub>

### Q2. Maximum Profit with Bitwise OR at Most K

You are given two arrays a and profits of length n, and an integer k. Item i has number a[i] and profit profits[i]. Choose any subset of items such that the bitwise OR of their a values is at most k. The profit of a subset is the sum of profits[i] over the chosen items. Return the maximum total profit. (Same as AtCoder Tenka1 2017 D - IntegerotS.)

<sub>Topics: Bit Manipulation, Greedy · Source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [chat, 10 Oct](../archive/inter-nit/2026-10.jsonl#L588)</sub>

### Q3. Subsequence With the Minimum Score

You are given two strings one and two. You may remove any number of characters from two; after the removals, two must be a subsequence of one. Score: if no character is removed, the score is 0. Otherwise, let first and last be the smallest and largest indices (in the original two) of the removed characters; the score is last - first + 1. Return the minimum possible score. (Same as LeetCode 2565 - Subsequence With the Minimum Score.)

<sub>Topics: Strings, Two Pointers, Binary Search · Similar: [LeetCode 2565. Subsequence With the Minimum Score](https://leetcode.com/problems/subsequence-with-the-minimum-score/) (Hard) · Source: [Spotnana - OA_iitd_SDE.pdf](../archive/files/4841-Spotnana_-_OA_iitd_SDE.pdf), [chat, 10 Oct](../archive/inter-nit/2026-10.jsonl#L588)</sub>

## 2026-10-10 · IIT Delhi · FTE · SDE

### Q1. Minimum travel distance visiting required tree nodes

Given an undirected, unweighted, unrooted tree of 10^5 nodes. Given a list `required` of size m. You have to travel from node 1 to node n while also visiting every node in the `required` list at least once. Any node or edge can be used multiple times. Find the minimum distance for this.

<sub>Topics: Trees, Graphs · Source: [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L224), [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L225), [Spotnana - OA_iitd_SDE.pdf](../archive/files/4936-Spotnana_-_OA_iitd_SDE.pdf)</sub>

### Q2. Kth largest OR over all subarrays

Given an array `arr` of size 10^5 with arr[i] < 1024. Return the k-th largest OR among all subarrays. More formally, for an array of size n there are n*(n-1)/2 subarrays and that many ORs; return the k-th largest. k <= n*(n-1)/2.

<sub>Topics: Bit Manipulation, Arrays · Source: [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L224), [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L225), [Spotnana - OA_iitd_SDE.pdf](../archive/files/4936-Spotnana_-_OA_iitd_SDE.pdf)</sub>

### Q3. Minimum days to train and deploy all ML models

There are n machine learning models. Each model has a list of size m of days on which it can be deployed. It can only be deployed once and deployment takes 1 day (it can be deployed only on one of its given m days). Given a list of size n, the number of days required to train the i-th model. A model can't be deployed before training for its required number of days (can't train less or more than given for any model). Return the minimum number of days to deploy all the models, or -1 if it can't be done.

<sub>Topics: Binary Search, Greedy · Source: [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L224), [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L225), [Spotnana - OA_iitd_SDE.pdf](../archive/files/4936-Spotnana_-_OA_iitd_SDE.pdf)</sub>

### Q4. Minimize tree height by re-attaching edges to root

You are given a tree with n vertices rooted at vertex 1, and an integer `max_operations`.

- One operation: choose an edge (v, u), where v is the parent of u, remove it, and connect u (with its whole subtree) directly to the root.
- You may perform at most `max_operations` operations.
- The height of the tree is the maximum depth of any vertex (depth = number of edges from the root).

Return the minimum possible height of the tree.

(Practice equivalent per the PDF: Codeforces 1739D, Reset K Edges.)

<sub>Topics: Trees, Greedy, Binary Search · Source: [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L224), [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L225), [Spotnana - OA_iitd_SDE.pdf](../archive/files/4936-Spotnana_-_OA_iitd_SDE.pdf)</sub>

### Q5. Maximum profit with bitwise OR at most K

You are given two arrays `a` and `profits` of length n, and an integer k. Item i has number `a[i]` and profit `profits[i]`.

- Choose any subset of items such that the bitwise OR of their `a` values is at most k.
- The profit of a subset is the sum of `profits[i]` over the chosen items.

Return the maximum total profit.

(Practice equivalent per the PDF: AtCoder Tenka1 2017 D, IntegerotS.)

<sub>Topics: Bit Manipulation, Greedy · Source: [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L224), [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L225), [Spotnana - OA_iitd_SDE.pdf](../archive/files/4936-Spotnana_-_OA_iitd_SDE.pdf)</sub>

### Q6. Subsequence with the minimum score

You are given two strings `one` and `two`. You may remove any number of characters from `two`.

- After the removals, `two` must be a subsequence of `one`.
- Score: if no character is removed, the score is 0. Otherwise, let first and last be the smallest and largest indices (in the original `two`) of the removed characters; the score is last - first + 1.

Return the minimum possible score.

<sub>Topics: Strings, Two Pointers, Binary Search · Similar: [LeetCode 2565. Subsequence With the Minimum Score](https://leetcode.com/problems/subsequence-with-the-minimum-score/) (Hard) · Source: [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L224), [chat, 9 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L225), [Spotnana - OA_iitd_SDE.pdf](../archive/files/4936-Spotnana_-_OA_iitd_SDE.pdf)</sub>

## 2026-10-09 · IIT Kanpur · FTE

### Q1. Shortest walk covering all required nodes in a tree

You are given an unweighted tree and a set of required vertices. Find the length of the shortest path that visits every required vertex. This is not a plain BFS/DFS: when the path backtracks, the backtracked steps also count. Example: the path 1-2-3-2-4 covers the required vertices, so the answer is 5. (Similar to Codeforces 592D Super M.)

<sub>Topics: Trees, Graphs · Source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [chat, 9 Oct](../archive/inter-nit/2026-10.jsonl#L616), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf)</sub>

### Q2. Train then execute: minimum days (or -1)

There are N ML algorithms. Each has a training time and must be fully trained before it can be executed. You are given a list of M days saying which algorithm can be executed on each day (the time slots in which each task must be completed). Find the minimum number of days needed to train and execute every algorithm, or return -1 if it is impossible. (Similar to LeetCode 3048 Earliest Second to Mark Indices I and Codeforces 732D Exams.)

<sub>Topics: Binary Search, Greedy · Similar: [LeetCode 3048. Earliest Second to Mark Indices I](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) (Medium) · Source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [chat, 9 Oct](../archive/inter-nit/2026-10.jsonl#L616), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf)</sub>

### Q3. k-th largest OR over all subarrays

You are given an array. Take the bitwise OR of every contiguous subarray and return the k-th largest of these OR values. Generating every subarray's OR by brute force ran out of time or memory on 5 hidden test cases.

<sub>Topics: Bit Manipulation, Binary Search, Heaps · Source: [membased spotnana.pdf](../archive/files/4530-membased_spotnana.pdf), [chat, 9 Oct](../archive/inter-nit/2026-10.jsonl#L616), [membased spotnana.pdf](../archive/files/4597-membased_spotnana.pdf)</sub>
