# Meltwater

**6 questions** from 2 OA drives · seen at IIT Hyderabad, VIT Vellore · latest 2026-10-16

**Topics:** [DP](../topics/dp.md) (2) · [Strings](../topics/strings.md) (2) · [Math](../topics/math.md) (2) · [Greedy](../topics/greedy.md) (1) · [Hashing](../topics/hashing.md) (1) · [Sorting](../topics/sorting.md) (1) · [Arrays](../topics/arrays.md) (1)

**LeetCode matches:** 2 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-16 · IIT Hyderabad · FTE](#2026-10-16--iit-hyderabad--fte) · 3 questions
- [2026-10-13 · VIT Vellore · FTE](#2026-10-13--vit-vellore--fte) · 3 questions

[← all companies](../README.md#companies)

---

## 2026-10-16 · IIT Hyderabad · FTE

### Q1. Sum of First N Triangular Numbers

Given n, return the sum of the first n triangular numbers. (One of 2 easy questions. Different candidates got different questions, but the pattern was the same for both roles.)

<sub>Topics: Math · Source: [chat, 16 Oct](../archive/inter-iit/2026-10.jsonl#L491), [chat, 16 Oct](../archive/inter-iit/2026-10.jsonl#L492)</sub>

### Q2. Kth Character of Concatenated Sorted Unique Substrings

Given a string s_input and an integer k, take all unique substrings of s_input, sort them in lexicographical order and concatenate them. Return the k-th character of the resulting string.

<sub>Topics: Strings, Sorting · Source: [chat, 16 Oct](../archive/inter-iit/2026-10.jsonl#L491), [chat, 16 Oct](../archive/inter-iit/2026-10.jsonl#L492)</sub>

### Q3. Subarrays with GCD Equal to G

Hard question. You are given two arrays c and v and an integer g. Over all subarrays where the GCD of the c values equals g, compute: (1) the maximum sum of the v values of such a subarray, (2) how many such subarrays there are, and (3) the minimum length among all such subarrays.

<sub>Topics: Math, Arrays · Source: [chat, 16 Oct](../archive/inter-iit/2026-10.jsonl#L491), [chat, 16 Oct](../archive/inter-iit/2026-10.jsonl#L492)</sub>

## 2026-10-13 · VIT Vellore · FTE

### Q1. Remove Boxes (LeetCode 546)

Shared under the heading 'Meltwater and InMobi OA questions'; the post doesn't say which company asked which question. LeetCode 546 Remove Boxes: boxes of different colours are given as positive numbers. In each round you may remove some contiguous boxes of the same colour (k boxes, k >= 1) and earn k*k points. Return the maximum points you can get.

<sub>Topics: DP · Similar: [LeetCode 546. Remove Boxes](https://leetcode.com/problems/remove-boxes/) (Hard) · Source: [chat, 13 Oct](../archive/inter-iit/2026-10.jsonl#L136)</sub>

### Q2. Minimum Number of Taps to Open to Water a Garden (LeetCode 1326)

Shared under the heading 'Meltwater and InMobi OA questions'; the post doesn't say which company asked which question. LeetCode 1326: a one-dimensional garden spans [0, n] on the x-axis, with n+1 taps at points 0..n. Tap i can water the area [i - ranges[i], i + ranges[i]]. Return the minimum number of taps to open to water the whole garden, or -1 if that is impossible.

<sub>Topics: Greedy, DP · Similar: [LeetCode 1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) (Hard) · Source: [chat, 13 Oct](../archive/inter-iit/2026-10.jsonl#L136)</sub>

### Q3. The Bounded Substream

Shared under the heading 'Meltwater and InMobi OA questions'; the post doesn't say which company asked which question. Difficulty: Hard; time limit 2.0 s; memory limit 256 MB. You are given an infinitely large 1-D grid in which every position starts empty. You receive N commands; each gives a very large index and a character ('*' or a lowercase letter a-z) to place there. Whenever placing a character completes a bounded alphabet substring, print that alphabet substring immediately on a new line. A bounded alphabet substring matches the pattern *(alphabets)*, where (alphabets) is entirely contiguous lowercase letters with no empty spaces, immediately bounded by '*' on the left and on the right. Indices can be up to 10^18, so plain arrays cannot be used. Input: the first line is N; each of the next N lines is 'index character' (index is a 64-bit integer). Output: each time a fully bounded alphabet substring is formed, print its letters without the asterisks. Constraints: 1 &lt;= N &lt;= 10^5; 1 &lt;= index &lt;= 10^18; character in {*, a..z}; commands arrive in any order (indices are not sorted or contiguous); an index is never overwritten with a different character. Example input: 7 / 629464829 * / 629464831 * / 629464830 a / 1 * / 3 c / 2 b / 4 *. Output: a / bc. (The message's explanation is cut off.)

<sub>Topics: Hashing, Strings · Source: [chat, 13 Oct](../archive/inter-iit/2026-10.jsonl#L136)</sub>
