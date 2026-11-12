# Amazon

**21 questions** · 18 drives · latest 11 Nov 2026 · [1 practice problem](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 17 · [Arrays](../topics/arrays.md) 2 · [Hashing](../topics/hashing.md) 1 · [Trees](../topics/trees.md) 1 · [ML/AI](../topics/ml-ai.md) 1 · [Software Engineering](../topics/software-engineering.md) 1 · [Graphs](../topics/graphs.md) 1 · [Binary Search](../topics/binary-search.md) 1 · +3 more  
**Seen at:** BITS, BITS Pilani, IIT BHU, IIT Delhi, IIT Guwahati, IIT Hyderabad, IIT Kharagpur, IIT Kharagpur/Kanpur +7 more

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-11 · VNIT Nagpur · FTE](#2026-11-11--vnit-nagpur--fte)
  - [Amazon OA debugging questions overview](#q1-amazon-oa-debugging-questions-overview)
- [2026-11-11 · Unknown · FTE · SDE · Interview](#2026-11-11--unknown--fte--sde--interview)
  - [Selection process and final round focus](#q1-selection-process-and-final-round-focus)
- [2026-11-11 · IIT Kharagpur/Kanpur · FTE](#2026-11-11--iit-kharagpurkanpur--fte)
  - [Lexicographically maximum array after sorting K-sized subarrays](#q1-lexicographically-maximum-array-after-sorting-k-sized-subarrays)
- [2026-11-10 · IIT Roorkee · FTE](#2026-11-10--iit-roorkee--fte)
  - [Backend code debugging question (repo)](#q1-backend-code-debugging-question-repo)
- [2026-11-09 · MNNIT Allahabad · FTE](#2026-11-09--mnnit-allahabad--fte)
  - [Amazon AI-assisted coding round](#q1-amazon-ai-assisted-coding-round)
- [2026-11-09 · IIT Madras · FTE · SDE-1](#2026-11-09--iit-madras--fte--sde-1)
  - [Amazon SDE-1 OA format](#q1-amazon-sde-1-oa-format)
- [2026-11-08 · MNNIT Allahabad · FTE](#2026-11-08--mnnit-allahabad--fte)
  - [Amazon OA structure: DSA and AI-assisted coding](#q1-amazon-oa-structure-dsa-and-ai-assisted-coding)
- [2026-11-05 · Unknown · FTE](#2026-11-05--unknown--fte)
  - [Debugging: movie DB search backend](#q1-debugging-movie-db-search-backend)
- [2026-11-05 · NIT Raipur · FTE · SDE](#2026-11-05--nit-raipur--fte--sde)
  - [Amazon SDE OA pattern](#q1-amazon-sde-oa-pattern)
- [2026-11-05 · IIT Madras · FTE](#2026-11-05--iit-madras--fte)
  - [Amazon OA format](#q1-amazon-oa-format)
- [2026-11-05 · IIT Hyderabad · FTE](#2026-11-05--iit-hyderabad--fte)
  - [Amazon OA format](#q1-amazon-oa-format-1)
- [2026-11-05 · IIT Guwahati · FTE](#2026-11-05--iit-guwahati--fte)
  - [Amazon OA format](#q1-amazon-oa-format-2)
- [2026-11-05 · IIT Delhi · FTE](#2026-11-05--iit-delhi--fte)
  - [Amazon OA format: AI-assisted backend debugging](#q1-amazon-oa-format-ai-assisted-backend-debugging)
  - [Amazon OA format: coding and debugging](#q2-amazon-oa-format-coding-and-debugging)
  - [Minimize max inconvenience after opening one store](#q3-minimize-max-inconvenience-after-opening-one-store)
- [2026-11-04 · IIT Madras · FTE](#2026-11-04--iit-madras--fte)
  - [Amazon OA overview: DSA and debugging sections](#q1-amazon-oa-overview-dsa-and-debugging-sections)
- [2026-11-01 · MNNIT Allahabad · FTE](#2026-11-01--mnnit-allahabad--fte)
  - [Amazon OA pattern](#q1-amazon-oa-pattern)
- [2026-10-30 · IIT Guwahati · FTE](#2026-10-30--iit-guwahati--fte)
  - [Amazon on-campus OA format](#q1-amazon-on-campus-oa-format)
- [2026-10-29 · BITS · FTE · SDE](#2026-10-29--bits--fte--sde)
  - [Amazon SDE OA pattern change](#q1-amazon-sde-oa-pattern-change)
- [2026-10-03 · IIT BHU · FTE · Applied Scientist · Interview](#2026-10-03--iit-bhu--fte--applied-scientist--interview)
  - [Internal implementation of map, set, unordered_map, unordered_set](#q1-internal-implementation-of-map-set-unordered_map-unordered_set)
  - [ML round: PCA, decision trees, SGD, K-means](#q2-ml-round-pca-decision-trees-sgd-k-means)

</details>

---

## 2026-11-11 · VNIT Nagpur · FTE

### Q1. Amazon OA debugging questions overview

The debugging questions were mostly about identifying logical errors and fixing implementation issues in the given code: incorrect loop conditions, boundary cases, wrong variable initialization, improper handling of edge cases, incorrect if-else conditions, off-by-one errors and array indexing issues. In a few cases the overall approach was correct but small implementation mistakes caused incorrect outputs. Suggested revision: arrays, strings, loops, sorting, searching and edge-case handling.

<sub>Topics: OA Format · Source: [chat, 11 Nov](../archive/amazon-oa/2026-11.jsonl#L130)</sub>

## 2026-11-11 · Unknown · FTE · SDE · Interview

### Q1. Selection process and final round focus

In their college, 100 students were shortlisted for the OA and 6 were taken to the final round. The final round focused more on AI systems and RAGs. Actual questions were not shared.

<sub>Topics: OA Format · Source: [chat, 11 Nov](../archive/inter-nit/2026-11.jsonl#L1194)</sub>

## 2026-11-11 · IIT Kharagpur/Kanpur · FTE

### Q1. Lexicographically maximum array after sorting K-sized subarrays

You are given an integer array arr of size N and an integer K.

You can perform the following operation any number of times:
1. Choose an index i such that 0 ≤ i ≤ N-K.
2. Select K consecutive elements starting from index i, i.e. arr[i...i+K-1].
3. Sort these K elements in increasing (ascending) order.
4. Replace the selected subarray with its sorted version.

Each operation may produce a different arrangement of the array. Return the lexicographically maximum array obtainable by performing zero or more such operations.

Example 1:
```
Input:
N = 5
K = 3
arr = [3, 5, 1, 4, 2]

Output: [3, 5, 1, 4, 2]
```
Possible operations: sort indices 0 to 2 gives [1, 3, 5, 4, 2]; sort indices 1 to 3 gives [3, 1, 4, 5, 2]; sort indices 2 to 4 gives [3, 5, 1, 2, 4].

Explanation: Since zero operations are allowed, the original array is already the lexicographically maximum possible arrangement. Sorting any subarray in ascending order cannot make the array lexicographically larger.

<sub>Topics: Arrays, Sorting, Greedy · Source: [chat, 11 Nov](../archive/amazon-oa/2026-11.jsonl#L140) · Also asked at: IIT Kharagpur ×2 (last 2026-11-11), IIT Kharagpur/Kanpur (2026-11-11)</sub>

## 2026-11-10 · IIT Roorkee · FTE

### Q1. Backend code debugging question (repo)

The OA has a repo/backend code debugging question. Most probably it involves fixing bugs in an already implemented solution rather than implementing a feature, and the backend is usually Express.js.

The actual bugs or problem statement were not shared.

<sub>Topics: OA Format, Web Dev · Source: [chat, 10 Nov](../archive/amazon-oa/2026-11.jsonl#L124), [chat, 10 Nov](../archive/amazon-oa/2026-11.jsonl#L125)</sub>

## 2026-11-09 · MNNIT Allahabad · FTE

### Q1. Amazon AI-assisted coding round

The AI-assisted coding round was medium to hard in difficulty. It involved backend debugging only (no frontend). Advice given: solve the DSA part and attempt the AI-assisted coding part partially.

<sub>Topics: OA Format · Source: [chat, 9 Nov](../archive/amazon-oa/2026-11.jsonl#L96), [chat, 9 Nov](../archive/amazon-oa/2026-11.jsonl#L100)</sub>

## 2026-11-09 · IIT Madras · FTE · SDE-1

### Q1. Amazon SDE-1 OA format

The DSA level is 1500-1600 rated Codeforces problems, plus a debugging question, for 60 minutes.

<sub>Topics: OA Format · Source: [chat, 9 Nov](../archive/amazon-oa/2026-11.jsonl#L89)</sub>

## 2026-11-08 · MNNIT Allahabad · FTE

### Q1. Amazon OA structure: DSA and AI-assisted coding

The DSA part was 40 minutes. After fully submitting it you can move to the next part, AI-assisted coding, which was 60 minutes. For the Node.js question, Express was used (not plain vanilla Node).

<sub>Topics: OA Format · Source: [chat, 8 Nov](../archive/amazon-oa/2026-11.jsonl#L83), [chat, 8 Nov](../archive/amazon-oa/2026-11.jsonl#L84)</sub>

## 2026-11-05 · Unknown · FTE

### Q1. Debugging: movie DB search backend

Backend debugging question about a movie database. Movies are stored in a database; the errors occur in fetching movies by title, name, rating etc. Almost all errors are in the fetching/search logic. From the frontend you go to the `MovieController`, where the search business logic is present, and you need to fix it. Only one file needs changes, correcting some basic implementations. The question lists what to correct; you identify those in the codebase and make the tests pass.

Exact statement not given.

<sub>Topics: Software Engineering, OA Format · Source: [chat, 5 Nov](../archive/amazon-oa/2026-11.jsonl#L50), [chat, 5 Nov](../archive/amazon-oa/2026-11.jsonl#L51), [chat, 5 Nov](../archive/amazon-oa/2026-11.jsonl#L52)</sub>

## 2026-11-05 · NIT Raipur · FTE · SDE

### Q1. Amazon SDE OA pattern

The OA had 1 DSA question and 1 back-end web development question. (Details not given.)

<sub>Topics: OA Format · Source: [chat, 5 Nov](../archive/inter-nit/2026-11.jsonl#L465)</sub>

## 2026-11-05 · IIT Madras · FTE

### Q1. Amazon OA format

One medium DSA question plus 1 debugging question with an AI assistant.

<sub>Topics: OA Format · Source: [chat, 5 Nov](../archive/campus-iit-madras-placements/2026-11.jsonl#L80)</sub>

## 2026-11-05 · IIT Hyderabad · FTE

### Q1. Amazon OA format

One medium-level DSA question and one Node.js debugging task along with an AI assistant, followed by behavioural questions.

<sub>Topics: OA Format · Source: [chat, 5 Nov](../archive/campus-nit-kurukshetra-placements/2026-11.jsonl#L23), [chat, 5 Nov](../archive/campus-nit-kurukshetra-placements/2026-11.jsonl#L24) · Also asked at: IIT Hyderabad ×2 (last 2026-11-06)</sub>

## 2026-11-05 · IIT Guwahati · FTE

### Q1. Amazon OA format

One DSA question and one code repo debugging task.

<sub>Topics: OA Format · Source: [chat, 5 Nov](../archive/campus-mnnit-allahabad-placements/2026-11.jsonl#L66)</sub>

## 2026-11-05 · IIT Delhi · FTE

### Q1. Amazon OA format: AI-assisted backend debugging

The OA was on HackerRank (as the poster believed). It included an AI-assisted debugging backend question: candidates were given a VS Code-like platform with various files and folders and a chatbot. They had to find the issues in the codebase and change the code. The problem statement was provided along with input files. The language or framework (e.g. C++, Node) had to be chosen before starting the test.

The details of the specific bugs and the DSA questions were not shared.

<sub>Topics: OA Format · Source: [chat, 5 Nov](../archive/amazon-oa/2026-11.jsonl#L37), [chat, 5 Nov](../archive/amazon-oa/2026-11.jsonl#L38), [chat, 5 Nov](../archive/amazon-oa/2026-11.jsonl#L39), [chat, 5 Nov](../archive/amazon-oa/2026-11.jsonl#L44) · Also asked at: BITS Pilani (2026-11-08), IIT Delhi (2026-11-09)</sub>

### Q2. Amazon OA format: coding and debugging

The OA had 1 coding question and 1 debugging question, in a proper setup with all the files and an inbuilt chatbot. The debugging question could be done in C++. The actual question statements were not shared.

<sub>Topics: OA Format · Source: [chat, 5 Nov](../archive/campus-iit-delhi-placements/2026-11.jsonl#L151), [chat, 5 Nov](../archive/campus-iit-delhi-placements/2026-11.jsonl#L163), [chat, 5 Nov](../archive/campus-iit-delhi-placements/2026-11.jsonl#L164)</sub>

### Q3. Minimize max inconvenience after opening one store

You are given an N × M binary matrix representing a city grid.
- Each cell represents a city.
- 1 represents a city that already has a store.
- 0 represents a city that does not have a store.

The inconvenience of a city is defined as its minimum distance from any existing store, where the distance between two cells (r1, c1) and (r2, c2) is:

d = max(|r1-r2|, |c1-c2|)

In other words, the distance is the maximum of the absolute differences in their row and column coordinates.

Now, Amazon wants to open exactly one additional store. You can choose any cell containing 0 and convert it into 1.

Determine the minimum possible value of the maximum inconvenience among all cities after opening this additional store.

Constraints:
- N, M <= 500
- Matrix contains only 0 and 1

<sub>Topics: Graphs, Binary Search, Arrays · Same idea: [LeetCode 1162. As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) (Medium), multi-source BFS grid distance maximizing minimum distance · Source: [chat, 5 Nov](../archive/campus-iit-delhi-placements/2026-11.jsonl#L173)</sub>

## 2026-11-04 · IIT Madras · FTE

### Q1. Amazon OA overview: DSA and debugging sections

1. DSA questions were random; some were weird DP problems, but many were standard problems, e.g. longest subarray of 1s with at most k swaps of 0s.
2. Debugging section (AI-assisted): choose a stack you are at least familiar with. The AI will not generate code unless you figure out the problematic part. The problem description gives enough information, so read it properly.

<sub>Topics: OA Format · Source: [chat, 4 Nov](../archive/amazon-oa/2026-11.jsonl#L32) · Also asked at: Thapar Institute (2026-11-04), NIT Surathkal (2026-11-04), IIT Hyderabad (2026-11-04), IIT Delhi (2026-11-07)</sub>

## 2026-11-01 · MNNIT Allahabad · FTE

### Q1. Amazon OA pattern

Same as the off-campus application:

- 1 DSA question
- 1 debugging question (backend)
- then a psychometric test including mail replies and your behaviour

<sub>Topics: OA Format · Source: [chat, 1 Nov](../archive/amazon-oa/2026-11.jsonl#L5), [chat, 1 Nov](../archive/amazon-oa/2026-11.jsonl#L6) · Also asked at: IIT Roorkee ×4 (last 2026-11-10), IIT Delhi (2026-11-10)</sub>

## 2026-10-30 · IIT Guwahati · FTE

### Q1. Amazon on-campus OA format

3 medium DSA questions and behavioural MCQs. Specific questions were not given.

<sub>Topics: OA Format · Source: [chat, 30 Oct](../archive/inter-nit/2026-10.jsonl#L2943)</sub>

## 2026-10-29 · BITS · FTE · SDE

### Q1. Amazon SDE OA pattern change

The only change in the Amazon OA pattern is one "Find the bug" question, where you are given a codebase with a basic AI assistant.

<sub>Topics: OA Format · Source: [chat, 29 Oct](../archive/amazon-oa/2026-10.jsonl#L27) · Also asked at: MNNIT Allahabad (2026-11-01), NIT Surathkal (2026-11-03)</sub>

## 2026-10-03 · IIT BHU · FTE · Applied Scientist · Interview

### Q1. Internal implementation of map, set, unordered_map, unordered_set

In the DSA round, along with two DSA questions, the interviewer asked about the internal implementation of map, set, unordered_map and unordered_set.

The two DSA questions themselves were not shared.

<sub>Topics: Hashing, Trees · Source: [chat, 3 Oct](../archive/amazon-oa/2026-10.jsonl#L3), [chat, 14 Oct](../archive/amazon-oa/2026-10.jsonl#L8)</sub>

### Q2. ML round: PCA, decision trees, SGD, K-means

The second round had only ML questions. Topics asked: what is PCA, decision trees, SGD (stochastic gradient descent), and K-means clustering. If a Neural Networks project was on the resume, the discussion on it was much longer.

<sub>Topics: ML/AI · Source: [chat, 3 Oct](../archive/amazon-oa/2026-10.jsonl#L3), [chat, 14 Oct](../archive/amazon-oa/2026-10.jsonl#L8)</sub>
