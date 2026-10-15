# Harness OA

## 2026-10-13 · NIT Karnataka · FTE

### Q1. Maximum Memory Collection with Row Limit

You are given an n × m integer matrix memory, where memory[i][j] is the amount of memory that can be collected from cell (i, j). You start at the top-left cell (0, 0) and want to reach the bottom-right cell (n - 1, m - 1). At every cell you must do exactly one of these: (1) Read the current cell and collect its memory value, or (2) Skip the current cell and collect nothing. Then you must move one cell right or one cell down, staying inside the matrix. Constraint: in every row you may read at most k cells. Return the maximum total memory that can be collected.

Example 1: memory = [[4,5,9],[1,2,4],[6,5,2]], k = 2 → Output: 21. (Path (0,0)→(0,1)→(1,1)→(1,2)→(2,2) reading 4,5,2,4,2 gives 17; path (0,0)→(1,0)→(2,0)→(2,1)→(2,2) gives 4+6+5+2 = 17; an optimal strategy gives 21 while never reading more than 2 cells in any row.)
Example 2: memory = [[5,1],[3,7]], k = 1 → Output: 12 (read 5 from the first row and 7 from the second row).

Function signature: long long maximumMemory(vector<vector<int>>& memory, int k)
Constraints: 1 <= n, m <= 200; 1 <= memory[i][j] <= 10^9; 1 <= k <= m.
Expected approach: dp(i, j, cnt), where cnt is the number of cells already read in the current row and resets to 0 when moving down. Each cell has 4 choices (read/skip × right/down). Time and space O(n·m·k).
(Reconstructed by the poster from a whiteboard description, so it is approximate.)

Topics: DP, Arrays  
📎 source: [msg 6114](../archive/inter-nit/2026-10.jsonl), [Harness_SDE_NIT_Karanataka (3).pdf](../archive/files/6117-Harness_SDE_NIT_Karanataka_3_.pdf)

### Q2. Maximum Weight Tree After Degree Constraints

You are given an undirected weighted tree of n servers numbered 0 to n - 1, given as arrays g_from, g_to and g_weight: g_from[i] and g_to[i] are the endpoints of an edge and g_weight[i] is its weight. You are also given an integer k. You may remove any number of edges. After the removals, every server must have at most k incident edges. Return the maximum possible sum of the weights of the remaining edges.

Example 1: n = 5, g_from = [0,0,0,2], g_to = [1,2,3,4], g_weight = [10,20,5,15], k = 2 → Output: 45. Server 0 has degree 3, which is more than k, so remove edge (0,3) with weight 5. The remaining weight is 10 + 20 + 15 = 45.
Example 2: n = 4, g_from = [0,1,2], g_to = [1,2,3], g_weight = [4,7,5], k = 2 → Output: 16 (no edge needs to be removed).
Example 3: n = 6, g_from = [0,0,0,1,2], g_to = [1,2,3,4,5], g_weight = [8,6,10,5,9], k = 1 → Output: 19 (keep edges 0-3 (10) and 2-5 (9)).

Function signature: long long maximumWeight(int n, vector<int>& g_from, vector<int>& g_to, vector<int>& g_weight, int k)
Constraints: 2 <= n <= 2×10^5; g_from.length == g_to.length == g_weight.length == n - 1; 0 <= g_from[i], g_to[i] < n; 1 <= g_weight[i] <= 10^9; 1 <= k <= n - 1; the edges form a valid tree.
Expected approach: root the tree and run a post-order DFS tree DP with two states (dp0/dp1: whether the edge to the parent is kept). At each node, keep the best child gains after sorting them. O(N log N).

Topics: Trees, DP, Greedy  
📎 source: [msg 6114](../archive/inter-nit/2026-10.jsonl), [Harness_SDE_NIT_Karanataka (3).pdf](../archive/files/6117-Harness_SDE_NIT_Karanataka_3_.pdf)

## 2026-10-13 · IIT Guwahati · FTE

### Q1. Minimum Jumps in a Grid

