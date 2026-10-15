# Eternal OA

## 2026-10-13 · IIT Dhanbad · FTE

### Q1. Binomial distribution: archer mean and variance

Product Analyst OA (90 minutes total: 20 aptitude/probability/statistics/quant/electrical-core MCQs, 2 SQL queries, 3 Python/Pandas MCQs and 2 Python/Pandas coding questions). If the probability that an archer strikes the target is 30% and the archer makes 10 attempts, what are the mean and variance of the number of successful attempts? Options: 3, 2.1; 3, 2.4; 7, 2.1; 7, 2.4.

Topics: Math, Aptitude  
📎 source: [Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf](../archive/files/5876-Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf), [msg 5878](../archive/inter-nit/2026-10.jsonl)

### Q2. Highest power of 24 dividing 150!

What is the highest power of 24 that divides 150! exactly? Options: 42, 44, 46, 48.

Topics: Math, Aptitude  
📎 source: [Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf](../archive/files/5876-Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf), [msg 5878](../archive/inter-nit/2026-10.jsonl)

### Q3. Normal distribution: P(mean > 55)

A dataset is normally distributed with mean 50 and standard deviation 5. What is the probability of selecting a sample with a mean greater than 55? Options: approximately 2.28%, 15.87%, 50%, 97.72%.

Topics: Math, Aptitude  
📎 source: [Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf](../archive/files/5876-Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf), [msg 5878](../archive/inter-nit/2026-10.jsonl)

### Q4. Painted cube: red and blue faces

A cube of side 18 cm has two opposite faces coloured red and the other four faces coloured blue. It is cut into 729 equal smaller cubes. How many of the smaller cubes have at least one red face and at least one blue face?

Topics: Aptitude  
📎 source: [Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf](../archive/files/5876-Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf), [msg 5878](../archive/inter-nit/2026-10.jsonl)

### Q5. Bayes: did it snow last night?

A girl knows the probability that it snows on any given night is 1/8. Her father tells her that it snowed last night. Her second daughter says the father lies with probability 5/6. Based on this, what is the probability that it actually snowed last night?

Topics: Math, Aptitude  
📎 source: [Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf](../archive/files/5876-Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf), [msg 5878](../archive/inter-nit/2026-10.jsonl)

### Q6. SQL: email campaign analysis

Tables: campaigns(id, campaign_name) and email_campaigns(campaign_id, emails_sent, emails_opened). For each campaign, output campaign_name, total_emails_sent, total_emails_opened and total_emails_not_opened, one row per campaign. Sample campaigns: (1, Summer Sale), (2, Diwali Offer), (3, New User Promo). Sample email_campaigns: (1, 1000, 700), (1, 500, 300), (2, 2000, 1200), (2, 1000, 600), (3, 800, 500). Expected output: Summer Sale 1500 1000 500; Diwali Offer 3000 1800 1200; New User Promo 800 500 300.

Topics: SQL  
📎 source: [Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf](../archive/files/5876-Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf), [msg 5878](../archive/inter-nit/2026-10.jsonl)

### Q7. SQL: device traffic and cost in May

Tables: devices(id, mac, tariff) and traffic(id, dt, amount). Join on device id. For each MAC address, output the total traffic during May as traffic and the cost (traffic x tariff) rounded to 2 decimal places, one row per MAC. Sample devices: (1, AA:BB:CC:DD:EE:01, 0.50), (2, AA:BB:CC:DD:EE:02, 0.60), (3, AA:BB:CC:DD:EE:03, 0.40). Sample traffic: (1, 2026-05-03, 100), (1, 2026-05-15, 50), (1, 2026-06-02, 200), (2, 2026-05-10, 200), (2, 2026-05-25, 120), (3, 2026-05-18, 150). Expected output: AA:BB:CC:DD:EE:01 150 75.00; AA:BB:CC:DD:EE:02 320 192.00; AA:BB:CC:DD:EE:03 150 60.00.

Topics: SQL  
📎 source: [Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf](../archive/files/5876-Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf), [msg 5878](../archive/inter-nit/2026-10.jsonl)

### Q8. Python / Pandas section (3 MCQs + 2 coding)

3 MCQs, mostly short Python/Pandas code-output or concept questions, covering DataFrame creation/selection, loc/iloc, Boolean filtering, column operations, missing values, groupby/aggregation, transform/filter, data-type conversion, dates, categorical data and pd.cut(). Then 2 relatively easy coding questions on practical tabular-data manipulation: loading data, cleaning/filtering, creating or transforming columns, grouping/aggregation and basic feature engineering. Exact questions were not recalled.

Topics: Other  
📎 source: [Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf](../archive/files/5876-Eternal_Product_Analyst_OA_IIT_Dhanbad.pdf), [msg 5878](../archive/inter-nit/2026-10.jsonl)

## 2026-10-02 · IIT (ISM) Dhanbad · FTE

### Q1. Second Most Frequent Element

