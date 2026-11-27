# DE Shaw

**6 questions** · 4 drives · latest 26 Nov 2026 · [3 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 2 · [Bit Manipulation](../topics/bit-manipulation.md) 2 · [Sorting](../topics/sorting.md) 1 · [Arrays](../topics/arrays.md) 1 · [Sliding Window](../topics/sliding-window.md) 1 · [Heaps](../topics/heaps.md) 1 · [Greedy](../topics/greedy.md) 1 · [DP](../topics/dp.md) 1 · +3 more  
**Seen at:** IIT BHU, IIT Kharagpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-26 · Unknown · Unknown · Interview](#2026-11-26--unknown--unknown--interview)
  - [DE Shaw interview topics](#q1-de-shaw-interview-topics)
- [2026-11-26 · IIT Kharagpur · FTE](#2026-11-26--iit-kharagpur--fte)
  - [Interval Coverage XOR](#q1-interval-coverage-xor)
  - [Sliding Window k-th Minimum](#q2-sliding-window-k-th-minimum)
  - [Maximum Profit with Power-of-Two Costs](#q3-maximum-profit-with-power-of-two-costs)
- [2026-11-25 · IIT BHU · FTE](#2026-11-25--iit-bhu--fte)
  - [DE Shaw OA had three DSA questions](#q1-de-shaw-oa-had-three-dsa-questions)
- [2026-07-01 · Unknown · FTE](#2026-07-01--unknown--fte)
  - [DE Shaw OA pattern (summary of shared experiences)](#q1-de-shaw-oa-pattern-summary-of-shared-experiences)

</details>

---

## 2026-11-26 · Unknown · Unknown · Interview

### Q1. DE Shaw interview topics

Summary based on 5 experiences: interviews were mostly DSA + OS, networks, C++, projects and puzzles.

The exact questions are not given.

<sub>Topics: OS/DBMS/CN MCQ, Puzzles, HR & Behavioral · Source: [chat, 26 Nov](../archive/campus-iit-roorkee-placements/2026-11.jsonl#L740)</sub>

## 2026-11-26 · IIT Kharagpur · FTE

### Q1. Interval Coverage XOR

You are given n closed intervals `[start[i], end[i]]` for `0 <= i < n`, where every endpoint lies within `[1, m]`. For each integer x in `[1, m]`, let `F[x]` denote the number of intervals that cover x (i.e., `start[i] <= x <= end[i]`). Compute and return the bitwise XOR of all values `F[1], F[2], ..., F[m]`:

```
F[1] XOR F[2] XOR ... XOR F[m]
```

Constraints:
- `1 <= n <= 10^5`
- `1 <= m <= 10^9`
- `1 <= start[i] <= end[i] <= m`

<sub>Topics: Sorting, Bit Manipulation, Arrays · Same idea: [LeetCode 1943. Describe the Painting](https://leetcode.com/problems/describe-the-painting/) (Medium), sweep line over segments with constant interval coverage · Source: [chat, 26 Nov](../archive/inter-nit/2026-11.jsonl#L2699)</sub>

### Q2. Sliding Window k-th Minimum

You are given an array `nums` of n integers along with two integers m and k. Slide a contiguous window of size m across the array from left to right, one position at a time. For each window, find its k-th smallest element (1-indexed) and return an array containing these `n - m + 1` values.

Constraints:
- `1 <= n <= 10^5`
- `1 <= k <= m <= n`
- `-10^9 <= nums[i] <= 10^9`

<sub>Topics: Sliding Window, Heaps · Similar: [LeetCode 2653. Sliding Subarray Beauty](https://leetcode.com/problems/sliding-subarray-beauty/) (Medium) · Source: [chat, 26 Nov](../archive/inter-nit/2026-11.jsonl#L2699)</sub>

### Q3. Maximum Profit with Power-of-Two Costs

You are given two arrays A and B of length n, and an integer budget W. Each item i (`0 <= i < n`) has a cost of `2^A[i]` and yields a profit of `B[i]`, and each item can be selected at most once. Determine the maximum total profit you can obtain without the total cost of selected items exceeding W.

Constraints:
- `1 <= n < 10^5`
- `0 <= A[i] <= 60`
- `0 <= B[i] <= 10^9`
- `0 <= W <= 10^18`

<sub>Topics: Greedy, DP, Bit Manipulation · Same idea: [LeetCode 2835. Minimum Operations to Form Subsequence With Target Sum](https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/) (Hard), bit-by-bit greedy over power-of-two sizes · Source: [chat, 26 Nov](../archive/inter-nit/2026-11.jsonl#L2699)</sub>

## 2026-11-25 · IIT BHU · FTE

### Q1. DE Shaw OA had three DSA questions

The OA had three DSA questions.

The actual questions are not given.

<sub>Topics: OA Format · Source: [chat, 25 Nov](../archive/inter-nit/2026-11.jsonl#L2561)</sub>

## 2026-07-01 · Unknown · FTE

### Q1. DE Shaw OA pattern (summary of shared experiences)

Summary compiled from shared experiences:

- OA was in July (exact day not given).
- 3 hard coding questions, CP style (from 5 shared experiences).
- Mostly graph + DP, with one greedy (from 4 experiences).
- People shared solving 2 of the 3 (from 3 experiences).

The actual questions are not given.

<sub>Topics: OA Format · Source: [chat, 25 Nov](../archive/inter-nit/2026-11.jsonl#L2560) · Also asked at: Unknown ×2 (last 2026-11-26)</sub>
