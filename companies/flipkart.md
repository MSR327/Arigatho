# Flipkart OA

## 2026-10-24 · IIT Delhi · FTE

### Q1. ASCII Digit Checksum

Flipkart AI Engineer OA (3 coding questions, 90 minutes). Flipkart's messaging service tags every outgoing message with a small per-character checksum so corrupted characters can be spotted. You are given a message msg (a char[] in C++, a list of characters in Python). For each character, take its ASCII code and add up the decimal digits of that code (e.g. 'a' -> 97 -> 9 + 7 = 16). Return: print the digit sum for each character, one by one, in order.

Examples:
Input: msg = "Hi" -> Output: 9, 6 ('H' = 72 -> 7+2 = 9, 'i' = 105 -> 1+0+5 = 6)
Input: msg = "a!" -> Output: 16, 6 ('a' = 97 -> 16, '!' = 33 -> 6)
Input: msg = "A" -> Output: 11 ('A' = 65 -> 6+5 = 11)

Constraints: not recorded.

Topics: Strings, Math  
📎 source: [Flipkart - OA.pdf](../archive/files/14821-Flipkart_-_OA.pdf)

### Q2. Balanced-Parity Category Nodes

Flipkart's product catalogue is stored as a binary category tree. Each category has an id and a value, and an audit flags categories whose two sub-catalogues disagree in parity.
- You are given the id of the root node and an integer n.
- Then n lines follow, each 'path node': path is a string over L/R describing the route from the root (e.g. LRLR), and node is the id of the node at that position.
- Node ids are distinct but need not be consecutive (e.g. 11, 6, 22).
- You are also given an array value, where value[i] is the value of the i-th node (root first, then the nodes in input order).
- A node u is flagged if it has both a left and a right child, and the sum of values in its left child's subtree and the sum of values in its right child's subtree have different parity (one odd, one even).
Return: the sum of the ids of all flagged nodes.

Examples:
Input: root = 11, n = 4; L 6, R 22, LL 4, LR 9; value = [3, 1, 2, 4, 6] (nodes 11, 6, 22, 4, 9) -> Output: 11 (node 11: left {6,4,9} = 11 odd, right {22} = 2 even -> flagged; node 6: left {4} = 4, right {9} = 6, both even -> not flagged)
Input: root = 10, n = 6; L 3, R 25, LL 7, LR 14, RL 2, RR 30; value = [1, 2, 3, 4, 5, 6, 7] -> Output: 38 (node 10: 11 vs 16 flagged; node 3: 4 vs 5 flagged; node 25: 6 vs 7 flagged; 10+3+25 = 38)
Input: root = 5, n = 2; L 8, LL 1; value = [5, 1, 2] -> Output: 0 (no node has two children)

Constraints: n <= 1000 (recalled as 100 or 1000).

Topics: Trees, Recursion/Backtracking  
📎 source: [Flipkart - OA.pdf](../archive/files/14821-Flipkart_-_OA.pdf)

### Q3. Service Engineer (minimum days to finish all servicing)

Mona is an on-site service engineer for a laptop manufacturer. She works 8 hours a day, spending time either travelling to a site or providing service at the site. You are given an R x C matrix; each cell contains the time needed to complete servicing at that site (0 means no servicing required). Mona can move only horizontally or vertically and takes 2 hours to move to the next cell. Mona starts at cell (0, 0) and can finish in any cell. Find the minimum number of days in which she can complete all the tasks.

Input format: first line R and C; next R lines contain C values each (the cells of matrix).
Output format: print the minimum number of days.

Examples:
Input: 3 3 / 2 0 0 / 0 0 0 / 0 0 1 -> Output: 2 (servicing 2 + 1 = 3 h; route (0,0)->(2,2) = 4 units = 8 h; 11 h -> 2 days)
Input: 3 4 / 3 0 0 0 / 3 0 0 0 / 0 0 5 0 -> Output: 3 (servicing 11 h; route (0,0)->(1,0)->(2,2) = 4 units = 8 h; 19 h -> 3 days)
Input: 2 3 / 0 0 0 / 0 0 0 -> Output: 0 (no servicing required)

Constraints: 1 <= R <= 30, 1 <= C <= 30, 0 <= matrix[i][j] <= 1000; number of non-zero cells <= 15. Time limit 1 s, memory 256 MB.
Note: same as Goldman Sachs Coding Test II 'Service Engineer', except the start is fixed at (0, 0) (there, Mona can start and finish in any cell).

Topics: DP, Bit Manipulation, Graphs  
📎 source: [Flipkart - OA.pdf](../archive/files/14821-Flipkart_-_OA.pdf)

## 2026-10-22 · IIT BHU · FTE

### Q1. ASCII Sum Digit-Sum to Character

Flipkart AI Engineer role OA at IIT BHU. The test had 4 questions in 1.5 hours, and only Java/Python were allowed (no C++). You are given a string of lowercase letters. Convert each character to its ASCII integer value and add them all up. Then add up the digits of that sum. Finally, print the lowercase character that corresponds to that value.

Topics: Strings, Math  
📎 source: [msg 10604](../archive/inter-nit/2026-10.jsonl), [msg 10606](../archive/inter-nit/2026-10.jsonl)

### Q2. Max Distance from Non-Celebrating House to Celebrating House

You are given N, then some numbers between 1 and N. These are the coordinates of the houses celebrating Christmas. Find the maximum possible distance between a house that is not celebrating and a house that is celebrating (i.e. the largest distance from a non-celebrating house to its nearest celebrating house).

Topics: Arrays, Greedy  
📎 source: [msg 10604](../archive/inter-nit/2026-10.jsonl), [msg 10606](../archive/inter-nit/2026-10.jsonl)

### Q3. Count Graphs on n Nodes with k Components mod m

Described as the tough question. You are given three numbers n, k and m. Print (the number of possible graphs/subgraphs on n nodes with exactly k connected components) % m.

Topics: DP, Graphs, Math  
📎 source: [msg 10604](../archive/inter-nit/2026-10.jsonl), [msg 10606](../archive/inter-nit/2026-10.jsonl)

### Q4. SQL Left Join Question

A SQL question based on a LEFT JOIN. The poster did not share the exact schema or problem statement.

Topics: SQL  
📎 source: [msg 10604](../archive/inter-nit/2026-10.jsonl), [msg 10606](../archive/inter-nit/2026-10.jsonl)

## 2026-10-15 · MNNIT Allahabad · FTE

### Q1. Partition Seller Reviews into K Batches (Minimize Max Batch Sum)

Flipkart AI Engineer 1 OA. Flipkart is grouping seller reviews into batches based on structural similarity weights. You are given an array of integers weights of size N and an integer K. Partition the array into K contiguous subarrays (batches) so that the maximum sum of elements in any single subarray is as small as possible. Return that minimized maximum sum.
Constraints: 1 <= N <= 10^5; 1 <= weights[i] <= 10^6; 1 <= K <= N.

Topics: Binary Search, Greedy, Arrays  
📎 source: [msg 7093](../archive/inter-nit/2026-10.jsonl)