You are given an integer array A of size N. Your task is to find the second most frequent distinct element in the array. The frequency of an element is the number of times it appears in the array.

Tie-Breaking Rule: If multiple elements have the same frequency, the greater element should be considered more frequent for ranking purposes. In other words, when comparing two elements:
- The element with the higher frequency ranks higher.
- If their frequencies are equal, the greater element ranks higher.

Return the element that ranks second according to these rules. (Poster's note: simple hash map.)

Topics: Hashing, Arrays, Sorting  
📎 source: [msg 2348](../archive/inter-nit/2026-10.jsonl)

### Q2. Fruit Selection with Discount Coupons

You are given N different fruits. Each fruit has:
- price[i]: the cost of the i-th fruit.
- nutrition[i]: the nutritional value you gain by eating the i-th fruit.

You have M units of money and K discount coupons. You want to maximize the total nutritional value of the fruits you purchase.

Coupon Rule:
- Each fruit can be purchased at most once.
- If you purchase a fruit without using a coupon, you pay its full price price[i].
- If you purchase a fruit using one coupon, you pay half its price, i.e. floor(price[i] / 2).
- Each coupon can be used on at most one fruit.
- You can choose not to use all your coupons.
- The total amount spent must not exceed M.

Return the maximum total nutrition you can obtain. (Poster's note: 3D DP, easy question.)

Topics: DP  
📎 source: [msg 2348](../archive/inter-nit/2026-10.jsonl)

### Q3. Minimum Sum Assignment on a Tree

You are given a tree with N nodes. Each node must be assigned a non-negative integer value. Some nodes already have fixed values, while the values of the remaining nodes are unknown.

For every edge (u, v) in the tree, the absolute difference between the values at adjacent nodes must not be less than exactly 1.

Your task is to assign values to all unassigned nodes such that:
- All pre-assigned values remain unchanged.
- For every edge (u, v), the absolute difference between their values is exactly 1.

(The message is cut off here. Going by the title, the goal is to minimise the sum of all assigned values.)

Topics: Trees, Graphs  
📎 source: [msg 2348](../archive/inter-nit/2026-10.jsonl)

## 2026-09-29 · IIT Guwahati · FTE

### Q1. OA pattern: 15 MCQs on OS, DBMS, SQL, CN, Docker

Eternal (Zomato) OA for SDE & PA roles. Duration: 90 min. 15 MCQs covering OS, DBMS, SQL, Computer Networks and Docker, plus 3 DSA questions.

Topics: OS/DBMS/CN MCQ, SQL  
📎 source: [msg 1841](../archive/inter-nit/2026-09.jsonl), [msg 1842](../archive/inter-nit/2026-09.jsonl)

### Q2. Second highest frequency element in an array

Given an array, find the element with the second highest frequency.

Topics: Arrays, Hashing  
📎 source: [msg 1841](../archive/inter-nit/2026-09.jsonl), [msg 1842](../archive/inter-nit/2026-09.jsonl)

### Q3. Collision problem

Collision problem (no further details shared; likely an asteroid-collision style problem).

Topics: Stack/Queue, Arrays  
📎 source: [msg 1841](../archive/inter-nit/2026-09.jsonl), [msg 1842](../archive/inter-nit/2026-09.jsonl)

### Q4. Maximize nutrition within a fixed budget

Given a price array and a nutrition array for items, and a fixed amount of money, choose items to earn the maximum total nutrition without exceeding the money (knapsack).

Topics: DP  
📎 source: [msg 1841](../archive/inter-nit/2026-09.jsonl), [msg 1842](../archive/inter-nit/2026-09.jsonl)

### Q5. Total energy of all subsequences (subset sum K)

You are given an array A of N integers and an integer K. For every non-empty subsequence of A, define its energy as the number of different ways to select elements from that subsequence such that their sum is exactly K. Each selection of elements is counted separately. Elements at different positions are considered different, even if they have the same value. The total energy of the array is the sum of the energies of all its non-empty subsequences.

Example: A = [1, 2, 3], K = 3
[3] -> {3} -> energy = 1
[1,2] -> {1,2} -> energy = 1
[1,3] -> {3} -> energy = 1
[2,3] -> {3} -> energy = 1
[1,2,3] -> {3}, {1,2} -> energy = 2
Total Energy = 1 + 1 + 1 + 1 + 2 = 6

Topics: DP, Math  
📎 source: [msg 1841](../archive/inter-nit/2026-09.jsonl), [msg 1842](../archive/inter-nit/2026-09.jsonl)

### Q6. Minimum steps with prime jumps

You are given an array A of N integers. You start at position 0 and need to reach position N-1. From your current position i, you can move to an adjacent position (i-1 or i+1) in 1 step. Additionally, if an adjacent element has a prime value p, you can make a prime jump to any position whose element is divisible by p. This jump also costs 1 step. Find the minimum number of steps required to move from position 0 to position N-1.

Example 1: A = [1, 2, 4, 6]; Path: 1 -> 2 -> 4

Topics: Graphs, Math  
📎 source: [msg 1841](../archive/inter-nit/2026-09.jsonl), [msg 1842](../archive/inter-nit/2026-09.jsonl)

## 2026-09-29 · IIT (ISM) Dhanbad · FTE

### Q1. Maximize Total Tastiness of Purchased Fruits (LeetCode 2431)

Shared as a link: https://leetcode.doocs.org/en/lc/2431/ (LeetCode 2431). You are given two non-negative integer arrays price and tastiness, both of length n, and two non-negative integers maxAmount and maxCoupons. price[i] is the price of the i-th fruit and tastiness[i] is its tastiness. Buy some fruits so that total tastiness is as large as possible and total price does not exceed maxAmount. A coupon lets you buy a fruit for half its price, rounded down. You can use at most maxCoupons coupons in total, buy each fruit at most once, and use at most one coupon per fruit. Return the maximum total tastiness.
Example 1: price = [10,20,20], tastiness = [5,8,8], maxAmount = 20, maxCoupons = 1 -> 13.
Example 2: price = [10,15,7], tastiness = [5,8,20], maxAmount = 10, maxCoupons = 2 -> 28.
Constraints: 1 <= n <= 100; 0 <= price[i], tastiness[i], maxAmount <= 1000; 0 <= maxCoupons <= 5.

Topics: DP, Arrays  
📎 source: [msg 1928](../archive/inter-nit/2026-09.jsonl), [msg 1932](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

### Q2. Snowflake OA graph problem (LeetCode Discuss 4062769)

Shared only as a link to a LeetCode Discuss post titled 'Snowflake OA graph problem': https://leetcode.com/discuss/post/4062769/snowflake-oa-graph-problem-by-anonymous_-cppn/ . The problem statement was not given in the chat.

Topics: Graphs  
📎 source: [msg 1928](../archive/inter-nit/2026-09.jsonl), [msg 1932](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

### Q3. Second most frequent element

Find the second most frequent element in the given array/collection. No more details were given.

Topics: Hashing, Sorting  
📎 source: [msg 1928](../archive/inter-nit/2026-09.jsonl), [msg 1932](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

### Q4. Aptitude and statistics MCQs (Product Analyst)

20 aptitude MCQs on topics such as mean, variance, escalator problems, probability, hypothesis testing, p-values, Type I error, and painted-cube problems, plus some core EE (electrical engineering) questions.

Topics: Aptitude, Math  
📎 source: [msg 1930](../archive/inter-nit/2026-09.jsonl), [msg 1931](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

### Q5. Python MCQs

2 MCQs on Python.

Topics: Other  
📎 source: [msg 1930](../archive/inter-nit/2026-09.jsonl), [msg 1931](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

### Q6. Key-value store with low/medium/high value levels

Python coding: process n operations of the form set(key, value) and get(key). Values fall into ranges: 0-10 is 'low', 11-20 is 'medium', and above that is 'high'. The output is true/false based on these levels. Only this partial description was given.

Topics: Hashing, Strings  
📎 source: [msg 1930](../archive/inter-nit/2026-09.jsonl), [msg 1931](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

### Q7. Clothes sizes stock check

Python coding: you are given the clothes sizes received (stock). For the sizes to be sold on the next date, say whether it is possible to sell them from the stock received. Only this partial description was given.

Topics: Hashing, Arrays  
📎 source: [msg 1930](../archive/inter-nit/2026-09.jsonl), [msg 1931](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

### Q8. SQL: basic join

An SQL query that needs a normal join between tables. No more details were given.

Topics: SQL  
📎 source: [msg 1930](../archive/inter-nit/2026-09.jsonl), [msg 1931](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

### Q9. SQL: join with date extraction for May totals

An SQL query using a join and date extraction: for the month of May, compute the total cost (number of requests * cost) and the total traffic (SUM(traffic)), and similar aggregates.

Topics: SQL  
📎 source: [msg 1930](../archive/inter-nit/2026-09.jsonl), [msg 1931](../archive/inter-nit/2026-09.jsonl), [msg 1934](../archive/inter-nit/2026-09.jsonl)

## 2026-09-28 · IIT BHU · FTE

### Q1. Aptitude section (Product Analyst)

Eternal Product Analyst OA: 20 aptitude questions covering sets, permutations & combinations, probability and other quantitative topics.

Topics: Aptitude  
📎 source: [msg 1665](../archive/inter-nit/2026-09.jsonl)

### Q2. SQL questions (one easy, one very hard)

Eternal Product Analyst OA: 2 SQL questions, one easy and one very hard.

Topics: SQL  
📎 source: [msg 1665](../archive/inter-nit/2026-09.jsonl)

### Q3. Python pandas question

Eternal Product Analyst OA: a Python pandas data-manipulation question.

Topics: Other  
📎 source: [msg 1665](../archive/inter-nit/2026-09.jsonl)
