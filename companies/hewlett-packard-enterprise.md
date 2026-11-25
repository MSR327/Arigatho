# Hewlett Packard Enterprise

**3 questions** · 3 drives · latest 24 Nov 2026 · [← all companies](../README.md#companies)

**Asks about:** [ML/AI](../topics/ml-ai.md) 2 · [OA Format](../topics/oa-format.md) 2 · [Arrays](../topics/arrays.md) 1 · [Hashing](../topics/hashing.md) 1  
**Seen at:** IIT BHU, IIT Guwahati

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-24 · Unknown · FTE · Data Science](#2026-11-24--unknown--fte--data-science)
  - [HPE OA pattern](#q1-hpe-oa-pattern)
- [2026-11-24 · IIT Guwahati · FTE · AI Engineer · Other round](#2026-11-24--iit-guwahati--fte--ai-engineer--other-round)
  - [HPE round 2: LangChain question](#q1-hpe-round-2-langchain-question)
- [2026-11-24 · IIT BHU · FTE · AI Engineer](#2026-11-24--iit-bhu--fte--ai-engineer)
  - [Lexicographically smallest four indices with equal pair sums](#q1-lexicographically-smallest-four-indices-with-equal-pair-sums)

</details>

---

## 2026-11-24 · Unknown · FTE · Data Science

### Q1. HPE OA pattern

HPE had LeetCode medium questions, along with MCQs based on agentic AI and RAG. It was a HackerRank desktop-based test conducted in the college itself.

Total CTC offered was 21 with a base of 16; around 15 people were taken from the poster's college.

<sub>Topics: OA Format, ML/AI · Source: [chat, 24 Nov](../archive/campus-iit-delhi-placements/2026-11.jsonl#L744)</sub>

## 2026-11-24 · IIT Guwahati · FTE · AI Engineer · Other round

### Q1. HPE round 2: LangChain question

Round 2 asked a LangChain question; duration 2 hrs.

The actual question statement is not given.

<sub>Topics: ML/AI, OA Format · Source: [chat, 24 Nov](../archive/inter-iit/2026-11.jsonl#L1279)</sub>

## 2026-11-24 · IIT BHU · FTE · AI Engineer

### Q1. Lexicographically smallest four indices with equal pair sums

Given an array `arr[]` of positive integers, find four indices a, b, c, and d such that `arr[a] + arr[b] = arr[c] + arr[d]`, where a, b, c, d are all distinct indices.

If multiple such quadruplets exist, return the one that is lexicographically smallest when the indices are considered in the order a, b, c, d.
If no such quadruplet exists, return `{-1, -1, -1, -1}`.
Ensure a < b and c < d, and the pair (a, b) is lexicographically smaller than the pair (c, d).

Examples:

```
Input: arr[] = [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5]
Explanation: arr[0] + arr[2] = 3 + 7 = 10, arr[3] + arr[5] = 1 + 9 = 10.
This is the lexicographically smallest such quadruplet of indices.
```

```
Input: arr[] = [1, 2, 3, 3]
Output: [-1, -1, -1, -1]
Explanation: No two distinct pairs of indices produce the same sum.
```

Constraints:

- 4 ≤ arr.size() ≤ 10^3
- 1 ≤ arr[i] ≤ 10^7

```cpp
class Solution {
  public:
    vector<int> findPairs(vector<int>& arr) {
        
        
    }
};
```

<sub>Topics: Arrays, Hashing · Source: [chat, 24 Nov](../archive/campus-iit-bhu-placements/2026-11.jsonl#L694)</sub>
