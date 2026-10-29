# Nvidia

**28 questions** from 13 OA drives · seen at IIT BHU, IIT Dhanbad, MNNIT Allahabad, NIT Delhi, NIT Meghalaya, NIT Rourkela, Unknown, VNIT Nagpur · latest 2026-10-29

**Topics:** [Digital Electronics](../topics/digital-electronics.md) (9) · [OA Format](../topics/oa-format.md) (7) · [Math](../topics/math.md) (5) · [Stack/Queue](../topics/stack-queue.md) (4) · [Trees](../topics/trees.md) (4) · [Graphs](../topics/graphs.md) (3) · [Circuits](../topics/circuits.md) (3) · [OS/DBMS/CN MCQ](../topics/os-dbms-cn-mcq.md) (2) · [Recursion/Backtracking](../topics/recursion-backtracking.md) (2) · [Bit Manipulation](../topics/bit-manipulation.md) (2) · [DP](../topics/dp.md) (2) · [Hashing](../topics/hashing.md) (1) · [Strings](../topics/strings.md) (1) · [Arrays](../topics/arrays.md) (1) · [Aptitude](../topics/aptitude.md) (1) · [Analog Electronics](../topics/analog-electronics.md) (1) · [HR & Behavioral](../topics/hr-behavioral.md) (1)

