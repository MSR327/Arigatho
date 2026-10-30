# Calix

**4 questions** · 1 drive · latest 22 Sep 2026 · [3 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 1 · [DP](../topics/dp.md) 1 · [Math](../topics/math.md) 1 · [Stack/Queue](../topics/stack-queue.md) 1 · [Arrays](../topics/arrays.md) 1 · [Bit Manipulation](../topics/bit-manipulation.md) 1 · [Hashing](../topics/hashing.md) 1  
**Seen at:** IIT Dhanbad

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-09-22 · IIT Dhanbad · FTE](#2026-09-22--iit-dhanbad--fte)
  - [OA format: topics asked](#q1-oa-format-topics-asked)
  - [Signal Transmission Between Towers](#q2-signal-transmission-between-towers)
  - [Airplane Collision](#q3-airplane-collision)
  - [Largest group of strings differing by one character](#q4-largest-group-of-strings-differing-by-one-character)

</details>

---

## 2026-09-22 · IIT Dhanbad · FTE

### Q1. OA format: topics asked

The OA had three coding questions:

- 1 easy implementation
- 1 medium-hard bitset problem
- 1 hard DP on graph problem

<sub>Topics: OA Format · Source: [chat, 26 Sep](../archive/calix-oa/2026-09.jsonl#L7), [chat, 2 Oct](../archive/calix-oa/2026-10.jsonl#L2)</sub>

### Q2. Signal Transmission Between Towers

You are given N towers arranged in a straight line from left to right. The towers are numbered 1 to N.
Each tower i has an activation energy a[i].

A signal starts at Tower 1 and must reach Tower N.

If the signal is transferred from Tower j to Tower i (j < i), the cost is:

(i−j)² + a[i]

where (i−j)² is the cost of travelling between the towers, and a[i] is the activation energy required at the destination tower i.

You may also skip a tower. Skipping a tower costs a fixed amount X.

Find the minimum total cost required to transfer the signal from Tower 1 to Tower N.

**Input**

The first line contains two integers N and X.
The second line contains N integers a[1], a[2], ..., a[N].

**Output**

Print the minimum cost to reach Tower N.

**Constraints**

```
1 ≤ N ≤ 2 × 10^5
1 ≤ a[i], X ≤ 10^9
```

<sub>Topics: DP, Math · Same idea: [AtCoder DP Z. Frog 3](https://atcoder.jp/contests/dp/tasks/dp_z), DP with squared cost, convex hull trick · Source: [chat, 26 Sep](../archive/calix-oa/2026-09.jsonl#L7), [chat, 2 Oct](../archive/calix-oa/2026-10.jsonl#L2)</sub>

### Q3. Airplane Collision

You are given N airplanes arranged in a straight line from left to right. Each airplane has a momentum p[i].

- If p[i] < 0, airplane i is moving west (left).
- If p[i] > 0, airplane i is moving east (right).
- The absolute value |p[i]| represents its momentum magnitude.

When two airplanes moving toward each other collide, the airplane with larger momentum magnitude survives. The surviving airplane continues moving in its original direction.

The positions of the airplanes are given by their order in the array, from left to right.

Determine the number of airplanes remaining after all possible collisions.

```
n <= 2e5
```

<sub>Topics: Stack/Queue, Arrays · Similar: [LeetCode 735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) (Medium) · Source: [chat, 26 Sep](../archive/calix-oa/2026-09.jsonl#L7), [chat, 2 Oct](../archive/calix-oa/2026-10.jsonl#L2)</sub>

### Q4. Largest group of strings differing by one character

Given a set of strings, find the maximum group size where all strings' alphabet sets differ by exactly 1 character.

```
n <= 1e4
length of string <= 20
t <= 10
```

The poster only half-remembered this one; the exact statement and examples are missing.

<sub>Topics: Bit Manipulation, Hashing · Same idea: [LeetCode 1554. Strings Differ by One Character](https://leetcode.com/problems/strings-differ-by-one-character/) (Medium), group strings differing by one character via hashing · Source: [chat, 26 Sep](../archive/calix-oa/2026-09.jsonl#L7), [chat, 2 Oct](../archive/calix-oa/2026-10.jsonl#L2)</sub>
