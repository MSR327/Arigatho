# Stripe

**5 questions** · 5 drives · latest 23 Nov 2026 · [1 practice problem](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [OA Format](../topics/oa-format.md) 3 · [Sorting](../topics/sorting.md) 1 · [Binary Search](../topics/binary-search.md) 1 · [Arrays](../topics/arrays.md) 1 · [Hashing](../topics/hashing.md) 1  
**Seen at:** BITS Pilani, IIT BHU, IIT Hyderabad, IIT Roorkee

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-23 · IIT Roorkee · FTE](#2026-11-23--iit-roorkee--fte)
  - [Merchant fraud score from transactions and rules](#q1-merchant-fraud-score-from-transactions-and-rules)
- [2026-11-21 · Unknown · FTE · SDE · Other round](#2026-11-21--unknown--fte--sde--other-round)
  - [Stripe SDE OA and interview pattern](#q1-stripe-sde-oa-and-interview-pattern)
- [2026-10-26 · IIT BHU · FTE · Interview](#2026-10-26--iit-bhu--fte--interview)
  - [Stripe virtual onsite structure](#q1-stripe-virtual-onsite-structure)
- [2026-10-25 · IIT Hyderabad · FTE · Interview](#2026-10-25--iit-hyderabad--fte--interview)
  - [Stripe virtual onsite rounds](#q1-stripe-virtual-onsite-rounds)
- [2026-10-13 · BITS Pilani · FTE · Interview](#2026-10-13--bits-pilani--fte--interview)
  - [CSES sorting and searching problem](#q1-cses-sorting-and-searching-problem)

</details>

---

## 2026-11-23 · IIT Roorkee · FTE

### Q1. Merchant fraud score from transactions and rules

The fraud detection team at Stripe aims to reduce merchant fraud risk with minimal pain to good merchants through machine learning. You are to develop a system to assess the fraud risk associated with transactions made to various merchants.

You are given `transactions_list` (transactions for a certain day), `merchants_list` (list of merchants) and `rules_list` (a rule corresponding to each transaction). A transaction is a payment by a customer to a merchant. Each merchant has a `base_score`. Assign each merchant a fraud score:

Initialize a merchant's `current_score` as their `base_score`. For each transaction, update the merchant's `current_score`, in separate passes over the entire list for each step:

1. If the transaction amount is greater than the corresponding rule's `min_transaction_amount`, multiply `current_score` by the rule's `multiplicative_factor`.
2. If the same `customer_id` has made three or more transactions to that `merchant_id` (including the current one), add all the corresponding rules' `additive_factor`s to `current_score`, cumulatively (e.g. if the score at the third transaction is X, including the first, second and third additive factors, the fourth transaction gives X + the fourth transaction's additive_factor).
3. If a transaction is the third or more from the same `customer_id` in the same hour for the same `merchant_id` (including the current one):
   - If the hour is between 12 and 17 (inclusive): add the penalty each time (this includes the first and second transaction as well as all after the third).
   - If the hour is between 9 and 11, or 18 and 21 (inclusive): subtract the penalty each time (this includes the first and second transaction as well as all after the third).
   - Otherwise do nothing.

Input (no integer overflows):
- `transactions_list`: length n (1 ≤ n ≤ 1000), each a comma-separated string: `merchant_id` (string, length > 0), `amount` (integer), `customer_id` (string, length > 0), `hour` (integer, 0 ≤ hour ≤ 23).
- `rules_list`: length n (1 ≤ n ≤ 1000), each a comma-separated string corresponding to each transaction: `min_transaction_amount` (integer, minimum amount to consider fraudulent), `multiplicative_factor` (integer), ...

The message is cut off here: the remaining rule fields (additive_factor, penalty), merchants_list format, output format and examples are missing.

<sub>Topics: Arrays, Hashing · Source: [chat, 23 Nov](../archive/campus-iit-madras-placements/2026-11.jsonl#L304), [chat, 23 Nov](../archive/campus-iit-madras-placements/2026-11.jsonl#L305)</sub>

## 2026-11-21 · Unknown · FTE · SDE · Other round

### Q1. Stripe SDE OA and interview pattern

- OA: one DSA question; 17/19 test cases passed was enough to get the interview call (from 1 shared experience)
- Interviews: DSA, often multi-part, plus string parsing (from 3 shared experiences)
- Questions reported are mostly simulation, sorting, string

<sub>Topics: OA Format · Source: [chat, 21 Nov](../archive/inter-nit/2026-11.jsonl#L2261), [chat, 21 Nov](../archive/inter-nit/2026-11.jsonl#L2271)</sub>

## 2026-10-26 · IIT BHU · FTE · Interview

### Q1. Stripe virtual onsite structure

3 stages, each eliminative.

First round (1 hour): 5 questions, revealed one by one as solved, with progressive difficulty. The first two were easy-to-medium. Not expected to solve every question or write an optimized solution; working code was fine. Result came after 3-4 days.

Second round: two rounds of 45 minutes each, with a 30 minute break in between. The first was an API integration round in the same 5-question style, built around a codebase where some JSON data and an API were given. Poster solved 4/5.

The third stage and the second 45-minute round are not described.

<sub>Topics: OA Format · Source: [chat, 26 Oct](../archive/intern-2028/2026-10.jsonl#L90) · Also asked at: IIT BHU (2026-11-12)</sub>

## 2026-10-25 · IIT Hyderabad · FTE · Interview

### Q1. Stripe virtual onsite rounds

The first round was DSA, and the second round was a deep system design round. No specific questions were shared.

<sub>Topics: OA Format · Source: [chat, 25 Oct](../archive/intern-2028/2026-10.jsonl#L71)</sub>

## 2026-10-13 · BITS Pilani · FTE · Interview

### Q1. CSES sorting and searching problem

A friend of the poster was asked a CSES problem from the Sorting and Searching section in the Stripe interview. The exact problem was not specified.

<sub>Topics: Sorting, Binary Search · Same idea: [CSES: Sum of Two Values](https://cses.fi/problemset/task/1640), sorting and searching section problem · Source: [chat, 13 Oct](../archive/intern-2028/2026-10.jsonl#L235)</sub>
