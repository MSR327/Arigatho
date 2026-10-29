# Mastercard

**6 questions** · 4 drives · latest 29 Oct 2026 · [1 LeetCode match](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 4 · [DP](../topics/dp.md) 1 · [Strings](../topics/strings.md) 1 · [Arrays](../topics/arrays.md) 1 · [Sorting](../topics/sorting.md) 1  
**Seen at:** IIIT Sri City, IIT Guwahati, IIT Kharagpur, IIT Kharagpur/Kanpur

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-29 · IIT Guwahati · FTE · Product Specialist](#2026-10-29--iit-guwahati--fte--product-specialist)
  - [Mastercard Product Specialist OA pattern](#q1-mastercard-product-specialist-oa-pattern)
- [2026-10-28 · IIT Guwahati · FTE · Data Science](#2026-10-28--iit-guwahati--fte--data-science)
  - [Mastercard Data Science OA topics](#q1-mastercard-data-science-oa-topics)
  - [Mastercard DS OA contents](#q2-mastercard-ds-oa-contents)
- [2026-10-25 · IIIT Sri City · FTE · Associate Consultant / APS · Other round](#2026-10-25--iiit-sri-city--fte--associate-consultant--aps--other-round)
  - [Mastercard selection process topics](#q1-mastercard-selection-process-topics)
- [2026-10-24 · IIT Kharagpur/Kanpur · FTE](#2026-10-24--iit-kharagpurkanpur--fte)
  - [Edit the Filename](#q1-edit-the-filename)
  - [Mario and the Number Mountain](#q2-mario-and-the-number-mountain)

</details>

---

## 2026-10-29 · IIT Guwahati · FTE · Product Specialist

### Q1. Mastercard Product Specialist OA pattern

- SQL: 10 questions (9 MCQ, 1 coding), 10 mins
- Python: 5 questions (1 DSA, 4 MCQ), 20 mins
- Math: 20 questions, 20 mins

<sub>Topics: OA Format · Source: [chat, 29 Oct](../archive/campus-iit-guwahati-placements/2026-10.jsonl#L466)</sub>

## 2026-10-28 · IIT Guwahati · FTE · Data Science

### Q1. Mastercard Data Science OA topics

Topics asked: Python, SQL, stats.

<sub>Topics: OA Format · Source: [chat, 27 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L21), [chat, 28 Oct](../archive/campus-iit-kharagpur-placements/2026-10.jsonl#L49)</sub>

### Q2. Mastercard DS OA contents

One easy Python DSA question and MCQs.

<sub>Topics: OA Format · Source: [chat, 28 Oct](../archive/inter-nit/2026-10.jsonl#L2694)</sub>

## 2026-10-25 · IIIT Sri City · FTE · Associate Consultant / APS · Other round

### Q1. Mastercard selection process topics

Topics asked: DSA, Core CS (DBMS, OS, CN, OOP), System Design, Projects & Resume, Coding/OA, and HR/Behavioral questions.

No individual questions were given.

<sub>Topics: OA Format · Source: [chat, 25 Oct](../archive/campus-iiit-allahabad-placements/2026-10.jsonl#L23)</sub>

## 2026-10-24 · IIT Kharagpur/Kanpur · FTE

### Q1. Edit the Filename

A student has built an application that receives a filename and a dictionary string. Find the minimum number of single-character operations needed to transform the filename into the dictionary string. If both are already equal, output 0. Each operation has unit cost and can be applied at any position: Insert (add one character to the filename), Remove (delete one character from the filename), Replace (change one character in the filename to another character).  
Input: line 1 contains the filename; line 2 contains the dictionary string. Output: one integer, the minimum number of operations.  
Constraints: both strings contain only letters and digits; each length is greater than 1 and at most 25.  
Sample: Input "Hello" / "There" -> Output 5. (The statement says the strings are case-insensitive, but the expected output 5 comes from a case-sensitive comparison.)

<sub>Topics: DP, Strings · Similar: [LeetCode 72. Edit Distance](https://leetcode.com/problems/edit-distance/) (Medium) · Source: [Mastercard_OA_iitkgp.pdf](../archive/files/12277-Mastercard_OA_iitkgp.pdf) · Also asked at: IIT Kharagpur ×2 (last 2026-10-25)</sub>

### Q2. Mario and the Number Mountain

Mario stands at the top-left of an n x n grid of integers. A special loophole is at the middle cell of the grid. To reach Princess Peach, Mario must use the values around that cell to build a mountain of numbers. Print the mountain using these rules:  
- The loophole value is the center cell, arr[n/2][n/2] (zero-based).  
- If n &lt;= 9, take the 8 surrounding cells (the 3x3 region minus the center). If n > 9, take the 24 surrounding cells (the 5x5 region minus the center).  
- Add the center value to each selected neighbouring cell, and include 0 for the center itself. This gives 9 or 25 values.  
- Sort these values from largest to smallest. The middle element of the sorted list is the tip of the mountain.  
- For each later level, take the values immediately to the left and right of the middle sorted position as the edges of the row. Fill the gaps alternately with the difference (left - right) and the sum (left + right) of those edges, starting with the difference.  
Input: the first line has the odd integer n, followed by n rows of n space-separated integers. Output: the mountain, one level per line, with space-separated values.  
Constraints: n is odd and n > 2.  
Sample input:  
5  
1 2 1 9 6  
3 3 9 8 5  
4 1 2 3 2  
1 1 2 6 7  
7 8 9 0 3  
Expected output:  
5  
5 4  
8 5 3  
10 7 13 3  
11 11 11 11 0  
(The center is 2. Its neighbours 3,9,8,1,3,1,2,6 plus 2 each, and 0 for the center, give 5,11,10,3,5,3,4,8,0. Sorted descending: [11,10,8,5,5,4,3,3,0].)

<sub>Topics: Arrays, Sorting · Source: [Mastercard_OA_iitkgp.pdf](../archive/files/12277-Mastercard_OA_iitkgp.pdf) · Also asked at: IIT Kharagpur ×2 (last 2026-10-25)</sub>
