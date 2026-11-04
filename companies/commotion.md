# Commotion

**4 questions** · 1 drive · latest 3 Nov 2026 · [4 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Graphs](../topics/graphs.md) 3 · [Heaps](../topics/heaps.md) 2 · [DP](../topics/dp.md) 2 · [Binary Search](../topics/binary-search.md) 1 · [Sliding Window](../topics/sliding-window.md) 1 · [Strings](../topics/strings.md) 1 · [Hashing](../topics/hashing.md) 1 · [Bit Manipulation](../topics/bit-manipulation.md) 1  
**Seen at:** IIT Madras

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-03 · IIT Madras · FTE · ML Engineer](#2026-11-03--iit-madras--fte--ml-engineer)
  - [Cooling the Foundry Floor](#q1-cooling-the-foundry-floor)
  - [Smallest Covering Window](#q2-smallest-covering-window)
  - [Network Reliability Investigation](#q3-network-reliability-investigation)
  - [The Great Chai Stall Crawl](#q4-the-great-chai-stall-crawl)

</details>

---

## 2026-11-03 · IIT Madras · FTE · ML Engineer

### Q1. Cooling the Foundry Floor

A robotics team runs a square foundry floor divided into an n x n grid of tiles. Each tile (i, j) has been heated to a temperature given by grid[i][j].

A cooling system is switched on. After it runs for t seconds, every tile whose temperature is at most t has cooled down enough to be safe to stand on. A tile whose temperature is strictly greater than t is still too hot to touch.

An inspection robot starts on the top-left tile (0, 0). Each second the robot can step to a tile that shares an edge with its current tile (up, down, left, or right), but only if both the tile it is leaving and the tile it is entering are already safe (temperature at most t). Once tiles are safe, the robot can move across any number of them instantly, so travel between safe tiles takes no time. The robot must always stay inside the grid.

Determine the earliest second t at which the robot can reach the bottom-right tile (n - 1, n - 1).

**Input Format**
The first line contains a single integer n, the side length of the grid. Each of the next n lines contains n space-separated integers; the j-th value on the i-th of these lines is grid[i][j].

**Constraints**
- n == number of rows == number of columns
- 1 <= n <= 50
- 0 <= grid[i][j] < n^2
- Every value grid[i][j] is distinct.

**Output Format**
Print a single integer: the earliest second at which tile (n - 1, n - 1) becomes reachable from tile (0, 0).

Example:
```
Input:
2
0 2
1 3
Output:
3
```
At second 0 the robot sits on (0, 0); both neighbours are too hot. Only after 3 seconds are all tiles safe.

Other samples:
```
1
0
-> 0

2
0 1
3 2
-> 2
```

<sub>Topics: Graphs, Binary Search, Heaps · Similar: [LeetCode 778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) (Hard) · Source: [Q1.pdf](../archive/files/19648-Q1.pdf), [Q2.pdf](../archive/files/19649-Q2.pdf), [Q3.pdf](../archive/files/19650-Q3.pdf), [Q4.pdf](../archive/files/19651-Q4.pdf)</sub>

### Q2. Smallest Covering Window

You are given two strings, s (the text) and t (the pattern).

A substring of s is said to cover t if every character of t appears in that substring at least as many times as it appears in t. Repeated characters in t must be matched by the same number of occurrences in the substring.

Find the shortest substring of s that covers t.
- If no substring of s covers t, print -1.
- If several shortest substrings cover t, print the one that starts earliest in s.
- Characters are case-sensitive: 'a' and 'A' are different.

**Input Format**
The first line contains the string s. The second line contains the string t.

**Constraints**
- 1 ≤ |s|, |t| ≤ 10^5
- s and t consist only of uppercase and lowercase English letters.

**Output Format**
Print the shortest substring of s that covers t, or -1.

Example:
```
ADOBECODEBANC
ABC
```
Output:
```
BANC
```

<sub>Topics: Sliding Window, Strings, Hashing · Similar: [LeetCode 76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard) · Source: [Q1.pdf](../archive/files/19648-Q1.pdf), [Q2.pdf](../archive/files/19649-Q2.pdf), [Q3.pdf](../archive/files/19650-Q3.pdf), [Q4.pdf](../archive/files/19651-Q4.pdf)</sub>

### Q3. Network Reliability Investigation

An ML platform has n services connected by one-way network links. Each link has a positive latency. A diagnostic request must travel from service 1 to service n.

Among all routes with the minimum total latency, determine:
1. The minimum latency.
2. The number of minimum-latency routes, modulo 1,000,000,007.
3. The minimum number of links used by any minimum-latency route.
4. The maximum number of links used by any minimum-latency route.

Two routes are different if their sequences of links differ. The network may contain cycles, self-links, and duplicate links.

If service n cannot be reached from service 1, report -1 0 0 0. If n = 1, print 0 1 0 0.

**Input Format**
The first line contains two integers n and m. The next m lines each contain a, b, latency: a one-way link from a to b.

**Constraints**
- 1 ≤ n ≤ 100,000
- 0 ≤ m ≤ 200,000
- 1 ≤ latency ≤ 1,000,000,000
- 1 ≤ a, b ≤ n

**Output Format**
Four space-separated integers: minimum latency, number of minimum-latency routes mod 1,000,000,007, min links, max links.

Example 1:
```
4 5
1 2 1
1 3 1
2 4 1
3 4 1
1 4 2
```
Output:
```
2 3 1 2
```
Example 2:
```
3 1
1 2 5
```
Output:
```
-1 0 0 0
```
Example 3:
```
3 4
1 2 1
1 2 1
2 3 2
3 3 1
```
Output:
```
3 2 2 2
```

<sub>Topics: Graphs, Heaps, DP · Similar: [LeetCode 1976. Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) (Medium) · Source: [Q1.pdf](../archive/files/19648-Q1.pdf), [Q2.pdf](../archive/files/19649-Q2.pdf), [Q3.pdf](../archive/files/19650-Q3.pdf), [Q4.pdf](../archive/files/19651-Q4.pdf)</sub>

### Q4. The Great Chai Stall Crawl

Meera visits a market with n chai stalls, numbered 1 to n, connected by m one-way lanes, each with its own fare. She enters at stall 1 and must leave at stall n, tasting chai at every stall exactly once (stall 1 first, stall n last). Such a plan is a crawl. Two crawls are different if the sequences of lanes they use are different (parallel lanes between the same stalls count as different).

Output:
1. The number of different crawls, modulo 1,000,000,007.
2. The cheapest total fare among all crawls.

If no crawl exists, print 0 -1. If n = 1, print 1 0.

**Input Format**
The first line contains n and m. The next m lines each contain a, b, fare: a one-way lane from a to b.

**Constraints**
- 1 ≤ n ≤ 20
- 0 ≤ m ≤ n²
- 1 ≤ a, b ≤ n
- 1 ≤ fare ≤ 1,000,000
- Self-lanes and duplicate lanes may occur.

Example 1:
```
4 6
1 2 3
1 3 1
2 3 2
3 2 1
2 4 4
3 4 6
```
Output:
```
2 6
```
Example 2:
```
3 2
1 2 5
3 2 4
```
Output:
```
0 -1
```
Example 3:
```
3 3
1 2 5
1 2 3
2 3 4
```
Output:
```
2 7
```

<sub>Topics: DP, Bit Manipulation, Graphs · Close variant: [CSES: Hamiltonian Flights](https://cses.fi/problemset/task/1690), bitmask DP counting Hamiltonian paths from 1 to n · Source: [Q1.pdf](../archive/files/19648-Q1.pdf), [Q2.pdf](../archive/files/19649-Q2.pdf), [Q3.pdf](../archive/files/19650-Q3.pdf), [Q4.pdf](../archive/files/19651-Q4.pdf)</sub>
