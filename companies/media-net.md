# Media.net

**18 questions** · 9 drives · latest 19 Oct 2026 · [8 LeetCode matches](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [DP](../topics/dp.md) 7 · [Arrays](../topics/arrays.md) 7 · [Trees](../topics/trees.md) 4 · [Greedy](../topics/greedy.md) 4 · [Strings](../topics/strings.md) 3 · [OA Format](../topics/oa-format.md) 3 · [OS/DBMS/CN MCQ](../topics/os-dbms-cn-mcq.md) 2 · [Two Pointers](../topics/two-pointers.md) 2 · +4 more  
**Seen at:** Delhi Technological University, IIT Bhubaneswar, IIT Bombay, IIT Delhi, Netaji Subhas University of Technology, VNIT Nagpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-19 · VNIT Nagpur · FTE · SDE · Interview](#2026-10-19--vnit-nagpur--fte--sde--interview)
  - [Media.net SDE interview overview](#q1-medianet-sde-interview-overview)
- [2026-10-19 · Unknown · Intern · SDE](#2026-10-19--unknown--intern--sde)
  - [Magic Number Array](#q1-magic-number-array)
  - [Allied Nations' Tour](#q2-allied-nations-tour)
  - [Matrix 2x2 XOR Conversion](#q3-matrix-2x2-xor-conversion)
- [2026-10-19 · Netaji Subhas University of Technology · FTE](#2026-10-19--netaji-subhas-university-of-technology--fte)
  - [Trapping Rain Water](#q1-trapping-rain-water)
- [2026-10-17 · Delhi Technological University · FTE](#2026-10-17--delhi-technological-university--fte)
  - [Trapping Rain Water II](#q1-trapping-rain-water-ii)
- [2026-10-16 · Delhi Technological University · Intern](#2026-10-16--delhi-technological-university--intern)
  - [Trapping rain water and an easy array question](#q1-trapping-rain-water-and-an-easy-array-question)
- [2026-10-15 · IIT Delhi · FTE](#2026-10-15--iit-delhi--fte)
  - [Minimum Concatenations to Form a Target String](#q1-minimum-concatenations-to-form-a-target-string)
  - [Recover Two Swapped Elements in a BST](#q2-recover-two-swapped-elements-in-a-bst)
  - [Minimum Cost to Merge an Array into One Element](#q3-minimum-cost-to-merge-an-array-into-one-element)
- [2026-10-15 · IIT Bombay · Intern](#2026-10-15--iit-bombay--intern)
  - [Build string from prefixes with minimum concatenations](#q1-build-string-from-prefixes-with-minimum-concatenations)
  - [Recover BST with two swapped nodes in O(1) space](#q2-recover-bst-with-two-swapped-nodes-in-o1-space)
  - [Merge adjacent elements with minimum total cost](#q3-merge-adjacent-elements-with-minimum-total-cost)
  - [MCQs on CN, DBMS, OS and Linux](#q4-mcqs-on-cn-dbms-os-and-linux)
- [2026-10-13 · Unknown · FTE · SRE · Interview](#2026-10-13--unknown--fte--sre--interview)
  - [Media.net SRE hiring process description](#q1-medianet-sre-hiring-process-description)
- [2026-10-13 · IIT Bhubaneswar · FTE · SDE](#2026-10-13--iit-bhubaneswar--fte--sde)
  - [Minimum concatenations to form a string from prefixes](#q1-minimum-concatenations-to-form-a-string-from-prefixes)
  - [Recover BST with two swapped nodes](#q2-recover-bst-with-two-swapped-nodes)
  - [Minimum cost to merge array into one element](#q3-minimum-cost-to-merge-array-into-one-element)

</details>

---

## 2026-10-19 · VNIT Nagpur · FTE · SDE · Interview

### Q1. Media.net SDE interview overview

Mainly DSA questions are asked, some questions on core subjects, and the interviewers go deep into your projects. (No specific questions given.)

<sub>Topics: OA Format · Source: [chat, 19 Oct](../archive/intern-2027/2026-10.jsonl#L68)</sub>

## 2026-10-19 · Unknown · Intern · SDE

### Q1. Magic Number Array

Given a permutation of size N in integer array A. For each number, find if the value of its magic number is >= 0 or negative. The value of a magic number is defined as: (count of smaller numbers to the left × count of smaller numbers to the right) − (count of larger numbers to the left × count of larger numbers to the right).

Return an integer array where `ans[i]` is 1 if the magic number is >= 0 or -1 if it is negative.

Constraints:

```
1 <= N <= 10^5
```

<sub>Topics: Arrays, Trees · Source: [chat, 19 Oct](../archive/intern-2027/2026-10.jsonl#L64), [Media.net_OA.pdf](../archive/files/9140-Media.net_OA.pdf)</sub>

### Q2. Allied Nations' Tour

The allied nations in total have A cities numbered from 1 to A. Currently you are at city B. Your task is to take a tour of the given A cities for C days. From a city i you can go to any city in the range i − E to i + E and you cannot go out of range.

The intel core has provided M information given in the form of a 2D array D of size M. According to this, at day `D[i][0]` Akatsuki will attack on city `D[i][1]`. You cannot be present in some city on a certain day if Akatsuki will arrive there.

Find the total number of tours you will be able to take. Since the answer can be big, output it modulo 1000000007.

Constraints:

```
1 <= A, C <= 1000
1 <= M <= A x C
```

<sub>Topics: DP, Arrays · Source: [chat, 19 Oct](../archive/intern-2027/2026-10.jsonl#L64), [Media.net_OA.pdf](../archive/files/9140-Media.net_OA.pdf)</sub>

### Q3. Matrix 2x2 XOR Conversion

Given 2 matrices A and B of size N x N, all the elements are either 0 or 1. We perform an operation on matrix A any number of times: choose any 2 x 2 submatrix of A and make each element `A[i][j] = A[i][j] XOR 1` for each (i, j) in this submatrix.

Check if it is possible to convert A into B. Return 1 if possible and 0 if not.

Constraints:

```
2 <= |A| = |B| <= 10^3
```

<sub>Topics: Arrays, Greedy, Bit Manipulation · Source: [chat, 19 Oct](../archive/intern-2027/2026-10.jsonl#L64), [Media.net_OA.pdf](../archive/files/9140-Media.net_OA.pdf)</sub>

## 2026-10-19 · Netaji Subhas University of Technology · FTE

### Q1. Trapping Rain Water

Trapping Rain Water (LeetCode 42): given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining. (The poster named only the problem, in reply to 'what was asked in media.net'.)

<sub>Topics: Two Pointers, Arrays, Stack/Queue · Similar: [LeetCode 42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) · Source: [chat, 19 Oct](../archive/inter-nit/2026-10.jsonl#L1594)</sub>

## 2026-10-17 · Delhi Technological University · FTE

### Q1. Trapping Rain Water II

Trapping Rain Water II: given an m x n integer matrix heightMap giving the height of each cell in a 2D elevation map, return the volume of water it can trap after raining. (The poster named only the problem as one of the questions in the Media.net OA held recently at DTU. No other details were given.)

<sub>Topics: Heaps, Graphs, Arrays · Similar: [LeetCode 407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) (Hard) · Source: [chat, 17 Oct](../archive/inter-nit/2026-10.jsonl#L1469) · Also asked at: Netaji Subhas University of Technology (2026-10-19)</sub>

## 2026-10-16 · Delhi Technological University · Intern

### Q1. Trapping rain water and an easy array question

Trapping rainwater and one easy array question (details of the second not given; unclear whether 1D or 2D trapping rain water).

<sub>Topics: Arrays, Two Pointers · Similar: [LeetCode 42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) · Source: [chat, 16 Oct](../archive/intern-2027/2026-10.jsonl#L138)</sub>

## 2026-10-15 · IIT Delhi · FTE

### Q1. Minimum Concatenations to Form a Target String

You are given an array of strings A and a target string s. You can use prefixes of strings in the array to construct the target string. Find the minimum number of strings/prefixes used to form the target.

Example:
```
A = ["abc", "cat"]
s = "ac"
Output: 2
```
Use "a" from "abc" and "c" from "cat".

<sub>Topics: Strings, DP, Greedy · Source: [chat, 15 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L192)</sub>

### Q2. Recover Two Swapped Elements in a BST

You are given a BST in which two elements have been swapped accidentally. Identify the two incorrect elements in the required order. Suggested approach: Morris Traversal for inorder traversal with O(1) auxiliary space.

<sub>Topics: Trees · Similar: [LeetCode 99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) (Medium) · Source: [chat, 15 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L192)</sub>

### Q3. Minimum Cost to Merge an Array into One Element

Given an array of integers. In one operation, combine two adjacent elements a and c into a single element a+c, at cost a+c. Find the minimum total cost to convert the entire array into a single element.

<sub>Topics: DP, Greedy · Source: [chat, 15 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L192)</sub>

## 2026-10-15 · IIT Bombay · Intern

### Q1. Build string from prefixes with minimum concatenations

Given an array of strings A and a string s, build s by concatenating prefixes of strings in A, using as few pieces as possible. Return the minimum number of concatenations (strings used). Example: A = [abc, cat], s = ac -> use 'a' from A[0] and 'c' from A[1], so the answer is 2.

<sub>Topics: DP, Strings · Similar: [LeetCode 3291. Minimum Number of Valid Strings to Form Target I](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/) (Medium) · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L85)</sub>

### Q2. Recover BST with two swapped nodes in O(1) space

A BST has two of its elements swapped. Find those two elements using O(1) extra space (threaded binary tree / Morris traversal approach).

<sub>Topics: Trees · Similar: [LeetCode 99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) (Medium) · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L85)</sub>

### Q3. Merge adjacent elements with minimum total cost

Given an array of integers, reduce it to a single element. In one operation, replace two adjacent elements (a, c) with their sum a+c, which costs a+c. Minimise the total cost of reducing the array to one element.

<sub>Topics: DP, Arrays · Similar: [LeetCode 1000. Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) (Hard) · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L85)</sub>

### Q4. MCQs on CN, DBMS, OS and Linux

MCQ/OA round with questions on Computer Networks, DBMS, Operating Systems and Linux troubleshooting.

<sub>Topics: OS/DBMS/CN MCQ, OA Format · Source: [chat, 15 Oct](../archive/inter-nit/2026-10.jsonl#L85)</sub>

## 2026-10-13 · Unknown · FTE · SRE · Interview

### Q1. Media.net SRE hiring process description

Process for SRE role:
- MCQ/OA round: MCQs on Computer Networks, DBMS, Operating Systems and Linux troubleshooting.
- Machine coding round: 2-3.5 hours, focused on socket programming.
- R1 Technical interview: CS fundamentals, especially CN, OS and basic Linux. No DSA reported. Projects not discussed in depth, but SRE/DevOps projects may attract questions.
- R2 System design: scenario-based, with requirements revealed progressively. The most important round.
- R3 Director of Engineering: formal, managerial discussion.
- HR round after the director round.

Prep: socket programming, CN, OS, Linux troubleshooting (practice on SadServers; the campus process also uses a custom platform), system design.

<sub>Topics: OA Format, OS/DBMS/CN MCQ · Source: [chat, 13 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L167)</sub>

## 2026-10-13 · IIT Bhubaneswar · FTE · SDE

### Q1. Minimum concatenations to form a string from prefixes

Given an array of strings and a target string s, form s using the minimum number of concatenations of strings from the array. A prefix of a string in the array may be used.

Example: A = [abc, cat], s = "ac": use 'a' from A[0] and 'c' from A[1]. Find the minimum number of concatenations (strings used from the array).

<sub>Topics: Strings, DP · Source: [chat, 13 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L166)</sub>

### Q2. Recover BST with two swapped nodes

Given a BST in which two elements have been swapped, find those two elements. The solution used a threaded binary tree approach (Morris traversal), i.e. O(1) space. The poster's exact output format ("in order of 1") was unclear.

<sub>Topics: Trees · Similar: [LeetCode 99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) (Medium) · Source: [chat, 13 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L166)</sub>

### Q3. Minimum cost to merge array into one element

Given an array of integers, convert it to a single element. You can merge two adjacent elements (a, c) into one element (a+c) at a cost of a+c. Minimise the total cost to reduce the array to a single element.

<sub>Topics: DP, Greedy · Source: [chat, 13 Oct](../archive/campus-iit-delhi-placements/2026-10.jsonl#L166)</sub>
