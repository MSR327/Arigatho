# Visa

**6 questions** from 2 OA drives · seen at IIT BHU · latest 2026-10-26

**Topics:** [Graphs](../topics/graphs.md) (3) · [Math](../topics/math.md) (2) · [Bit Manipulation](../topics/bit-manipulation.md) (1) · [Greedy](../topics/greedy.md) (1) · [Trees](../topics/trees.md) (1) · [Binary Search](../topics/binary-search.md) (1) · [Sliding Window](../topics/sliding-window.md) (1) · [Hashing](../topics/hashing.md) (1)

**LeetCode matches:** 2 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-26 · IIT BHU · Intern](#2026-10-26--iit-bhu--intern) · 5 questions
- [2026-10-24 · IIT BHU · Intern](#2026-10-24--iit-bhu--intern) · 1 question

[← all companies](../README.md#companies)

---

## 2026-10-26 · IIT BHU · Intern

### Q1. Missed Chapters in Cyclic Teaching

Chapters are numbered from 0 to n-1. A teacher teaches one chapter every day and cycles indefinitely (after chapter n-1 comes chapter 0 again). A student misses class from day a to day b. Find how many chapters the student missed.

<sub>Topics: Math · Source: [chat, 26 Oct](../archive/inter-iit/2026-10.jsonl#L1038)</sub>

### Q2. Minimum K with Even Powers of 2

Given an array, for each element find the minimum k such that the element can be written as the sum of k numbers, where all numbers are > 0, exactly k-1 of them are even powers of 2 (excluding 2^0, i.e. 4, 16, 64, ...), and the remaining one number is 1, 2 or 3. If no such k exists for an element, output -1 for that element.

<sub>Topics: Math, Bit Manipulation, Greedy · Source: [chat, 26 Oct](../archive/inter-iit/2026-10.jsonl#L1038)</sub>

### Q3. Remove Node to Minimise Infection in Tree

Given a tree and an initially infected node. An infected node infects all its neighbours, and the infection keeps spreading. You may remove a single node from the tree. Find which node to remove to minimise the final number of infected nodes. Constraints: n &lt;= 1e3 (brute force over the removed node works).

<sub>Topics: Trees, Graphs · Source: [chat, 26 Oct](../archive/inter-iit/2026-10.jsonl#L1038)</sub>

### Q4. Count Timestamps in Last 10 Units

Given a list of timestamps a, for each a_i find the number of timestamps that happened between a_i - 10 and a_i.

<sub>Topics: Binary Search, Sliding Window · Similar: [LeetCode 933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) (Easy) · Source: [chat, 26 Oct](../archive/inter-iit/2026-10.jsonl#L1038)</sub>

### Q5. Max Common Friends Non-Friend

You are given which people are friends (as edges of a graph). For each person x, find a person y such that x and y have the maximum number of common friends and y is not already a friend of x. If no such y exists, output -1.

<sub>Topics: Graphs, Hashing · Source: [chat, 26 Oct](../archive/inter-iit/2026-10.jsonl#L1038)</sub>

## 2026-10-24 · IIT BHU · Intern

### Q1. Minimum Score of a Path Between Two Cities

Shared as one of the questions in the Visa SWE intern OA ("Minimum Path Score Between Cities"); matches LeetCode 2492. You are given n cities numbered 1 to n and a 2D array roads where roads[i] = [a, b, distance] is a bidirectional road between a and b with the given distance. The cities graph is not necessarily connected. The score of a path is the minimum distance of any road on that path. Return the minimum possible score of a path between cities 1 and n. A path may contain the same road or city multiple times, including cities 1 and n. It is guaranteed that there is at least one path between 1 and n. Constraints: 2 &lt;= n &lt;= 10^5, 1 &lt;= roads.length &lt;= 10^5, 1 &lt;= distance &lt;= 10^4. Example: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]] -> 5.

<sub>Topics: Graphs · Similar: [LeetCode 2492. Minimum Score of a Path Between Two Cities](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/) (Medium) · Source: [chat, 24 Oct](../archive/inter-iit/2026-10.jsonl#L904)</sub>
