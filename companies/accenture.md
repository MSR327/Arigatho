# Accenture OA

## 2026-10-12 · IIT Hyderabad · FTE

### Q1. Remaining Water After Watering Trees

You are given N trees and K units of total water. Each tree initially requires M units of water. For the ith tree: array1[i] is the number of additional times the tree needs to be watered, and array2[i] is the amount of water needed for each additional watering. The total water required by the ith tree is M + (array1[i] × array2[i]). Calculate and return the amount of water left after watering all N trees. If the total water required is greater than K, return 0.
Input: integer N (number of trees), integer K (total available water), integer M (initial water requirement of each tree), array array1 of size N, array array2 of size N.
Output: max(0, K - totalWaterRequired).
(The poster says the actual wording may have differed slightly.)

Topics: Arrays, Math  
📎 source: [msg 5796](../archive/inter-nit/2026-10.jsonl)

### Q2. SQL Query Joining 3 Tables

An SQL query that joins 3 tables using multiple join conditions, GROUP BY and IS NULL. The poster found the schema too complex to understand and did not share it.

Topics: SQL  
📎 source: [msg 5796](../archive/inter-nit/2026-10.jsonl)

### Q3. Web Dev Task (HTML/CSS/JS)

A frontend task in HTML, CSS and JavaScript. Hints are given in comments for each step (e.g. change the colour from this to this), and the JS part works the same way. Tip from the poster: go over the basics of each component and write the code 3-4 times. HTML/CSS hardly need practice; focus on JS.

Topics: Other  
📎 source: [msg 5796](../archive/inter-nit/2026-10.jsonl)

## 2026-10-12 · IIT Dhanbad · FTE

### Q1. MCQ section (Accenture Japan OA pattern)

Accenture Japan OA at IIT Dhanbad: 20 MCQs in 20 minutes, then 1 coding question in 60 minutes (80 minutes total). The MCQs covered LLM / Generative AI, aptitude, pseudocode / output-prediction questions, SQL, and CS fundamentals (mainly Operating Systems and Cloud Computing). The OS and Cloud questions were reported to be relatively easy. Any programming language was allowed for the coding question.

Topics: OS/DBMS/CN MCQ, Aptitude, SQL  
📎 source: [Accenture_Japan_OA_IIT_Dhanbad.pdf](../archive/files/5557-Accenture_Japan_OA_IIT_Dhanbad.pdf)

### Q2. Morse Code Dictionary Decode (Set 1)

You are given a Morse-code mapping table in which each English letter maps to a sequence of '.' and '-'. Given a string written in Morse code (with no separators between letters), decode it and print an English word whose Morse-code representation matches the input. The word must be present in the provided dictionary.txt file. If several dictionary words match, print any one of them.
Input: a Morse-code string, plus the Morse mapping table for the alphabet.
Output: any valid word from dictionary.txt whose Morse encoding equals the input.

Topics: Strings, Hashing, Recursion/Backtracking  
📎 source: [Accenture_Japan_OA_IIT_Dhanbad.pdf](../archive/files/5557-Accenture_Japan_OA_IIT_Dhanbad.pdf)

### Q3. Minimum Dice Rolls to Reach the End (Set 2)

You are given an array A of N non-negative integers. You start at index 0 and need to reach any index >= N. At any index i you can do one of two things: (1) Roll a special die: choose any value from 1 to 6 and jump forward that many positions. This counts as one dice roll. (2) Use the value at the current index: jump forward exactly A[i] positions. This costs no dice roll. Find the minimum number of dice rolls needed to reach an index >= N.
Example: N = 10, A = [0, 0, 0, 0, 0, 1, 1, 1, 1] -> Output: 1.
(Similar to LeetCode 45 Jump Game II, but with the extra die move and free jumps based on array values.)

Topics: DP, Graphs, Greedy  
📎 source: [Accenture_Japan_OA_IIT_Dhanbad.pdf](../archive/files/5557-Accenture_Japan_OA_IIT_Dhanbad.pdf)

### Q4. MCQ section (20 MCQs, 20 min)

Accenture Japan (digital consulting) OA at IIT Dhanbad: 20 MCQs in 20 minutes, then 1 coding question in 60 minutes (any programming language allowed). The MCQs covered LLM / Generative AI, aptitude, pseudocode / output-based questions, SQL, and computer science fundamentals, mainly Operating Systems and Cloud Computing. The OS and cloud questions were reported to be relatively easy.

Topics: OS/DBMS/CN MCQ, Aptitude, SQL  
📎 source: [msg 5845](../archive/inter-nit/2026-10.jsonl)

### Q5. Morse Code Dictionary (Set 1)

