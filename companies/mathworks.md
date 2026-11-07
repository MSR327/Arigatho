# MathWorks

**13 questions** · 9 drives · latest 7 Nov 2026 · [6 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 5 · [Greedy](../topics/greedy.md) 5 · [Arrays](../topics/arrays.md) 4 · [Strings](../topics/strings.md) 3 · [Hashing](../topics/hashing.md) 2 · [Trees](../topics/trees.md) 1 · [Binary Search](../topics/binary-search.md) 1 · [Math](../topics/math.md) 1 · +6 more  
**Seen at:** BITS Pilani, IIT BHU, IIT Bombay, IIT Hyderabad, IIT Indore, VNIT Nagpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-07 · IIT BHU · FTE · Engineering track](#2026-11-07--iit-bhu--fte--engineering-track)
  - [MathWorks OA pattern (Computer Science and Engineering tracks)](#q1-mathworks-oa-pattern-computer-science-and-engineering-tracks)
- [2026-11-07 · BITS Pilani · FTE · Engineering track](#2026-11-07--bits-pilani--fte--engineering-track)
  - [MathWorks engineering track OA pattern](#q1-mathworks-engineering-track-oa-pattern)
- [2026-11-06 · IIT Indore · FTE](#2026-11-06--iit-indore--fte)
  - [Minimum swaps to sort using zero](#q1-minimum-swaps-to-sort-using-zero)
- [2026-11-06 · IIT Hyderabad · FTE](#2026-11-06--iit-hyderabad--fte)
  - [MathWorks OA pattern](#q1-mathworks-oa-pattern)
- [2026-11-05 · Unknown · FTE](#2026-11-05--unknown--fte)
  - [Maximum elements picked with at most one skip](#q1-maximum-elements-picked-with-at-most-one-skip)
  - [IBM get optimal string length](#q2-ibm-get-optimal-string-length)
  - [Minimum division operations to make array non-decreasing](#q3-minimum-division-operations-to-make-array-non-decreasing)
- [2026-11-05 · IIT Hyderabad · FTE · Engineering track](#2026-11-05--iit-hyderabad--fte--engineering-track)
  - [Count ancestor-descendant pairs within distance limit](#q1-count-ancestor-descendant-pairs-within-distance-limit)
- [2026-11-05 · IIT Bombay · FTE · Software](#2026-11-05--iit-bombay--fte--software)
  - [Minimum subsequences with a majority element](#q1-minimum-subsequences-with-a-majority-element)
  - [Count subarrays rearrangeable into palindromes](#q2-count-subarrays-rearrangeable-into-palindromes)
  - [Maximize beautiful substrings](#q3-maximize-beautiful-substrings)
- [2026-10-30 · VNIT Nagpur · FTE](#2026-10-30--vnit-nagpur--fte)
  - [MathWorks OA pattern](#q1-mathworks-oa-pattern-1)
- [2026-10-29 · VNIT Nagpur · FTE](#2026-10-29--vnit-nagpur--fte)
  - [MathWorks OA format](#q1-mathworks-oa-format)

</details>

---

## 2026-11-07 · IIT BHU · FTE · Engineering track

### Q1. MathWorks OA pattern (Computer Science and Engineering tracks)

90-minute interview/test. Choose exactly ONE track.

Computer Science: 3 coding questions; attempt all 3. Use TWO DIFFERENT programming languages across the 3 questions, chosen from C, C++, Java and JavaScript. Aptitude: basic math, problem solving and logical reasoning.

Engineering: basic concepts of Control Theory, Signal Processing and Embedded Systems. 2 coding questions, answered in C, C++, Java or JavaScript. Two different programming languages are encouraged, but the same language may be used for both questions. Aptitude: basic math, problem solving and logical reasoning.

<sub>Topics: OA Format, Control Systems, Signals & Systems · Source: [chat, 7 Nov](../archive/campus-iit-indore-placements/2026-11.jsonl#L95) · Also asked at: IIT BHU (2026-11-07)</sub>

## 2026-11-07 · BITS Pilani · FTE · Engineering track

### Q1. MathWorks engineering track OA pattern

Pattern: 3 DSA questions and MCQs.

<sub>Topics: OA Format · Source: [chat, 7 Nov](../archive/inter-nit/2026-11.jsonl#L772)</sub>

## 2026-11-06 · IIT Indore · FTE

### Q1. Minimum swaps to sort using zero

You are given an array `a` of `n` integers. The array contains exactly one `0`, and all other values are distinct and nonzero.

In one operation, you may swap the element `0` with any nonzero element. Find the minimum number of operations needed to sort the array in ascending order.

**Input**
- The first line contains an integer `n`.
- The second line contains `n` integers `a1, a2, ..., an`.

**Output**
Print the minimum number of swaps required to sort the array.

**Constraints**
- `1 ≤ n ≤ 10^5`
- The array contains exactly one `0`.
- All nonzero elements are distinct.

**Example**

Input
```text
5
4 0 2 1 3
```

Output
```text
6
```

<sub>Topics: Arrays, Greedy, Graphs · Source: [chat, 6 Nov](../archive/campus-iit-indore-placements/2026-11.jsonl#L82)</sub>

## 2026-11-06 · IIT Hyderabad · FTE

### Q1. MathWorks OA pattern

3 DSA questions and 5 aptitude MCQs.

<sub>Topics: OA Format · Source: [chat, 6 Nov](../archive/inter-nit/2026-11.jsonl#L742), [chat, 6 Nov](../archive/inter-nit/2026-11.jsonl#L743)</sub>

## 2026-11-05 · Unknown · FTE

### Q1. Maximum elements picked with at most one skip

You are given an array `arr` of n positive integers and an integer `k`, your available budget.

Starting from index 0, traverse the array from left to right. Follow these rules:

- If `arr[i] <= k`, you can pick that element and subtract its value from `k`.
- You may skip at most one element during the traversal without deducting its value from `k`.
- Once you have used your skip, you must continue picking elements in order as long as you can afford them.
- If you meet an element you cannot afford and have no skips left, the process stops.

Find the maximum number of elements you can pick.

Example 1:
```
arr = [2, 3, 8, 1, 2]
k = 8
Output: 4
```
Pick 2 (k=6), pick 3 (k=3), skip 8, pick 1 (k=2), pick 2 (k=0).

Example 2:
```
arr = [4, 2, 7, 3, 1]
k = 10
Output: 4
```
Pick 4 (k=6), pick 2 (k=4), skip 7, pick 3 (k=1), pick 1 (k=0).

Constraints (assumed by the poster):
```
1 <= n <= 10^5
1 <= arr[i]
1 <= k
```

<sub>Topics: Arrays, Greedy, Sliding Window · Same idea: [LeetCode 1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) (Medium), sliding window allowing limited skips · Source: [chat, 5 Nov](../archive/inter-iit/2026-11.jsonl#L230)</sub>

### Q2. IBM get optimal string length

Question 1 was the problem at fastprep.io 'ibm-get-optimal-string-length' (only the link was given, no statement).

<sub>Topics: Strings · Source: [chat, 5 Nov](../archive/campus-iit-hyderabad-placements/2026-11.jsonl#L73)</sub>

### Q3. Minimum division operations to make array non-decreasing

Question 2 was the LeetCode problem 'Minimum Division Operations to Make Array Non-Decreasing' (statement not reproduced by the poster).

<sub>Topics: Arrays, Greedy, Math · Similar: [LeetCode 3326. Minimum Division Operations to Make Array Non Decreasing](https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/) (Medium) · Source: [chat, 5 Nov](../archive/campus-iit-hyderabad-placements/2026-11.jsonl#L73)</sub>

## 2026-11-05 · IIT Hyderabad · FTE · Engineering track

### Q1. Count ancestor-descendant pairs within distance limit

You are given a tree with N nodes and N-1 edges. Each node has a value associated with it in the `val[]` array. Every edge has a distance (weight) associated with it. Find the count of every pair (u, v) such that u is an ancestor of v and distance(u, v) <= val[v].

Constraints: N <= 10^5

<sub>Topics: Trees, Binary Search · Same idea: [LeetCode 437. Path Sum III](https://leetcode.com/problems/path-sum-iii/) (Medium), count ancestor-descendant paths with weighted constraint via path prefix sums · Source: [chat, 5 Nov](../archive/campus-iit-bombay-placements/2026-11.jsonl#L95) · Also asked at: Unknown (2026-11-05), IIT Hyderabad ×3 (last 2026-11-06), BITS Pilani (2026-11-07)</sub>

## 2026-11-05 · IIT Bombay · FTE · Software

### Q1. Minimum subsequences with a majority element

You are given an integer array. Partition the array into the minimum possible number of subsequences such that every subsequence has a majority element.

A majority element is an element that occurs strictly more than half the length of that subsequence.

Find the minimum number of subsequences required.

**Note:** Every element must belong to exactly one subsequence.

<sub>Topics: Greedy, Arrays, Hashing · Same idea: [LeetCode 169. Majority Element](https://leetcode.com/problems/majority-element/) (Easy), majority element counting over frequencies · Source: [chat, 5 Nov](../archive/inter-nit/2026-11.jsonl#L514)</sub>

### Q2. Count subarrays rearrangeable into palindromes

You are given a vector of strings.

For each string, count the number of contiguous subarrays (substrings) whose characters can be rearranged to form a palindrome.

Return the count for each string.

<sub>Topics: Strings, Bit Manipulation, Hashing · Close variant: [LeetCode 1915. Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings/) (Medium), bitmask parity prefix counts for palindrome rearrangement · Source: [chat, 5 Nov](../archive/inter-nit/2026-11.jsonl#L514)</sub>

### Q3. Maximize beautiful substrings

You are given a string consisting of lowercase English letters (`a`–`z`) and dots (`.`).

Replace each dot with any lowercase English letter so that the total number of beautiful substrings is maximized.

A beautiful substring is a contiguous segment consisting entirely of identical characters.

**Input:** A string containing lowercase English letters and dots.

**Output:** An integer representing the maximum possible total number of beautiful substrings after replacing all dots.

Note: solutions must be implemented using at least two different programming languages across the three questions.

<sub>Topics: Strings, Greedy, DP · Same idea: [LeetCode 1759. Count Number of Homogenous Substrings](https://leetcode.com/problems/count-number-of-homogenous-substrings/) (Medium), count runs of identical characters substrings · Source: [chat, 5 Nov](../archive/inter-nit/2026-11.jsonl#L514)</sub>

## 2026-10-30 · VNIT Nagpur · FTE

### Q1. MathWorks OA pattern

2-3 DSA questions and some core subject MCQs were asked.

<sub>Topics: OA Format · Source: [chat, 30 Oct](../archive/campus-iit-patna-placements/2026-10.jsonl#L70) · Also asked at: VNIT Nagpur (2026-11-01)</sub>

## 2026-10-29 · VNIT Nagpur · FTE

### Q1. MathWorks OA format

3 DSA questions: one easy and the other two medium to hard. As far as the poster remembers, there was a binary search question and a DP question. The actual statements were not shared.

<sub>Topics: OA Format · Source: [chat, 29 Oct](../archive/campus-iit-patna-placements/2026-10.jsonl#L63), [chat, 29 Oct](../archive/campus-iit-patna-placements/2026-10.jsonl#L64), [chat, 29 Oct](../archive/campus-iit-patna-placements/2026-10.jsonl#L67) · Also asked at: IIT Hyderabad ×3 (last 2026-11-05), Unknown (2026-11-05)</sub>
