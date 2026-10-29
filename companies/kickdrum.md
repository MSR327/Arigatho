# Kickdrum

**12 questions** from 6 OA drives · seen at IIT Dhanbad, IIT Patna, NIT Rourkela, NIT Silchar, Unknown · latest 2026-10-23

**Topics:** [Arrays](../topics/arrays.md) (6) · [Stack/Queue](../topics/stack-queue.md) (3) · [Two Pointers](../topics/two-pointers.md) (2) · [Hashing](../topics/hashing.md) (2) · [OA Format](../topics/oa-format.md) (2) · [Linked List](../topics/linked-list.md) (1) · [Software Engineering](../topics/software-engineering.md) (1) · [Web Dev](../topics/web-dev.md) (1) · [Strings](../topics/strings.md) (1)

**LeetCode matches:** 3 (see the [practice list](../practice.md))

**Drives:**

- [2026-10-23 · NIT Rourkela · FTE · Interview](#2026-10-23--nit-rourkela--fte--interview) · 1 question
- [2026-10-21 · NIT Silchar · FTE](#2026-10-21--nit-silchar--fte) · 1 question
- [2026-10-12 · IIT Dhanbad · FTE](#2026-10-12--iit-dhanbad--fte) · 3 questions
- [2026-10-05 · IIT Dhanbad · FTE](#2026-10-05--iit-dhanbad--fte) · 2 questions
- [2026-09-30 · IIT Patna · FTE](#2026-09-30--iit-patna--fte) · 3 questions
- [2026-09-29 · Unknown · FTE](#2026-09-29--unknown--fte) · 2 questions

[← all companies](../README.md#companies)

---

## 2026-10-23 · NIT Rourkela · FTE · Interview

### Q1. Project folder walkthrough and feature implementation

The interviewer gives a complete project folder. You go through every file and the README and explain the project. They ask questions on it, such as which APIs are used and which databases are there. Then they ask you to implement a new feature in the project. AI use is allowed only in a very limited way. All questions come from the project folder they showed.

<sub>Topics: Software Engineering, Web Dev · Source: [chat, 23 Oct](../archive/kickdrum-oa/2026-10.jsonl#L21)</sub>

## 2026-10-21 · NIT Silchar · FTE

### Q1. Guess the Word: longest odd-length word

Kochouseph Chittilappilly went to Dhruv Zplanet, a gaming space, with his friends and played a game called "Guess the Word".

Rules of the game: the computer displays some strings on the screen and the player should pick one string / word; if this word matches the random word that the computer picks then the player is declared the winner.

Kochouseph Chittilappilly's friends played the game and no one won. It is now his turn to play and he decided to must win the game.

What he observed from his friends' games is that the computer picks the string whose length is odd and which should also be maximum. Due to system failure, the computer sometimes cannot generate odd length words. In such cases you will lose the game anyway and it displays "Better luck next time". He needs your help.

Sample input 0:

```
5
Hello Good morning Welcome you
```

Sample output 0:

```
morning
```

Explanation: Hello → 5, Good → 4, Morning → 7, Welcome → 7, You → 3. The first word picked by the computer is morning.

Sample input 1:

```
3
Go to hell
```

Sample output 1:

```
Better luck next time
```

Explanation: Here no word has odd length, so the computer gives "Better luck next time".

Note: the first line is the number of strings.

<sub>Topics: Strings, Arrays · Source: [chat, 21 Oct](../archive/intern-2027/2026-10.jsonl#L89)</sub>

## 2026-10-12 · IIT Dhanbad · FTE

### Q1. Codeforces 1771B-like coding question

One coding question similar to Codeforces contest 1771 problem B (https://codeforces.com/contest/1771/problem/B). The exact statement was not shared.

<sub>Topics: Arrays, Two Pointers · Source: [chat, 12 Oct](../archive/kickdrum-oa/2026-10.jsonl#L9)</sub>

### Q2. Browser history design question

One coding question similar to LeetCode Design Browser History. The exact statement was not shared.

<sub>Topics: Stack/Queue · Similar: [LeetCode 1472. Design Browser History](https://leetcode.com/problems/design-browser-history/) (Medium) · Source: [chat, 12 Oct](../archive/kickdrum-oa/2026-10.jsonl#L9)</sub>

### Q3. OA format and MCQ topics

20 MCQs and 2 coding questions. MCQs were based on Python, SQL, OOPs and ACID properties.

<sub>Topics: OA Format · Source: [chat, 12 Oct](../archive/kickdrum-oa/2026-10.jsonl#L9)</sub>

## 2026-10-05 · IIT Dhanbad · FTE

### Q1. Count cut-ahead adventurers

Function `countCutAheadAdventurers(n, entryOrder, chamberOrder)` returns an integer. The poster shared only a C++ solution, not the statement. From the code: `entryOrder` gives the order in which adventurers entered, `chamberOrder` gives the order in which they reached the chamber, and the answer counts adventurers who cut ahead (those who appear later in entry order than someone who comes after them in chamber order, found by scanning chamberOrder from the end while tracking the minimum entry position).

```cpp
class Solution {
public:
    int countCutAheadAdventurers(int n, const vector<int>& entryOrder, const vector<int>& chamberOrder) {
        if (n <= 1) return 0;
        int maxId = n;
        for (int x : entryOrder) if (x > maxId) maxId = x;
        vector<int> pos(maxId + 1);
        for (int i = 0; i < n; ++i) pos[entryOrder[i]] = i;
        int ans = 0;
        int minPos = n + 1;
        for (int i = n - 1; i >= 0; --i) {
            int p = pos[chamberOrder[i]];
            if (p > minPos) ans++;
            else minPos = p;
        }
        return ans;
    }
};
```

The original problem statement is missing.

<sub>Topics: Arrays, Hashing · Source: [chat, 5 Oct](../archive/kickdrum-oa/2026-10.jsonl#L3)</sub>

### Q2. Manage recipe experiments (undo/redo history)

Function `manage_recipe_experiments(operations)` takes a list of string operations and returns a list of strings. The poster shared only a C++ solution, not the statement. From the code: history starts with "Basic". Operations:
- `COOK recipe`: discard any redo history beyond the current position and add the recipe as the new current state.
- `UNDO k`: move back k steps (not below the start) and output the current recipe.
- `REDO k`: move forward k steps (not past the latest) and output the current recipe.
- `ACTIVE`: output the current recipe.

```cpp
vector<string> manage_recipe_experiments(vector<string> operations) {
    vector<string> history; history.push_back("Basic");
    int cur = 0; vector<string> ans;
    for (const string& op : operations) {
        if (op.empty()) continue;
        stringstream ss(op); string cmd;
        if (!(ss >> cmd)) continue;
        if (cmd == "COOK") { string recipe; ss >> recipe; history.resize(cur + 1); history.push_back(recipe); cur++; }
        else if (cmd == "UNDO") { long long k; ss >> k; cur = max(0LL, (long long)cur - k); ans.push_back(history[cur]); }
        else if (cmd == "REDO") { long long k; ss >> k; cur = min((long long)history.size() - 1, (long long)cur + k); ans.push_back(history[cur]); }
        else if (cmd == "ACTIVE") ans.push_back(history[cur]);
    }
    return ans;
}
```

<sub>Topics: Stack/Queue, Arrays · Similar: [LeetCode 1472. Design Browser History](https://leetcode.com/problems/design-browser-history/) (Medium) · Source: [chat, 5 Oct](../archive/kickdrum-oa/2026-10.jsonl#L3)</sub>

## 2026-09-30 · IIT Patna · FTE

### Q1. Hashing coding question (40 marks)

Coding question on hashing, easy level, worth 40 marks. The exact problem statement was not shared.

<sub>Topics: Hashing · Source: [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L7), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L9), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L10), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L11)</sub>

### Q2. Linked list coding question (60 marks)

Coding question on linked lists, medium to hard level, worth 60 marks. The linked list had to be implemented from scratch. The exact problem statement was not shared.

<sub>Topics: Linked List · Source: [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L7), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L9), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L10), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L11)</sub>

### Q3. OA format and MCQ topics

Two coding questions in 90 minutes and 20 MCQs in 30 minutes. MCQ topics: LLM tokens, transactions, SQL, OOPs.

<sub>Topics: OA Format · Source: [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L7), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L9), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L10), [chat, 30 Sep](../archive/kickdrum-oa/2026-09.jsonl#L11)</sub>

## 2026-09-29 · Unknown · FTE

### Q1. Hossam and Friends (Codeforces)

Hossam and Friends (Codeforces 1771B): there are n people and m pairs who are not friends; count the subsegments [a, b] of people in which every pair of people are friends.

<sub>Topics: Two Pointers, Arrays · Source: [chat, 29 Sep](../archive/inter-nit/2026-09.jsonl#L127)</sub>

### Q2. Variation of Browser History

A variation of the Design Browser History problem: support visit(url), back(steps) and forward(steps) operations on a browser's history.

<sub>Topics: Stack/Queue, Arrays · Similar: [LeetCode 1472. Design Browser History](https://leetcode.com/problems/design-browser-history/) (Medium) · Source: [chat, 29 Sep](../archive/inter-nit/2026-09.jsonl#L127)</sub>