You are given an n × m grid where each cell is 0 (empty) or 1 (obstacle), and an integer k. You start at cell (0, 0) and want to reach cell (n − 1, m − 1). In one move you jump x cells (1 ≤ x ≤ k) in one of the 4 directions. From (i, j) you can move right to (i, j + x), left to (i, j − x), down to (i + x, j) or up to (i − x, j). A jump is valid only if the destination is inside the grid and every cell along the jump, including the destination, is empty (you cannot jump over or land on an obstacle). Each jump costs 1, whatever its length. Return the minimum number of jumps to reach (n − 1, m − 1), or −1 if it is impossible.

Example 1: grid = [[0,0,0],[1,1,0],[0,0,0]], k = 2 → Output: 2 (jump right by 2 to (0,2), then down by 2 to (2,2)).
Example 2: same grid, k = 1 → Output: 4 ((0,0)→(0,1)→(0,2)→(1,2)→(2,2)).
Example 3: grid = [[0,1],[1,0]], k = 1 → Output: -1 (both moves out of (0,0) are blocked).

Constraints: 1 ≤ n, m ≤ 100; 1 ≤ k ≤ 100; grid[i][j] is 0 or 1.

Topics: Graphs, Arrays  
📎 source: [Harness_IITG_OA_Questions.pdf](../archive/files/6318-Harness_IITG_OA_Questions.pdf), [msg 6324](../archive/inter-nit/2026-10.jsonl), [Harness_IITG_OA_Questions.pdf](../archive/files/6332-Harness_IITG_OA_Questions.pdf)

### Q2. Tower Placement on a Tree

You are given a tree with n nodes numbered 0 to n − 1, described by arrays treeNode_from and treeNode_to of length n − 1, where each pair is an undirected edge. You may place a tower on any subset of nodes (including none or all), so there are 2^n possible placements. A node is active if it has a tower on it or is directly connected to a node with a tower. For every c from 0 to n, count the placements that make exactly c nodes active. Return an array of length n + 1 where index c holds that count.

Example 1: n = 3, treeNode_from = [0, 0], treeNode_to = [1, 2] → Output: [1, 0, 2, 5]. No towers gives 0 active nodes. {0} activates 3. {1} activates 2 ({0,1}) and {2} activates 2 ({0,2}). {0,1}, {0,2}, {1,2} and {0,1,2} each activate all 3.
Example 2: n = 2, treeNode_from = [0], treeNode_to = [1] → Output: [1, 0, 3].
Example 3: n = 4, treeNode_from = [0, 1, 2], treeNode_to = [1, 2, 3] (path 0–1–2–3) → Output: [1, 0, 2, 4, 9]. A tower only on node 0 or only on node 3 activates 2 nodes. {1}, {2}, {0,1} and {2,3} each activate 3. The remaining 9 placements activate all 4.

Constraints: not recorded (likely bounds on n, and possibly a modulo such as 10^9 + 7).

Topics: Trees, DP  
📎 source: [Harness_IITG_OA_Questions.pdf](../archive/files/6318-Harness_IITG_OA_Questions.pdf), [msg 6324](../archive/inter-nit/2026-10.jsonl), [Harness_IITG_OA_Questions.pdf](../archive/files/6332-Harness_IITG_OA_Questions.pdf)

### Q3. 10 MCQs on Backend, Testing and SQL

About 10 multiple-choice questions on backend development (REST APIs), software testing and SQL. The exact questions were not shared.

Topics: OS/DBMS/CN MCQ, SQL  
📎 source: [Harness_IITG_OA_Questions.pdf](../archive/files/6318-Harness_IITG_OA_Questions.pdf), [msg 6324](../archive/inter-nit/2026-10.jsonl), [Harness_IITG_OA_Questions.pdf](../archive/files/6332-Harness_IITG_OA_Questions.pdf)

## 2026-10-12 · NIT Surathkal · FTE

### Q1. Maximum Memory Collection with Row Limit