A Morse-code mapping table is provided in which each English letter maps to a Morse code made of '.' and '-'. Given a string in Morse code, decode it and output an English word. The decoded word must be present in the provided dictionary.txt file, and its Morse-code representation must match the given input. If several valid dictionary words can be generated, print any one. Input: a Morse-code string, plus the Morse-code mapping table for the alphabet. Output: any valid word from dictionary.txt whose Morse-code representation matches the input.

Topics: Strings, Hashing, Recursion/Backtracking  
📎 source: [msg 5845](../archive/inter-nit/2026-10.jsonl)

### Q6. Minimum Dice Rolls to Reach the End (Set 2)

You are given an array A of N non-negative integers. You start at index 0 and need to reach an index >= N. A special die is available: you can choose any number from 1 to 6 whenever you roll it. At any index there are two possible actions: (1) roll the die and choose any value from 1 to ... [the message is cut off here; the second action and the exact objective (presumably the minimum number of dice rolls to reach the end) are not visible].

Topics: DP, Arrays  
📎 source: [msg 5845](../archive/inter-nit/2026-10.jsonl)

## 2026-10-11 · IIT Dhanbad · FTE

### Q1. MCQ Section (20 MCQs, 20 min)

Accenture Japan OA pattern: 20 MCQs (20 minutes) followed by 1 coding question (60 minutes), 80 minutes total. The MCQs covered LLM / Generative AI, Aptitude, Pseudocode / output-based questions, SQL, and Computer Science fundamentals (mainly Operating Systems and Cloud Computing). The OS and Cloud Computing questions were reported to be relatively easy.

Topics: OS/DBMS/CN MCQ, Aptitude, SQL  
📎 source: [Accenture_Japan_OA_IIT_Dhanbad.pdf](../archive/files/5238-Accenture_Japan_OA_IIT_Dhanbad.pdf)

### Q2. Morse Code Dictionary (Set 1)

A Morse-code mapping table is provided, where each English letter maps to a Morse-code representation made of '.' and '-'. Given a string written in Morse code (with no separators between letters), decode it and output a matching English word. The decoded word must be present in the provided dictionary.txt file.
Constraints: the output word must be present in dictionary.txt; the word's Morse-code representation must match the given input; if several dictionary words match, print any one of them.
Input: a Morse-code string, along with the Morse-code mapping table for the alphabet.
Output: any valid word from dictionary.txt whose Morse-code representation matches the input.
(1 coding question, 60 minutes, all languages allowed.)

Topics: Strings, Hashing, Recursion/Backtracking  
📎 source: [Accenture_Japan_OA_IIT_Dhanbad.pdf](../archive/files/5238-Accenture_Japan_OA_IIT_Dhanbad.pdf)

### Q3. Minimum Dice Rolls to Reach the End (Set 2)

You are given an array A of N non-negative integers. You start at index 0 and need to reach an index >= N. A special die is available, and you can choose any number from 1 to 6 whenever you roll it. At any index i there are two possible actions:
- Roll the die: choose any value from 1 to 6 and jump forward that many positions. This counts as one dice roll.
- Use the value at the current index: jump forward exactly A[i] positions. This does not need a dice roll.
Find the minimum number of dice rolls needed to reach an index >= N.
Example: N = 10, A = [0, 0, 0, 0, 0, 1, 1, 1, 1] -> Output: 1.
The PDF notes that the jump structure is similar to LeetCode 45 (Jump Game II), with an extra die operation and free jumps based on the array value.

Topics: DP, Graphs, Arrays  
📎 source: [Accenture_Japan_OA_IIT_Dhanbad.pdf](../archive/files/5238-Accenture_Japan_OA_IIT_Dhanbad.pdf)

## 2026-10-10 · VIT Vellore · FTE

### Q1. Destination and Booking Revenue Analysis

You are given a large relational database containing the following tables:

Destination Table
| Column Name | Description |
| destination_id | Unique destination identifier |
| destination_name | Name of the destination |

Booking Table
| Column Name | Description |
| booking_id | Unique booking identifier |
| destination_id | Destination associated with the booking |
| revenue | Revenue generated by the booking |

Write an SQL query to retrieve the total booking revenue generated by each destination. Display the destination name and its total revenue.

(Note from poster: reconstructed exam-style question based on notes; exact original wording and requirements may differ.)

Topics: SQL  
📎 source: [msg 4683](../archive/inter-iit/2026-10.jsonl)

## 2026-10-10 · IIT Hyderabad · FTE

### Q1. Remaining water after watering trees

You are given N trees and K units of total water. Each tree initially requires M units of water. For the ith tree, array1[i] is the number of additional times the tree needs to be watered and array2[i] is the amount of water needed for each additional watering. The total water required by the ith tree is M + (array1[i] × array2[i]). Calculate and return the water remaining after watering all N trees. If the total water required is greater than K, return 0.
Input: integer N (number of trees), integer K (total available water), integer M (initial requirement per tree), array array1 of size N, array array2 of size N.
Output: max(0, K - totalWaterRequired).

