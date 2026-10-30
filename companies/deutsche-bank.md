# Deutsche Bank

**17 questions** · 8 drives · latest 30 Oct 2026 · [1 LeetCode match](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Arrays](../topics/arrays.md) 5 · [Recursion/Backtracking](../topics/recursion-backtracking.md) 4 · [Strings](../topics/strings.md) 3 · [Two Pointers](../topics/two-pointers.md) 2 · [Graphs](../topics/graphs.md) 2 · [Trees](../topics/trees.md) 2 · [Sorting](../topics/sorting.md) 2 · [OA Format](../topics/oa-format.md) 2 · +5 more  
**Seen at:** IIT Delhi, IIT Guwahati, IIT Kanpur, IIT Kharagpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-30 · IIT Guwahati · FTE](#2026-10-30--iit-guwahati--fte)
  - [Maximise sum of unique building heights](#q1-maximise-sum-of-unique-building-heights)
  - [Minimum cars to remove for bridge crossing](#q2-minimum-cars-to-remove-for-bridge-crossing)
  - [Count anagrams without identical adjacent characters](#q3-count-anagrams-without-identical-adjacent-characters)
- [2026-10-29 · IIT Guwahati · FTE](#2026-10-29--iit-guwahati--fte)
  - [Count anagrams](#q1-count-anagrams)
  - [Frog Jump 2 type problem](#q2-frog-jump-2-type-problem)
- [2026-10-16 · IIT Kharagpur · FTE](#2026-10-16--iit-kharagpur--fte)
  - [OA pattern: 3 DSA questions](#q1-oa-pattern-3-dsa-questions)
- [2026-10-16 · IIT Kanpur · FTE](#2026-10-16--iit-kanpur--fte)
  - [Tree DFS bringing result up](#q1-tree-dfs-bringing-result-up)
  - [Standard BFS on a graph](#q2-standard-bfs-on-a-graph)
  - [Single pass over a string checking a condition](#q3-single-pass-over-a-string-checking-a-condition)
- [2026-10-15 · IIT Kharagpur · FTE](#2026-10-15--iit-kharagpur--fte)
  - [Deutsche Bank OA format](#q1-deutsche-bank-oa-format)
- [2026-10-15 · IIT Kanpur · FTE](#2026-10-15--iit-kanpur--fte)
  - [Palindrome with Question Marks](#q1-palindrome-with-question-marks)
  - [Ambulance Arrival Time](#q2-ambulance-arrival-time)
  - [Largest Perfect Subtree](#q3-largest-perfect-subtree)
- [2026-10-15 · IIT Guwahati · FTE · Graduate Analyst](#2026-10-15--iit-guwahati--fte--graduate-analyst)
  - [N queens in a row (DSA question)](#q1-n-queens-in-a-row-dsa-question)
- [2026-10-15 · IIT Delhi · FTE](#2026-10-15--iit-delhi--fte)
  - [Largest Magic Square in Matrix](#q1-largest-magic-square-in-matrix)
  - [Domino Arrangement with Matching Columns](#q2-domino-arrangement-with-matching-columns)
  - [Max Sum of Two Cells Not in Same Row/Column](#q3-max-sum-of-two-cells-not-in-same-rowcolumn)

</details>

---

## 2026-10-30 · IIT Guwahati · FTE

### Q1. Maximise sum of unique building heights

Given an array where each element describes the maximum height a building is allowed to have. Construct all buildings such that their heights are unique and the total sum is maximised. Return the total sum.

```
Input: [2,5,9,9,12,12,12,15]
Output: (15+12+11+10+9+8+5+2)
```

<sub>Topics: Greedy, Sorting, Arrays · Source: [chat, 30 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L505) · Also asked at: IIT Guwahati (2026-10-30)</sub>

### Q2. Minimum cars to remove for bridge crossing

You are given an integer array `weights` of size N, where `weights[i]` represents the weight of the i-th car, and an integer `maxWeight`, representing the maximum total weight the bridge can support.

At most two cars can be on the bridge at any given time. Whenever two cars are on the bridge together, the sum of their weights must not exceed `maxWeight`. Determine the minimum number of cars that must be removed so that all remaining cars can cross the bridge safely, while preserving their original order.

Example 1:
```
Input: weights = [1, 2, 5, 2, 1], maxWeight = 6
Output: 1
```
Remove the car with weight 5. The remaining cars can cross without violating the bridge's weight limit.

Example 2:
```
Input: weights = [3, 7, 2, 4, 5], maxWeight = 8
Output: 2
```
Remove the cars with weights 7 and 5.

Example 3:
```
Input: weights = [4, 4, 4, 4], maxWeight = 7
Output: 4
```
Any two cars together weigh 8, which exceeds the capacity. Therefore every car must be removed if the requirement is that two cars must always be allowed on the bridge simultaneously.

Constraints:
- 1 ≤ N ≤ 10^5
- 1 ≤ weights[i] ≤ 10^9
- 1 ≤ maxWeight ≤ 10^9

<sub>Topics: Arrays, Greedy, Two Pointers · Source: [Deutsche_Bank_IIT_Guwahati_Problems.pdf](../archive/files/16267-Deutsche_Bank_IIT_Guwahati_Problems.pdf)</sub>

### Q3. Count anagrams without identical adjacent characters

You are given a string `s` consisting of lowercase English letters (a–z). Count the number of distinct anagrams of `s` in which no two consecutive characters are the same. Two anagrams are considered distinct if their resulting strings are different.

Example 1:
```
Input: s = "aab"
Output: 1
```
The distinct anagrams are "aab", "aba", and "baa". Only "aba" satisfies the condition.

Example 2:
```
Input: s = "aabc"
Output: 6
```
There are 12 distinct anagrams of "aabc". Exactly 6 have no two identical consecutive characters.

Example 3:
```
Input: s = "aaa"
Output: 0
```

Example 4:
```
Input: s = "abc"
Output: 6
```

Constraints:
- 1 ≤ |s| ≤ 50
- s contains only lowercase English letters (a–z).
- The answer is guaranteed to be at most 2000.

<sub>Topics: DP, Recursion/Backtracking, Math · Source: [Deutsche_Bank_IIT_Guwahati_Problems.pdf](../archive/files/16267-Deutsche_Bank_IIT_Guwahati_Problems.pdf)</sub>

## 2026-10-29 · IIT Guwahati · FTE

### Q1. Count anagrams

Finding the number of anagrams (poster says it can be found on LeetCode). Exact statement not given.

<sub>Topics: Strings, Hashing · Source: [chat, 29 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L490)</sub>

### Q2. Frog Jump 2 type problem

A "frog jump 2" type question. Exact statement not given.

<sub>Topics: Arrays, DP · Source: [chat, 29 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L490)</sub>

## 2026-10-16 · IIT Kharagpur · FTE

### Q1. OA pattern: 3 DSA questions

Deutsche Bank OA (IIT Kharagpur) had 3 DSA questions: 1 tough and 2 easy-to-medium.

<sub>Topics: OA Format · Source: [chat, 16 Oct](../archive/inter-iit/2026-10.jsonl#L508) · Also asked at: IIT Guwahati ×2 (last 2026-10-29), Unknown (2026-10-29)</sub>

## 2026-10-16 · IIT Kanpur · FTE

### Q1. Tree DFS bringing result up

Given a tree, run a DFS on it to compute a result and bring the result up. (Poster did not remember the exact statement.)

<sub>Topics: Trees · Source: [chat, 16 Oct](../archive/campus-iit-kanpur-placements/2026-10.jsonl#L106)</sub>

### Q2. Standard BFS on a graph

A standard BFS problem on a graph. (Poster did not remember the exact statement.)

<sub>Topics: Graphs · Source: [chat, 16 Oct](../archive/campus-iit-kanpur-placements/2026-10.jsonl#L106)</sub>

### Q3. Single pass over a string checking a condition

Iterate over a string once, checking a condition. (Poster did not remember the exact statement.) The allotted time was 1h30m but it only needed 25-30 minutes; the questions were easy.

<sub>Topics: Strings · Source: [chat, 16 Oct](../archive/campus-iit-kanpur-placements/2026-10.jsonl#L106)</sub>

## 2026-10-15 · IIT Kharagpur · FTE

### Q1. Deutsche Bank OA format

The OA contained only behavioral questions. The test link was emailed and could be taken from the student's room any time before the 14 Oct 6pm deadline.

<sub>Topics: OA Format, HR & Behavioral · Source: [chat, 15 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L126)</sub>

## 2026-10-15 · IIT Kanpur · FTE

### Q1. Palindrome with Question Marks

Given a string S containing lowercase English letters and '?', replace every '?' with a lowercase letter so that the resulting string is a palindrome. Return any valid palindrome, or "NO" if it is impossible.

<sub>Topics: Strings, Two Pointers · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L1247)</sub>

### Q2. Ambulance Arrival Time

A city has N districts connected by M undirected streets. Arrays A and B describe the streets (street i connects A[i] and B[i]), and array H lists the districts that contain hospitals. Each street takes one minute to travel. Find the maximum, over all districts, of the shortest travel time to the nearest hospital. Return -1 if any district cannot be reached from a hospital.

<sub>Topics: Graphs · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L1247)</sub>

### Q3. Largest Perfect Subtree

Given a non-empty binary tree, find the size of the largest perfect subtree you can get by removing nodes. In a perfect binary tree every internal node has exactly two children and all leaves are at the same depth. Return the maximum number of nodes in such a subtree.

<sub>Topics: Trees, Recursion/Backtracking · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L1247)</sub>

## 2026-10-15 · IIT Guwahati · FTE · Graduate Analyst

### Q1. N queens in a row (DSA question)

A DSA question about placing N queens in a row was reportedly asked in the Deutsche Bank Graduate Analyst OA (said to be from the Striver sheet, from last year's test).

The full problem statement was not given.

<sub>Topics: Recursion/Backtracking · Source: [chat, 15 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L118)</sub>

## 2026-10-15 · IIT Delhi · FTE

### Q1. Largest Magic Square in Matrix

Given an m x n matrix, find the size of the largest magic square inside it. A magic square is a k x k submatrix where every row sum, every column sum and both main diagonal sums are equal. A single cell is the smallest possible magic square. Constraints: M, N &lt;= 20, so brute force over all square submatrices works.

<sub>Topics: Arrays · Similar: [LeetCode 1895. Largest Magic Square](https://leetcode.com/problems/largest-magic-square/) (Medium) · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L1300)</sub>

### Q2. Domino Arrangement with Matching Columns

You are given 6 dominoes. Each domino is a rectangle made of two square halves, and each half has a number. You may rotate the dominoes any way. Decide whether they can be arranged in the given layout so that every column formed shows the same number on its face. (The poster tried all permutations and rotations and checked each one.)

<sub>Topics: Recursion/Backtracking · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L1300)</sub>

### Q3. Max Sum of Two Cells Not in Same Row/Column

Given an m x n matrix of integers, pick two numbers that are not in the same row and not in the same column. Return the largest possible sum of the two numbers.

<sub>Topics: Arrays, Sorting · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L1300)</sub>