**LeetCode matches:** 2 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-29 · NIT Delhi · Intern · HW Intern](#2026-10-29--nit-delhi--intern--hw-intern) · 5 questions
- [2026-10-28 · NIT Rourkela · FTE · System Software Engineer](#2026-10-28--nit-rourkela--fte--system-software-engineer) · 1 question
- [2026-10-28 · NIT Meghalaya · Intern · Hardware (GPU)](#2026-10-28--nit-meghalaya--intern--hardware-gpu) · 5 questions
- [2026-10-28 · MNNIT Allahabad · FTE · System Software Engineer](#2026-10-28--mnnit-allahabad--fte--system-software-engineer) · 1 question
- [2026-10-26 · MNNIT Allahabad · FTE](#2026-10-26--mnnit-allahabad--fte) · 4 questions
- [2026-10-26 · MNNIT Allahabad · FTE · System Software Engineer](#2026-10-26--mnnit-allahabad--fte--system-software-engineer) · 1 question
- [2026-10-26 · MNNIT Allahabad · FTE · System Software Engineer · Interview](#2026-10-26--mnnit-allahabad--fte--system-software-engineer--interview) · 4 questions
- [2026-10-25 · VNIT Nagpur · FTE · System Software](#2026-10-25--vnit-nagpur--fte--system-software) · 1 question
- [2026-10-25 · IIT Dhanbad · Intern · System Software](#2026-10-25--iit-dhanbad--intern--system-software) · 2 questions
- [2026-10-21 · MNNIT Allahabad · FTE · Compiler](#2026-10-21--mnnit-allahabad--fte--compiler) · 1 question
- [2026-10-18 · Unknown · FTE · System Software](#2026-10-18--unknown--fte--system-software) · 1 question
- [2026-10-17 · MNNIT Allahabad · FTE · Software Compiler](#2026-10-17--mnnit-allahabad--fte--software-compiler) · 1 question
- [2026-10-16 · IIT BHU · Intern · Compiler Verification](#2026-10-16--iit-bhu--intern--compiler-verification) · 1 question

[← all companies](../README.md#companies)

---

## 2026-10-29 · NIT Delhi · Intern · HW Intern

### Q1. Smallest k making abcabc × p^k a perfect cube

A number N is of the form abcabc, where a, b and c are decimal digits between 1 and 9, including 1 and 9. The number abc is a perfect cube. N is multiplied by p^k.

For p = 7007, find the smallest non-zero value of k such that N × p^k is a perfect cube.

<sub>Topics: Math · Source: [chat, 29 Oct](../archive/nvidia-oa/2026-10.jsonl#L121)</sub>

### Q2. Clock buffers and max frequency with jitter

A sequential circuit consists of two identical flip-flops F1 and F2, a combinational logic cloud, and a number of clock buffers.

Given:
- Tsetup = 0.7 ns
- Thold = 0 ns
- Tclk-q = 0.5 ns
- Tpd = 1.1 ns
- Tcb = 0.1 ns
- F = 250 MHz
- Jitter J = 0.5%

Find:
1. How many clock buffers are present in the circuit for a zero-jitter clock source?
2. If the clock source has jitter equal to J of the rated clock period, what is the maximum rated clock frequency at which the circuit will operate correctly? Round off to the nearest integer.

<sub>Topics: Digital Electronics, Circuits · Source: [chat, 29 Oct](../archive/nvidia-oa/2026-10.jsonl#L121)</sub>

### Q3. Boolean expression from CMOS stick diagram

For the given CMOS stick diagram, A, B, C and D are inputs and Y is the output. VDD and GND are power rails. pDIFF denotes PMOS diffusion (pull-up network) and nDIFF denotes NMOS diffusion (pull-down network).

Derive the Boolean expression for Y.

(+ denotes OR, . denotes AND, and ' denotes NOT.)

The stick diagram itself was not included in the message.

<sub>Topics: Digital Electronics, Circuits · Source: [chat, 29 Oct](../archive/nvidia-oa/2026-10.jsonl#L121)</sub>

### Q4. Output bit width of product of two sums of N-bit numbers

A, B, C and D are N-bit unsigned integer variables.

The circuit performs the following operations:
1. Add A and B to obtain A + B.
2. Add C and D.
3. Multiply the two sums to obtain X.

Given N = 14, find the minimum number of bits required to store the output X.

<sub>Topics: Digital Electronics, Math · Source: [chat, 29 Oct](../archive/nvidia-oa/2026-10.jsonl#L121)</sub>

### Q5. Minimum clock cycles between states of D flip-flop circuit

Four D flip-flops are arranged so that the input of the first flip-flop is derived from a combinational circuit using the outputs of the other flip-flops. Initially, a clear signal is applied to the flip-flops. Subsequently, clocks are provided to each flip-flop, causing Q0, Q1, Q2 and Q3 to assume different values.

Assuming the start state is S (Q0Q1Q2Q3) and the final state is F (Q0Q1Q2Q3), determine the minimum number of clock cycles required to transition from the start state to the final state.

Consider:
- S = 0100
- F = 0010

The combinational logic feeding the first flip-flop was not included in the message.

<sub>Topics: Digital Electronics · Source: [chat, 29 Oct](../archive/nvidia-oa/2026-10.jsonl#L121)</sub>

## 2026-10-28 · NIT Rourkela · FTE · System Software Engineer

### Q1. Maximum Latency Path in a Tree

You are given a tree with N nodes numbered 1 to N and N-1 bidirectional edges. Each edge has a latency value W.

The latency of a path between two nodes is:

Path Latency = sum of W_e over edges e in P + max of W_e over edges e in P

where P is the unique path between the two nodes. Find the maximum possible path latency among all pairs of distinct nodes in the tree.

**Input Format**
- The first line contains an integer N, the number of nodes.
- The next N-1 lines each contain three integers U, V and W: a bidirectional edge between nodes U and V with latency W.

**Output Format**
Print a single integer: the maximum possible path latency among all pairs of distinct nodes.

(The message was cut off here, so the constraints and examples are missing.)

<sub>Topics: Trees, Graphs · Source: [chat, 28 Oct](../archive/intern-2027/2026-10.jsonl#L49)</sub>

## 2026-10-28 · NIT Meghalaya · Intern · Hardware (GPU)

### Q1. Smallest k making abcabc * 7007^k a perfect cube

A number N is of the form abcabc, where a, b and c are decimal digits between 1 and 9, including 1 and 9. The number abc is a perfect cube. N is multiplied by p^k.

For p = 7007, find the smallest non-zero value of k such that N × p^k is a perfect cube.

<sub>Topics: Math, Aptitude · Source: [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L37), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L38), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L40), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L41)</sub>

### Q2. Clock buffers and max frequency with jitter

A sequential circuit consists of two identical flip-flops F1 and F2, a combinational logic cloud, and a number of clock buffers.

Given:
- Tsetup = 0.7 ns
- Thold = 0 ns
- Tclk-q = 0.5 ns
- Tpd = 1.1 ns
- Tcb = 0.1 ns
- F = 250 MHz
- Jitter J = 0.5%

Find:
1. How many clock buffers are present in the circuit for a zero-jitter clock source?
2. If the clock source has jitter equal to J of the rated clock period, what is the maximum rated clock frequency at which the circuit will operate correctly? Round off to the nearest integer.

<sub>Topics: Digital Electronics, Circuits · Source: [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L37), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L38), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L40), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L41)</sub>

### Q3. Boolean expression from CMOS stick diagram

For the given CMOS stick diagram, A, B, C and D are inputs and Y is the output. VDD and GND are power rails. pDIFF denotes PMOS diffusion (pull-up network) and nDIFF denotes NMOS diffusion (pull-down network).

Derive the Boolean expression for Y.

(+ denotes OR, . denotes AND, and ' denotes NOT.)

The stick diagram itself was not included.

<sub>Topics: Digital Electronics, Analog Electronics · Source: [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L37), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L38), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L40), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L41)</sub>

### Q4. Output bits for product of two sums of N-bit numbers

A, B, C and D are N-bit unsigned integer variables.

The circuit performs the following operations:
1. Add A and B to obtain A + B.
2. Add C and D.
3. Multiply the two sums to obtain X.

Given N = 14, find the minimum number of bits required to store the output X.

<sub>Topics: Digital Electronics, Math · Source: [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L37), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L38), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L40), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L41)</sub>

### Q5. Minimum clocks between two states of 4 D flip-flops

Four D flip-flops are arranged so that the input of the first flip-flop is derived from a combinational circuit using the outputs of the other flip-flops. Initially, a clear signal is applied to the flip-flops. Subsequently, clocks are provided to each flip-flop, causing Q0, Q1, Q2 and Q3 to assume different values.

Assuming the start state is S (Q0Q1Q2Q3) and the final state is F (Q0Q1Q2Q3), determine the minimum number of clock cycles required to transition from the start state to the final state.

Consider:
- S = 0100
- F = 0010

The combinational circuit was not included.

<sub>Topics: Digital Electronics · Source: [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L37), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L38), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L40), [chat, 28 Oct](../archive/nvidia-oa/2026-10.jsonl#L41)</sub>

## 2026-10-28 · MNNIT Allahabad · FTE · System Software Engineer

### Q1. Nvidia System Software Engineer OA pattern

2 DSA questions of medium to hard difficulty, plus MCQs. No actual questions were shared.

<sub>Topics: OA Format · Source: [chat, 28 Oct](../archive/inter-nit/2026-10.jsonl#L2737)</sub>

## 2026-10-26 · MNNIT Allahabad · FTE

### Q1. OS for Autonomous Vehicles

(System Software Engineer, Round 2) Which OS will be used for autonomous vehicles and why? (Round 1 OA pattern: 2 LeetCode-medium coding questions + OS (medium) + COA (hard) + C++ output questions (easy-medium); minimum 60% needed to qualify. Round 2 also had three easy-medium LeetCode questions.)

<sub>Topics: OS/DBMS/CN MCQ, OA Format · Source: [chat, 26 Oct](../archive/inter-nit/2026-10.jsonl#L2436)</sub>

### Q2. How Stack Works in Recursion

(Round 3, Technical) Explain how the call stack works in recursion.

<sub>Topics: Recursion/Backtracking, Stack/Queue · Source: [chat, 26 Oct](../archive/inter-nit/2026-10.jsonl#L2436)</sub>

### Q3. Iterative In-order Traversal Using Stack

(Round 3, Technical) Implement in-order traversal of a binary tree using a stack, optimize it, and explain its time and space complexity.

<sub>Topics: Trees, Stack/Queue · Similar: [LeetCode 94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (Easy) · Source: [chat, 26 Oct](../archive/inter-nit/2026-10.jsonl#L2436)</sub>

### Q4. 32-bit Multiplication on 16-bit ALU

(Round 3, Technical) Write a C program to perform 32-bit multiplication on a microprocessor whose ALU only supports 16-bit multiplication.

<sub>Topics: Bit Manipulation, Math · Source: [chat, 26 Oct](../archive/inter-nit/2026-10.jsonl#L2436)</sub>

## 2026-10-26 · MNNIT Allahabad · FTE · System Software Engineer

### Q1. Nvidia System Software Engineer OA format

Round 1 was an OA with:
- Two coding questions (medium level, LeetCode style)
- OS (medium level)
- COA (hard level)
- C++ output questions (easy to medium)

A minimum of 60% was needed to qualify for the next round.

<sub>Topics: OA Format · Source: [chat, 26 Oct](../archive/intern-2027/2026-10.jsonl#L22)</sub>

## 2026-10-26 · MNNIT Allahabad · FTE · System Software Engineer · Interview

### Q1. Round 2: experience and OS for autonomous vehicles

Round 2 questions:
- Roles and responsibilities in the current organization.
- Which OS will be used for autonomous vehicles and why?
- Three easy to medium LeetCode questions (not specified).

<sub>Topics: HR & Behavioral, OS/DBMS/CN MCQ · Source: [chat, 26 Oct](../archive/intern-2027/2026-10.jsonl#L22)</sub>

### Q2. How a stack works in recursion

Technical round: explain how the stack works in recursion. The interviewer also asked about the candidate's current role in the company.

<sub>Topics: Recursion/Backtracking, Stack/Queue · Source: [chat, 26 Oct](../archive/intern-2027/2026-10.jsonl#L22)</sub>

### Q3. Iterative in-order traversal using a stack

Implement in-order traversal using a stack, optimize it, and explain the time and space complexity.

<sub>Topics: Trees, Stack/Queue · Similar: [LeetCode 94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (Easy) · Source: [chat, 26 Oct](../archive/intern-2027/2026-10.jsonl#L22)</sub>

### Q4. 32-bit multiplication on a 16-bit multiplier ALU

Write a C program for handling 32-bit multiplication on a microprocessor ALU that supports 16-bit multiplication.

<sub>Topics: Digital Electronics, Bit Manipulation · Source: [chat, 26 Oct](../archive/intern-2027/2026-10.jsonl#L22)</sub>

## 2026-10-25 · VNIT Nagpur · FTE · System Software

### Q1. Nvidia System Software OA: graph and DP questions

Two medium-level DSA questions were asked, based on graphs and dynamic programming. The poster did not give the exact problem statements.

<sub>Topics: Graphs, DP · Source: [chat, 25 Oct](../archive/intern-2027/2026-10.jsonl#L13)</sub>

## 2026-10-25 · IIT Dhanbad · Intern · System Software

### Q1. System Software OA structure

The OA has 4 sections:
- A coding question to be solved in 25 minutes
- Three MCQ sections based on: OS, compiler-related topics, and code output (C & C++ pointers)

<sub>Topics: OA Format · Source: [chat, 25 Oct](../archive/nvidia-oa/2026-10.jsonl#L16)</sub>

### Q2. Max path sum plus max edge in weighted tree

Given a tree with weighted edges, return the maximum possible value of f(u,v), where f(u,v) is the sum of the weights of the edges on the path from u to v plus the maximum-weight edge on that path.

<sub>Topics: Trees, Graphs, DP · Source: [chat, 25 Oct](../archive/nvidia-oa/2026-10.jsonl#L18)</sub>

## 2026-10-21 · MNNIT Allahabad · FTE · Compiler

### Q1. Message Delivery System (duplicate message filter)

Part B — C++20: Coding Question

Q6. Message Delivery System

A messaging app needs to prevent sending duplicate messages.

If a message with the same text was already delivered in the last k seconds, the new one is considered a duplicate and dropped.

Given a list of messages with their arrival times, return whether each message should be delivered (true) or marked as a duplicate (false).

Function signature

```cpp
vector<string> getMessageStatus(
    const vector<int>& timestamps,
    const vector<string>& messages,
    int k
);
```

Example 1

```
timestamps = [1, 4, 5, 9, 10, 14]
messages = ["hello", "bye", "bye", "bye", "bye", "hello"]
k = 5
Output: ["true", "true", "false", "false", "true", "true"]
```

Example 2

```
timestamps = [1, 1, 1, 11]
messages = ["message-2", "message-2", "message-3", "message-2"]
k = 5
Output: ["true", "false", "true", "true"]
```

Only the second message is dropped.

Constraints

- 1 <= n <= 10^5
- 1 <= |messages[i]| <= 15
- 1 <= timestamps[i] <= 10^6
- All messages contain lowercase English letters only.

<sub>Topics: Hashing, Strings, Arrays · Source: [chat, 21 Oct](../archive/nvidia-oa/2026-10.jsonl#L87)</sub>

## 2026-10-18 · Unknown · FTE · System Software

### Q1. System Software OA format

DSA coding questions were very basic, plus around 25 MCQs covering LLMs, Python, C and C++.

<sub>Topics: OA Format · Source: [chat, 18 Oct](../archive/nvidia-oa/2026-10.jsonl#L75)</sub>

## 2026-10-17 · MNNIT Allahabad · FTE · Software Compiler

### Q1. Nvidia OA format: 1 coding question and 20-25 MCQs

The Nvidia OA (software compiler role) had 1 coding question and 20-25 MCQs. The poster advised focusing on the MCQs because they carry more marks.

The actual questions were not shared.

<sub>Topics: OA Format · Source: [chat, 17 Oct](../archive/nvidia-oa/2026-10.jsonl#L64), [chat, 17 Oct](../archive/nvidia-oa/2026-10.jsonl#L66), [chat, 17 Oct](../archive/nvidia-oa/2026-10.jsonl#L67), [chat, 17 Oct](../archive/nvidia-oa/2026-10.jsonl#L69)</sub>

## 2026-10-16 · IIT BHU · Intern · Compiler Verification

### Q1. Nvidia compiler verification OA format

21 MCQs on C/C++, programming, data structures, and compiler output, plus one coding question (as told by a senior last year).

<sub>Topics: OA Format · Source: [chat, 16 Oct](../archive/intern-2027/2026-10.jsonl#L143), [chat, 16 Oct](../archive/intern-2027/2026-10.jsonl#L144)</sub>