(Reconstructed from a student's description of the Harness SDE OA at NIT Karnataka.) You are given an n x m integer matrix memory, where memory[i][j] is the amount of memory that can be collected from cell (i, j). You start at the top-left cell (0, 0) and want to reach the bottom-right cell (n-1, m-1). At every cell you do exactly one of these: (1) Read the cell and collect its memory value, or (2) Skip the cell and collect nothing. Then you must move one cell right or one cell down, staying inside the matrix. Constraint: in each row you may read at most k cells. Return the maximum total memory you can collect.

Example 1: memory = [[4,5,9],[1,2,4],[6,5,2]], k = 2 -> Output: 21 (an optimal strategy gives 21 and never reads more than 2 cells in any row).
Example 2: memory = [[5,1],[3,7]], k = 1 -> Output: 12 (read 5 from the first row and 7 from the second row).

Function signature: long long maximumMemory(vector<vector<int>>& memory, int k);
Constraints: 1 <= n, m <= 200; 1 <= memory[i][j] <= 10^9; 1 <= k <= m.
Hint given: DP over state dp(i, j, cnt), where cnt is the number of cells already read in the current row and resets when you move down. Four choices at each cell: read+right, skip+right, read+down, skip+down. O(n*m*k) time.

Topics: DP, Arrays  
📎 source: [Harness_SDE_NIT_Karanataka.pdf](../archive/files/5533-Harness_SDE_NIT_Karanataka.pdf)

### Q2. Maximum Weight Tree After Degree Constraints

(Reconstructed from a student's description of the Harness OA.) You are given an undirected weighted tree with n servers numbered 0 to n-1, given as arrays g_from, g_to, g_weight: edge i connects g_from[i] and g_to[i] and has weight g_weight[i]. You are also given an integer k. You may remove any number of edges. After the removals, every server must have at most k incident edges. Return the maximum possible sum of the weights of the remaining edges.

Example 1: n = 5, g_from = [0,0,0,2], g_to = [1,2,3,4], g_weight = [10,20,5,15], k = 2 -> Output: 45 (server 0 has degree 3, so remove edge (0,3) of weight 5; 10+20+15 = 45).
Example 2: n = 4, g_from = [0,1,2], g_to = [1,2,3], g_weight = [4,7,5], k = 2 -> Output: 16 (no edge needs to be removed).
Example 3: n = 6, g_from = [0,0,0,1,2], g_to = [1,2,3,4,5], g_weight = [8,6,10,5,9], k = 1 -> Output: 19 (keep edges 0-3 (10) and 2-5 (9)).

Function signature: long long maximumWeight(int n, vector<int>& g_from, vector<int>& g_to, vector<int>& g_weight, int k);
Constraints: 2 <= n <= 2*10^5; g_from.length == g_to.length == g_weight.length == n-1; 0 <= g_from[i], g_to[i] < n; 1 <= g_weight[i] <= 10^9; 1 <= k <= n-1; the edges form a valid tree.
Expected approach: O(N log N) tree DP. Root the tree, run a post-order DFS with two states (dp0/dp1), and pick which child edges to keep by sorting the gains.

Topics: Trees, DP, Greedy  
📎 source: [Harness_SDE_NIT_Karanataka.pdf](../archive/files/5533-Harness_SDE_NIT_Karanataka.pdf)

### Q3. Maximum Memory Collection with Row Limit

(Reconstructed by AI from a description of the OA question.) You are given an n × m integer matrix memory, where memory[i][j] is the amount of memory that can be collected from cell (i, j). You start at the top-left cell (0, 0) and want to reach the bottom-right cell (n-1, m-1). At every cell you do exactly one of: (1) Read the current cell and collect its memory value, or (2) Skip the current cell and collect nothing. Then you must move one cell right or one cell down, staying inside the matrix. Constraint: in every row you may read at most k cells. Return the maximum total memory that can be collected.
Example 1: memory = [[4,5,9],[1,2,4],[6,5,2]], k = 2 → Output 21 (never reading more than 2 cells from any row).
Example 2: memory = [[5,1],[3,7]], k = 1 → Output 12 (read 5 from the first row and 7 from the second).
Function signature: long long maximumMemory(vector<vector<int>>& memory, int k).
Constraints: 1 <= n, m <= 200; 1 <= memory[i][j] <= 10^9; 1 <= k <= m.
Intended approach: dp(i, j, cnt), where cnt = cells read so far in the current row (it resets when moving down). Transitions are read/skip × right/down. O(n·m·k).

Topics: DP, Arrays  
📎 source: [Harness_SDE_NIT_Karanataka.pdf](../archive/files/5808-Harness_SDE_NIT_Karanataka.pdf)

### Q4. Maximum Weight Tree After Degree Constraints

(Reconstructed by AI from a description of the OA question.) You are given an undirected weighted tree of n servers numbered 0 to n-1, given as arrays g_from, g_to, g_weight: edge i connects g_from[i] and g_to[i] with weight g_weight[i]. You are also given an integer k. You may remove any number of edges so that afterwards every server has at most k incident edges. Return the maximum possible sum of the weights of the remaining edges.
Example 1: n = 5, g_from = [0,0,0,2], g_to = [1,2,3,4], g_weight = [10,20,5,15], k = 2 → Output 45 (server 0 has degree 3, so remove edge (0,3) of weight 5; 10+20+15 = 45).
Example 2: n = 4, g_from = [0,1,2], g_to = [1,2,3], g_weight = [4,7,5], k = 2 → Output 16 (no edge needs removing).
Example 3: n = 6, g_from = [0,0,0,1,2], g_to = [1,2,3,4,5], g_weight = [8,6,10,5,9], k = 1 → Output 19 (keep 0-3 (10) and 2-5 (9)).
Function signature: long long maximumWeight(int n, vector<int>& g_from, vector<int>& g_to, vector<int>& g_weight, int k).
Constraints: 2 <= n <= 2×10^5; g_from.length == g_to.length == g_weight.length == n-1; 0 <= g_from[i], g_to[i] < n; 1 <= g_weight[i] <= 10^9; 1 <= k <= n-1; the edges form a valid tree.
Intended approach: root the tree and run a post-order DFS tree DP with two states (dp0/dp1, i.e. whether the edge to the parent is kept), keeping the best k child gains after sorting. O(N log N).

Topics: Trees, DP, Greedy  
📎 source: [Harness_SDE_NIT_Karanataka.pdf](../archive/files/5808-Harness_SDE_NIT_Karanataka.pdf)

## 2026-10-11 · NIT Surathkal · FTE

### Q1. Maximum Memory Collection with Row Limit

You are given an n x m integer matrix memory, where memory[i][j] is the amount of memory that can be collected from cell (i, j). You start at the top-left cell (0, 0) and want to reach the bottom-right cell (n-1, m-1). At every cell you do exactly one of these: (1) Read the cell and collect its memory value, or (2) Skip the cell and collect nothing. Then you must move one cell right or one cell down, staying inside the matrix. Constraint: in each row you may read at most k cells. Return the maximum total memory that can be collected.

Example 1: memory = [[4,5,9],[1,2,4],[6,5,2]], k = 2 -> Output: 21 (the path (0,0)->(0,1)->(1,1)->(1,2)->(2,2) collects 17, and a better total of 21 exists without reading more than 2 cells in any row).
Example 2: memory = [[5,1],[3,7]], k = 1 -> Output: 12 (read 5 from the first row and 7 from the second row).

Function signature: long long maximumMemory(vector<vector<int>>& memory, int k)
Constraints: 1 <= n, m <= 200; 1 <= memory[i][j] <= 10^9; 1 <= k <= m.
(The question was reconstructed from a student's memory. Intended approach: dp(i, j, cnt), where cnt is the number of cells read in the current row and resets when moving down. Time O(nmk).)

Topics: DP, Arrays  
📎 source: [Harness_SDE_NIT_Karanataka.pdf](../archive/files/5416-Harness_SDE_NIT_Karanataka.pdf)

### Q2. Maximum Weight Tree After Degree Constraints

You are given an undirected weighted tree with n servers numbered 0 to n-1, given as arrays g_from, g_to and g_weight: there is an edge between g_from[i] and g_to[i] with weight g_weight[i]. You are also given an integer k. You may remove any number of edges so that every server has at most k incident edges. Return the maximum possible sum of the weights of the remaining edges.

Example 1: n = 5, g_from = [0,0,0,2], g_to = [1,2,3,4], g_weight = [10,20,5,15], k = 2 -> Output: 45 (server 0 has degree 3, so remove edge (0,3) of weight 5; 10 + 20 + 15 = 45).
Example 2: n = 4, g_from = [0,1,2], g_to = [1,2,3], g_weight = [4,7,5], k = 2 -> Output: 16 (no edge needs to be removed).
Example 3: n = 6, g_from = [0,0,0,1,2], g_to = [1,2,3,4,5], g_weight = [8,6,10,5,9], k = 1 -> Output: 19 (keep edges 0-3 (10) and 2-5 (9)).

Function signature: long long maximumWeight(int n, vector<int>& g_from, vector<int>& g_to, vector<int>& g_weight, int k)
Constraints: 2 <= n <= 2*10^5; g_from.length == g_to.length == g_weight.length == n-1; 0 <= g_from[i], g_to[i] < n; 1 <= g_weight[i] <= 10^9; 1 <= k <= n-1; the edges form a valid tree.
(Reconstructed version. Expected approach: tree DP with a post-order DFS and two states (dp0/dp1), sorting child gains to pick the best edges to keep, O(N log N).)

Topics: Trees, DP, Greedy  
📎 source: [Harness_SDE_NIT_Karanataka.pdf](../archive/files/5416-Harness_SDE_NIT_Karanataka.pdf)

## 2026-10-10 · NIT Surathkal · FTE

### Q1. Maximum Memory Collection with Row Limit

(Reconstructed from a candidate's description.) You are given an n x m integer matrix memory, where memory[i][j] is the memory that can be collected from cell (i, j). Start at the top-left cell (0, 0) and reach the bottom-right cell (n-1, m-1). At every cell you do exactly one of: (1) Read the cell and collect its value, or (2) Skip it and collect nothing. Then move one cell right or one cell down, staying inside the matrix. Constraint: in every row you may read at most k cells. Return the maximum total memory that can be collected.
Example 1: memory = [[4,5,9],[1,2,4],[6,5,2]], k = 2 -> Output 21.
Example 2: memory = [[5,1],[3,7]], k = 1 -> Output 12 (read 5 from the first row and 7 from the second).
Signature: long long maximumMemory(vector<vector<int>>& memory, int k).
Constraints: 1 <= n, m <= 200; 1 <= memory[i][j] <= 10^9; 1 <= k <= m.
Expected approach: dp(i, j, cnt), where cnt = cells read so far in the current row (resets when moving down); O(n*m*k).

Topics: DP, Arrays  
📎 source: [Harness_SDE_NIT_Karanataka.pdf](../archive/files/4815-Harness_SDE_NIT_Karanataka.pdf)

### Q2. Maximum Weight Tree After Degree Constraints

(Reconstructed from a candidate's description.) You are given an undirected weighted tree of n servers numbered 0 to n-1, given as arrays g_from, g_to and g_weight (edge i joins g_from[i] and g_to[i] with weight g_weight[i]), and an integer k. Remove any number of edges so that every server has at most k incident edges. Return the maximum possible sum of the weights of the remaining edges.
Example 1: n = 5, g_from = [0,0,0,2], g_to = [1,2,3,4], g_weight = [10,20,5,15], k = 2 -> Output 45 (remove edge (0,3) of weight 5).
Example 2: n = 4, g_from = [0,1,2], g_to = [1,2,3], g_weight = [4,7,5], k = 2 -> Output 16.
Example 3: n = 6, g_from = [0,0,0,1,2], g_to = [1,2,3,4,5], g_weight = [8,6,10,5,9], k = 1 -> Output 19 (as given: keep 0-3 and 2-5).
Signature: long long maximumWeight(int n, vector<int>& g_from, vector<int>& g_to, vector<int>& g_weight, int k).
Constraints: 2 <= n <= 2*10^5; the arrays have length n-1; 0 <= g_from[i], g_to[i] < n; 1 <= g_weight[i] <= 10^9; 1 <= k <= n-1; the edges form a valid tree.
Expected approach: root the tree, post-order DFS, tree DP with two states (dp0/dp1) that picks the best child edges by gain; O(N log N).

Topics: Trees, DP, Greedy  
📎 source: [Harness_SDE_NIT_Karanataka.pdf](../archive/files/4815-Harness_SDE_NIT_Karanataka.pdf)

## 2026-10-07 · MNNIT Allahabad · FTE

### Q1. Energy-Decay Graph

A robot is moving through a directed network of N locations connected by M one-way links. Every location i has a recharge value R[i]. The robot initially stands at location 1 and starts with S units of energy.

Each link is described by four values: u v cost loss.

To move from location u to location v:
1. The robot must currently possess at least cost units of energy.
2. cost units are consumed for making the move.
3. An additional amount of energy is lost because of the history of the destination location.
4. After arriving at v, the robot receives R[v] units of energy.

The historical loss works as follows. For every location v, maintain a counter representing how many times that location has previously been entered. If the current counter of v is x, then entering v through an edge having loss value d causes an additional energy loss of d * (x + 1). After the robot receives the recharge R[v], the counter of v is advanced.

However, the robot's controller can store only K different states for each counter. Therefore, after reaching K, the counter cycles back to 0. In other words, the stored counter evolves as 0 -> 1 -> 2 -> ... -> K-1 -> 0 -> 1 -> ... The counter value used for an arrival is the value stored immediately before that arrival.

The robot is never allowed to have negative energy. It may use any directed link repeatedly and may revisit locations any number of times.

Determine the greatest number of link traversals that can be completed. If there exists a strategy allowing the robot to perform arbitrarily many traversals, output -1.

Input Format:
The first line contains: N M S K
The second line contains: R[1] R[2] ... R[N]
Each of the following M lines contains: u v cost loss, describing a directed link from u to v.

Output Format:
Output one integer. If only a finite number of traversals is possible, output the maximum number of traversals. If the robot can make i[nfinitely many traversals, output -1]. (Message text was cut off here; no constraints or examples were shown.)

Topics: Graphs, DP  
📎 source: [msg 3641](../archive/inter-iit/2026-10.jsonl), [msg 3650](../archive/inter-nit/2026-10.jsonl), [msg 3651](../archive/inter-nit/2026-10.jsonl)

### Q2. 3Sum Closest

Given an integer array nums and an integer target, find three integers in nums such that their sum is closest to target. Return the sum of the three integers.
Example: nums = [-1, 2, 1, -4], target = 1 -> Output: 2

Topics: Two Pointers, Sorting, Arrays  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q3. Subarray Sum Equals K

Given an integer array nums and an integer K, count the number of continuous subarrays whose sum is equal to K. (Example truncated in message: nums = [1 ...)

Topics: Hashing, Arrays  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q4. Count Good Subarrays

Given an array of integers, count the number of subarrays satisfying the given "good" condition. The condition is based on the frequency of elements inside the subarray.
Example: Input: [1, 2, 1, 2] -> Output: [Determine according to the specified frequency condition]

Topics: Sliding Window, Hashing, Arrays  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q5. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring containing no repeated characters.
Example: Input: abcabcbb -> Output: 3

Topics: Strings, Sliding Window, Hashing  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q6. Merge Overlapping Intervals

Given a collection of intervals, merge all overlapping intervals.
Example: Input: [[1,3],[2,6],[8,10],[9,12]] -> Output: [[1,6],[8,12]]

Topics: Sorting, Arrays  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q7. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest sequence of consecutive integers. Expected complexity: O(N).

Topics: Hashing, Arrays  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q8. LRU Cache

Design an LRU Cache supporting get(key) and put(key, value). Both operations should work in O(1) average time.

Topics: Hashing, Linked List  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q9. First Non-Repeating Character

Given a string, find the first character that occurs exactly once.
Example: Input: swiss -> Output: w

Topics: Strings, Hashing  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q10. Detect Cycle in Directed Graph

Given a directed graph with N vertices and M edges, determine whether the graph contains a cycle. Return true if a cycle exists, otherwise return false.

Topics: Graphs  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)

### Q11. Number of Islands

Given a binary matrix containing '0' and '1', find the number of connected groups of '1's. Adjacent cells are connected horizontally and vertically.

Topics: Graphs  
📎 source: [msg 3659](../archive/inter-nit/2026-10.jsonl)
