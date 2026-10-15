# Squarepoint OA

## 2026-10-15 · IIT Kharagpur · FTE

### Q1. Modulo Sum Function

Given a function C(i, j) = (i mod j) + (j mod i) for integers i and j, find f(n) = Σ(i=1..n) Σ(j=1..n) C(i, j) for a given n.

Constraints: n ≤ 10^6.

Hint from the sharer: C is symmetric, so f(n) = 2 × Σ (i mod j) over all pairs up to n; for a fixed j the sum can be computed with harmonic grouping or direct summation in O(n log n), instead of checking all pairs in O(n²).

Topics: Math  
📎 source: [SquarePoint_SDE_IITKGP (1).pdf](../archive/files/6947-SquarePoint_SDE_IITKGP_1_.pdf), [msg 6948](../archive/inter-nit/2026-10.jsonl)

### Q2. Tree Traversal Integrity (Valid BFS)

Given a tree and a sequence of vertices, determine whether the sequence is a valid Breadth-First Search (BFS) traversal of the tree. Tests graph representation and BFS queue management. Same as Codeforces 1037D - Valid BFS?

Topics: Trees, Graphs, Stack/Queue  
📎 source: [SquarePoint_SDE_IITKGP (1).pdf](../archive/files/6947-SquarePoint_SDE_IITKGP_1_.pdf), [msg 6948](../archive/inter-nit/2026-10.jsonl)

### Q3. Two Cores and a Latch (Optimal Operation Split)

Two cores process operations in a strictly given order. You are given an array time, where time[i] is the time needed to finish the i-th operation. A latch decides which core runs each operation. The core holding the latch can either assign the current operation to itself, which passes the latch to the other core, or assign the operation to the other core and keep the latch. Each core plays optimally to maximize its own total running time. Core 1 holds the latch initially. Return [total_time_core1, total_time_core2].

Example 1: Input [141, 592, 653] -> Output [733, 653] (Core 1 gives away 141 and keeps the latch, then runs 592 itself; the latch passes to Core 2, which runs 653).
Example 2: Input [10, 21, 10, 21, 10] -> Output [41, 31].

Similar problems: Codeforces 859C - Pie Rules (exact logic match), LeetCode 877 Stone Game, LeetCode 1140 Stone Game II.

Topics: DP  
📎 source: [SquarePoint_SDE_IITKGP (1).pdf](../archive/files/6947-SquarePoint_SDE_IITKGP_1_.pdf), [msg 6948](../archive/inter-nit/2026-10.jsonl)

## 2026-10-04 · IIT Roorkee · FTE

### Q1. Trade Packet Correction

You are given a list of trade records, trades. Each record has six integers: [time, price, qty, side, d1, d2].
- time: Timestamp of the trade. All trades with the same time form one packet.
- price: Price of the trade.
- qty: Quantity of the trade.
- side: 0 = no side, 1 = buy, 2 = sell.
- d1, d2: Identify the stock. If d2 == -1, the trade is in a simple stock with unique id d1. If d2 != -1, the trade is in a complex stock derived from the simple stocks with ids d1 and d2. The order of d1 and d2 matters: the complex stock (d1, d2) is different from (d2, d1).

The trades are sorted by time (trades[i].time >= trades[i-1].time), so every packet is a contiguous block of the array.

Correction rule: Inside a single packet, three trades A, B, C form a valid triple if:
- A is a simple-stock trade with id d1 and B is a simple-stock trade with id d2, where d1 and d2 are the components of C, which is a complex-stock trade (d1, d2).
- C.price == A.price - B.price.
- A.qty > 0, B.qty > 0 and C.qty > 0.
- Exactly one of the three trades has side != 0.
For every valid triple, let m = min(A.qty, B.qty, C.qty) and subtract m from the qty of the one trade whose side != 0. Apply this to every valid triple in every packet. A packet can contain several complex trades, and several trades can share the same simple stock id, so it can contain many triples.

Processing order: Triples are processed one at a time, ordered by the index of the complex trade C (ascending), then by the index of A (ascending), then by the index of B (ascending). Each triple is checked against the current quantities, which already include earlier corrections, so a trade whose quantity has dropped to 0 cannot take part in later triples. Corrections never cross packet boundaries.

Return the updated trades.

Input: trades: vector<vector<int>> of size n, where each element is [time, price, qty, side, d1, d2].
Output: The updated vector<vector<int>> after all corrections. Only qty values can change.

Constraints (suggested):
1 <= n <= 10^5
0 <= time, and time is non-decreasing
0 <= qty <= 10^9
side in {0, 1, 2}
d1 >= 0 and d2 >= -1
Prices fit in a 32-bit signed integer, and A.price - B.price does not overflow.

Example 1:
Input: trades = [[1,100,10,0,1,-1],[1,40,5,0,2,-1],[1,60,8,1,1,2],[2,50,3,2,3,-1]]
Output: [[1,100,10,0,1,-1],[1,40,5,0,2,-1],[1,60,3,1,1,2],[2,50,3,2,3,-1]]
Explanation: In packet time = 1, trade 2 is the complex stock (1, 2), and trades 0 and 1 are the simple stocks 1 and 2. The price check holds (100 - 40 = 60), all quantities are positive, and only trade 2 has side != 0. So m = min(10, 5, 8) = 5, and trade 2's quantity becomes 8 - 5 = 3. Packet time = 2 has no complex trade, so it is unchanged.

Example 2 (no correction):
Input: trades = [[1,100,10,1,1,-1],[1,40,5,0,2,-1],[1,60,8,2,1,2]]
Output: [[1,100,10,1,1,-1],[1,40,5,0,2,-1],[1,60,8,2,1,2]]
Explanation: Two of the three trades have side != 0, so the triple is not valid and nothing changes.

Notes: The complex stock (2, 1) would need a different complex trade. A trade (1, 2) must use A with id 1 and B with id 2, so the order of d1 and d2 matters.
Expected solution: scan once to find packet boundaries, then group the simple trades by stock id inside each packet and match each complex trade against them.

Topics: Arrays, Hashing  
📎 source: [msg 2757](../archive/inter-nit/2026-10.jsonl), [msg 2758](../archive/inter-nit/2026-10.jsonl)

## 2026-10-02 · IIT Roorkee · FTE

### Q1. Get Node To Remove (Flexport problem on FastPrep)

One of the Squarepoint OA questions, reported as exactly the same as the FastPrep problem 'Flexport – Get Node To Remove': https://www.fastprep.io/problems/flexport-get-node-to-remove (full statement not included in the message).

Topics: Graphs  
📎 source: [msg 2313](../archive/inter-iit/2026-10.jsonl), [msg 2314](../archive/inter-iit/2026-10.jsonl)

## 2026-10-02 · IIT Kanpur · FTE

### Q1. Search Suggestions System

Think of a search engine that has the vector `words` as its database. The string `search` is your current keyword. As you type the search word character by character, the search engine gives 3 suggestions whose prefixes match the current state of the search word, so you get a new recommendation list after each character typed. If more than three words in the database match the current prefix, return the three lexicographically smallest ones. If none match, return an empty list. Return the list of suggestion lists, one for each prefix of the search word.

Topics: Strings, Sorting, Binary Search  
📎 source: [msg 2288](../archive/inter-nit/2026-10.jsonl)
