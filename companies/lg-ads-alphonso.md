# LG Ads (Alphonso)

**7 questions** · 2 drives · latest 22 Oct 2026 · [1 LeetCode match](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Arrays](../topics/arrays.md) 4 · [Math](../topics/math.md) 3 · [Sliding Window](../topics/sliding-window.md) 2 · [Hashing](../topics/hashing.md) 2 · [Heaps](../topics/heaps.md) 1 · [OA Format](../topics/oa-format.md) 1 · [DP](../topics/dp.md) 1 · [Strings](../topics/strings.md) 1  
**Seen at:** IIT BHU, IIT Madras

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-22 · IIT Madras · FTE](#2026-10-22--iit-madras--fte)
  - [OA format: MCQs and coding](#q1-oa-format-mcqs-and-coding)
  - [Assignments with no choice repeated more than k times in a row](#q2-assignments-with-no-choice-repeated-more-than-k-times-in-a-row)
  - [Minimum time to reach destination in 3D with periodic moves](#q3-minimum-time-to-reach-destination-in-3d-with-periodic-moves)
  - [Arrow through minimum number of boxes across layers](#q4-arrow-through-minimum-number-of-boxes-across-layers)
- [2026-10-21 · IIT BHU · FTE](#2026-10-21--iit-bhu--fte)
  - [Max sum subarray with exactly one repeated element](#q1-max-sum-subarray-with-exactly-one-repeated-element)
  - [Longest subarray with max-min <= D and sum <= B](#q2-longest-subarray-with-max-min--d-and-sum--b)
  - [Towers receiving a field in D-dimensional space](#q3-towers-receiving-a-field-in-d-dimensional-space)

</details>

---

## 2026-10-22 · IIT Madras · FTE

### Q1. OA format: MCQs and coding

12 MCQs, simple: SQL, OOPs, basic system design. Followed by 3 coding questions. Platform: HackerRank.

<sub>Topics: OA Format · Source: [chat, 22 Oct](../archive/campus-iit-ropar-placements/2026-10.jsonl#L30)</sub>

### Q2. Assignments with no choice repeated more than k times in a row

Given n slots and c choices for each slot, find the number of assignments such that no choice is repeated more than k times in a row.

Constraints:

- n up to 1e9
- c up to 1e9
- k up to 100

<sub>Topics: DP, Math · Source: [chat, 22 Oct](../archive/campus-iit-ropar-placements/2026-10.jsonl#L30)</sub>

### Q3. Minimum time to reach destination in 3D with periodic moves

Given a starting point and an ending point in 3D, and a string of moves consisting of L, R, U, D, F, B (movement in all 3 directions), find the minimum time to get from the start to the destination, or -1 if not possible. The movement specified by the string is periodic and each movement takes 1 time unit. During each time unit, you can also move in any one of the 6 directions as well.

<sub>Topics: Math, Strings · Source: [chat, 22 Oct](../archive/campus-iit-ropar-placements/2026-10.jsonl#L30)</sub>

### Q4. Arrow through minimum number of boxes across layers

Given n layers of boxes of the same height. Each layer's total width is the same, but the number of boxes inside a layer and their widths differ.

Example:

```
[1,3,3,1], [4,2], [1,3,2]
```

An arrow is fired from the top to hit a target at the bottom. Fire it so that it passes through the minimum number of boxes. If the arrow is fired between the gaps of boxes, it passes right through. For the example above, firing at index 4 lets the arrow pass through all 3 layers without hitting a box (the poster's wording).

Constraint: n up to 1e4.

<sub>Topics: Arrays, Hashing · Similar: [LeetCode 554. Brick Wall](https://leetcode.com/problems/brick-wall/) (Medium) · Source: [chat, 22 Oct](../archive/campus-iit-ropar-placements/2026-10.jsonl#L30)</sub>

## 2026-10-21 · IIT BHU · FTE

### Q1. Max sum subarray with exactly one repeated element

An array is given. Find the maximum sum of a valid subarray, where a valid subarray is one having exactly one element occurring twice and all other elements occurring once.

<sub>Topics: Arrays, Sliding Window, Hashing · Source: [chat, 21 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L203), [chat, 21 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L212)</sub>

### Q2. Longest subarray with max-min <= D and sum <= B

Find the maximum length of a subarray where the difference between the maximum and the minimum of that subarray is <= a given value D, and the sum of that subarray is <= a given value B.

<sub>Topics: Sliding Window, Arrays, Heaps · Source: [chat, 21 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L203), [chat, 21 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L212)</sub>

### Q3. Towers receiving a field in D-dimensional space

There are T towers, each located at a fixed coordinate in a D-dimensional space. The current position of a moving point at time t is a D-dimensional vector p[t]. At each time step, a field contributes a displacement determined by the current position. The field is described using two parameters, magnitude and direction.

In addition to the field displacement, each coordinate may change by an adjustment from {-1, 0, 1}. Let this adjustment vector be noise[t], where each of its D coordinates belongs to {-1, 0, 1}. The position update is:

```
p[t + 1] = p[t] + field(p[t], t) + noise[t]
```

Whenever the moving point reaches a tower's coordinate, that tower receives the field. Determine how many towers receive the field during the process.

Note: the poster gave only this description; the exact field definition, constraints and input format are missing.

<sub>Topics: Math, Arrays · Source: [chat, 21 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L203), [chat, 21 Oct](../archive/campus-iit-bhu-placements/2026-10.jsonl#L212)</sub>
