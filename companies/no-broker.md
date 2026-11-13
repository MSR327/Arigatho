# No Broker

**1 question** · 1 drive · latest 12 Nov 2026 · [1 practice problem](../practice.md) · [← all companies](../README.md#companies)

**Asks about:** [Arrays](../topics/arrays.md) 1 · [Greedy](../topics/greedy.md) 1  
**Seen at:** IIT BHU

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-11-12 · IIT BHU · FTE · SDE](#2026-11-12--iit-bhu--fte--sde)
  - [Players who can still win the trophy](#q1-players-who-can-still-win-the-trophy)

</details>

---

## 2026-11-12 · IIT BHU · FTE · SDE

### Q1. Players who can still win the trophy

Given an array of size n (n up to 10^5) containing the scores of n people before the final race. In the final race, the person who comes first gets n points, second gets n-1, and so on, with the last getting 1 point (no ties). After the race, all players with the highest score get a trophy.

Find the number of players who still have a chance of winning the trophy.

Example:
```
n = 5, points = [12,14,14,15,15]
Output: 4
```
Player 1 cannot win even by finishing first: max 12+5 = 17, but the highest score would be at least 18.

<sub>Topics: Arrays, Greedy · Same idea: [LeetCode 1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) (Easy), add max bonus, compare against maximum of others · Source: [chat, 12 Nov](../archive/campus-iit-bhubaneswar-placements/2026-11.jsonl#L68)</sub>
