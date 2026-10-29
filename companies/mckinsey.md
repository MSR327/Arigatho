# McKinsey

**1 question** · 1 drive · latest 28 Oct 2026 · [← all companies](../README.md#companies)

**Asks about:** [Heaps](../topics/heaps.md) 1 · [Greedy](../topics/greedy.md) 1 · [Hashing](../topics/hashing.md) 1  
**Seen at:** IIT Roorkee

<details>
<summary><b>Contents</b>: every drive and question, newest first</summary>

- [2026-10-28 · IIT Roorkee · FTE · Data Science](#2026-10-28--iit-roorkee--fte--data-science)
  - [Reorder songs so same artist is not consecutive](#q1-reorder-songs-so-same-artist-is-not-consecutive)

</details>

---

## 2026-10-28 · IIT Roorkee · FTE · Data Science

### Q1. Reorder songs so same artist is not consecutive

You are given a 2D array `songs`, where each row contains a song name and its artist:

`songs[i] = [songName, artistName]`

Reorder the songs according to the following rules:

1. At each step, choose an artist who has the maximum number of unplayed songs remaining.
2. The same artist cannot appear in two consecutive positions in the reordered array.
3. If multiple artists have the same maximum number of unplayed songs, choose the artist who has the greater total number of songs in the original array.
4. After selecting an artist, choose one of their unplayed songs and append it to the result. Update the remaining counts and repeat until all songs have been played.

Example:

```
songs = [
    ["Song1", "A"],
    ["Song2", "B"],
    ["Song3", "A"],
    ["Song4", "C"],
    ["Song5", "B"],
    ["Song6", "A"],
    ["Song7", "C"],
    ["Song8", "B"]
]
```

Artist counts: A = 3, B = 3, C = 2.

One possible output:

```
[
    ["Song1", "A"],
    ["Song2", "B"],
    ["Song3", "A"],
    ["Song4", "C"],
    ["Song5", "B"],
    ["Song6", "A"],
    ["Song7", "C"],
    ["Song8", "B"]
]
```

The rule for choosing a song among multiple songs by the same artist was not specified; assume original relative order is preserved. Suggested approach: max heap on remaining counts, excluding the previously chosen artist and breaking ties by original total count.

<sub>Topics: Heaps, Greedy, Hashing · Source: [chat, 28 Oct](../archive/inter-iit/2026-10.jsonl#L1169)</sub>
