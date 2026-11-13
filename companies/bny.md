# BNY

**8 questions** · 6 drives · latest 12 Nov 2026 · [5 practice problems](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 4 · [Arrays](../topics/arrays.md) 2 · [DP](../topics/dp.md) 2 · [Binary Search](../topics/binary-search.md) 2 · [Recursion/Backtracking](../topics/recursion-backtracking.md) 1 · [Sorting](../topics/sorting.md) 1 · [Greedy](../topics/greedy.md) 1 · [Trees](../topics/trees.md) 1 · +2 more  
**Seen at:** IIT BHU, IIT Bombay, IIT Guwahati, IIT Jodhpur, MNNIT Allahabad, Thapar Institute of Engineering and Technology, VNIT Nagpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-12 · IIT BHU · FTE · SDE](#2026-11-12--iit-bhu--fte--sde)
  - [Assign tree node values with adjacent difference exactly 1](#q1-assign-tree-node-values-with-adjacent-difference-exactly-1)
  - [Paint houses with 3 colors, mirrored houses differ](#q2-paint-houses-with-3-colors-mirrored-houses-differ)
- [2026-11-11 · VNIT Nagpur · FTE](#2026-11-11--vnit-nagpur--fte)
  - [BNY OA topics](#q1-bny-oa-topics)
- [2026-11-11 · IIT BHU · FTE · Quant Analytics / SDE](#2026-11-11--iit-bhu--fte--quant-analytics--sde)
  - [Maximize call volume with non-overlapping calls](#q1-maximize-call-volume-with-non-overlapping-calls)
  - [Minimum makespan to process requests across servers](#q2-minimum-makespan-to-process-requests-across-servers)
- [2026-11-10 · IIT BHU · FTE · Quant Analytics and Risk Compliance](#2026-11-10--iit-bhu--fte--quant-analytics-and-risk-compliance)
  - [BNY OA pattern](#q1-bny-oa-pattern)
- [2026-11-09 · Thapar Institute of Engineering and Technology · FTE · Quant Analytics (Risk and Compliance)](#2026-11-09--thapar-institute-of-engineering-and-technology--fte--quant-analytics-risk-and-compliance)
  - [BNY Quant Analytics OA pattern](#q1-bny-quant-analytics-oa-pattern)
- [2026-11-07 · MNNIT Allahabad · FTE](#2026-11-07--mnnit-allahabad--fte)
  - [BNY OA pattern](#q1-bny-oa-pattern-1)

</details>

---

## 2026-11-12 · IIT BHU · FTE · SDE

### Q1. Assign tree node values with adjacent difference exactly 1

You are given a tree with N nodes. Each node must be assigned a non-negative integer value. Some nodes already have fixed values, while the values of the remaining nodes are unknown. For every edge (u, v) in the tree, the absolute difference between the values at adjacent nodes must be exactly 1.

Assign values to all unassigned nodes such that:
- All pre-assigned values remain unchanged.
- For every edge (u, v), the absolute difference between their values is exactly 1.
- The sum of values of all nodes is minimized.

<sub>Topics: Trees, Graphs · Same idea: [LeetCode 785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) (Medium), parity coloring of adjacent nodes by traversal · Source: [chat, 12 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L348), [chat, 12 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L354), [chat, 12 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L356), [chat, 12 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L357), [chat, 12 Nov](../archive/inter-nit/2026-11.jsonl#L1390) · Also asked at: IIT Jodhpur (2026-11-12), IIT Guwahati (2026-11-12)</sub>

### Q2. Paint houses with 3 colors, mirrored houses differ

Given an integer n, the number of houses in a row, color the houses using three colors such that no two adjacent houses have the same color, and also the i-th and (n-1-i)-th houses must have different colors. Find the total number of ways.

Constraint: n <= 10^5

<sub>Topics: DP, Math · Same idea: [LeetCode 1411. Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/) (Hard), counting 3-color arrangements with adjacent-different DP · Source: [chat, 12 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L348), [chat, 12 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L354), [chat, 12 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L356), [chat, 12 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L357), [chat, 12 Nov](../archive/inter-nit/2026-11.jsonl#L1390) · Also asked at: IIT Jodhpur (2026-11-12), IIT Guwahati (2026-11-12)</sub>

## 2026-11-11 · VNIT Nagpur · FTE

### Q1. BNY OA topics

BNY mostly asks medium-level array and string questions, and focuses more on recursion and backtracking, as such questions might appear.

<sub>Topics: OA Format, Arrays, Recursion/Backtracking · Same idea: [LeetCode 46. Permutations](https://leetcode.com/problems/permutations/) (Medium), recursion and backtracking basics · Source: [chat, 11 Nov](../archive/inter-iit/2026-11.jsonl#L589)</sub>

## 2026-11-11 · IIT BHU · FTE · Quant Analytics / SDE

### Q1. Maximize call volume with non-overlapping calls

You are given three arrays:
- Start[i] = starting time of call i
- Duration[i] = duration of call i
- Volume[i] = profit/volume obtained by selecting call i

You can select multiple calls, but no two selected calls can overlap.

The objective is to maximize the total volume.

<sub>Topics: DP, Sorting, Binary Search · Similar: [LeetCode 1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) (Hard) · Source: [chat, 11 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L329)</sub>

### Q2. Minimum makespan to process requests across servers

1. There are N servers and M requests.
2. cache[i] tells us which server has the data for request i.
3. Processing request i:
   - On its cached server: 1 unit.
   - On any other server: 2 units.
4. Multiple servers can process requests simultaneously.
5. Each server can process only one request at a time.

Determine the minimum total time (makespan) to process all requests.

<sub>Topics: Greedy, Binary Search, Arrays · Same idea: [LeetCode 1723. Find Minimum Time to Finish All Jobs](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/) (Hard), minimize maximum load assigning tasks to workers · Source: [chat, 11 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L329)</sub>

## 2026-11-10 · IIT BHU · FTE · Quant Analytics and Risk Compliance

### Q1. BNY OA pattern

OA pattern: 2 DSA questions + 1 debugging question.

<sub>Topics: OA Format · Source: [chat, 10 Nov](../archive/inter-iit/2026-11.jsonl#L542) · Also asked at: MNNIT Allahabad (2026-11-11), IIT BHU ×4 (last 2026-11-12), IIT Bombay (2026-11-12), IIT Jodhpur (2026-11-12), IIT Guwahati (2026-11-12)</sub>

## 2026-11-09 · Thapar Institute of Engineering and Technology · FTE · Quant Analytics (Risk and Compliance)

### Q1. BNY Quant Analytics OA pattern

OA contained aptitude and ML MCQs (reported second-hand by a Thapar friend). No DSA questions mentioned.

<sub>Topics: OA Format · Source: [chat, 9 Nov](../archive/inter-nit/2026-11.jsonl#L988)</sub>

## 2026-11-07 · MNNIT Allahabad · FTE

### Q1. BNY OA pattern

The OA had 3 DSA questions, all of medium to hard difficulty. The actual questions were not shared.

<sub>Topics: OA Format · Source: [chat, 7 Nov](../archive/campus-mnnit-allahabad-placements/2026-11.jsonl#L105) · Also asked at: MNNIT Allahabad (2026-11-11)</sub>