Topics: Arrays, Math  
📎 source: [msg 4967](../archive/inter-iit/2026-10.jsonl)

### Q2. SQL three-table join

SQL query joining 3 tables using GROUP BY, IS NULL and multiple join conditions (complex schema; exact question not shared).

Topics: SQL  
📎 source: [msg 4967](../archive/inter-iit/2026-10.jsonl)

### Q3. Web dev HTML/CSS/JS task

Web development task (HTML, CSS, JS): follow the hints in the code comments (e.g. change a colour from X to Y) and complete the JS part as described in the comments.

Topics: Other  
📎 source: [msg 4967](../archive/inter-iit/2026-10.jsonl)

### Q4. Count contiguous groups of same-sign elements

Given an array of integers containing positive and negative elements, find the number of contiguous groups in which all elements have the same sign. A new group starts whenever the sign changes between two consecutive elements.
Example: arr = [1, 2, -3, -4, 5] -> Output: 3 (groups [1, 2], [-3, -4], [5]).

Topics: Arrays  
📎 source: [msg 4968](../archive/inter-iit/2026-10.jsonl)

### Q5. SQL join between 3 tables

SQL query requiring a JOIN between 3 tables (exact question not shared). Role: Elite Technology Engineer.

Topics: SQL  
📎 source: [msg 4968](../archive/inter-iit/2026-10.jsonl)

### Q6. JavaScript frontend task

JavaScript frontend task: follow the instructions given in the question; basic DOM understanding is enough.

Topics: Other  
📎 source: [msg 4968](../archive/inter-iit/2026-10.jsonl)

## 2026-10-10 · IIT Hyderabad · Unknown

### Q1. Destinations with more than 2 hotels (SQL practice)

Practice question. Tables: Destination(destination_id, destination_name) with rows (1, Goa), (2, Mumbai), (3, Jaipur), (4, Manali); Hotel(hotel_id, destination_id, night_rate) with rows (101,1,2000), (102,1,3000), (103,1,2500), (104,1,3500), (105,2,4000), (106,2,5000), (107,3,1500), (108,3,2500), (109,3,2000), (110,4,3000).
Write an SQL query to find destinations that have more than 2 hotels and the average nightly rate of hotels in each such destination. Display destination name and average nightly rate. Use JOIN, GROUP BY, HAVING, COUNT() and AVG().
Expected output: Goa 2750.00; Jaipur 2000.00.

Topics: SQL  
📎 source: [msg 4969](../archive/inter-iit/2026-10.jsonl)

## 2026-09-24 · IIT (ISM) Dhanbad · FTE

### Q1. Basic SQL query with GROUP BY / ORDER BY

A very basic SQL question based on GROUP BY, ORDER BY, etc.

Topics: SQL  
📎 source: [msg 1096](../archive/inter-iit/2026-09.jsonl), [msg 1098](../archive/inter-iit/2026-09.jsonl)

### Q2. Reduce number to a single digit by repeated digit sums

Given a number, repeatedly replace it with the sum of its digits until it becomes a single digit. Return the final single digit. A brute-force approach works. Only Python and C# were allowed.

Topics: Math, Strings  
📎 source: [msg 1096](../archive/inter-iit/2026-09.jsonl), [msg 1098](../archive/inter-iit/2026-09.jsonl)

### Q3. Web task: new/confirm password interface

A web-based question: make some small changes to a new password / confirm password interface (similar examples can be found on YouTube).

Topics: Other  
📎 source: [msg 1096](../archive/inter-iit/2026-09.jsonl), [msg 1098](../archive/inter-iit/2026-09.jsonl)

## 2026-09-22 · IIT Dhanbad · FTE

### Q1. Basic SQL with GROUP BY / ORDER BY

A very basic SQL query question based on GROUP BY, ORDER BY, etc. (exact schema not recalled).

Topics: SQL  
📎 source: [msg 896](../archive/inter-iit/2026-09.jsonl)

### Q2. Reduce number to single digit by summing digits

Given a number, repeatedly replace it with the sum of its digits until it becomes a single digit, and return that digit. A basic brute-force approach works; only Python and C# were allowed.

Topics: Math, Strings  
📎 source: [msg 896](../archive/inter-iit/2026-09.jsonl)

### Q3. Web task: new/confirm password interface

Web-based coding question: make some small changes to a new password / confirm password interface (e.g. validation that the two fields match). Similar examples can be found on YouTube.

Topics: Other  
📎 source: [msg 896](../archive/inter-iit/2026-09.jsonl)
