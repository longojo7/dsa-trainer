---
title: Intervals
category: Arrays & Strings
order: 5
summary: Sort by start (or end), then sweep once, merging or counting overlaps.
signals:
  - Input is a list of [start, end] pairs
  - Merge, insert, or remove overlapping ranges
  - Meeting rooms / minimum resources needed at once
  - Scheduling the maximum number of non-overlapping events
complexity:
  time: O(n log n) for the sort
  space: O(n) for the output
problems:
  - { name: Merge Intervals, id: 56, slug: merge-intervals, difficulty: Medium }
  - { name: Insert Interval, id: 57, slug: insert-interval, difficulty: Medium }
  - { name: Non-overlapping Intervals, id: 435, slug: non-overlapping-intervals, difficulty: Medium }
  - { name: Minimum Number of Arrows to Burst Balloons, id: 452, slug: minimum-number-of-arrows-to-burst-balloons, difficulty: Medium }
  - { name: Meeting Rooms II, id: 253, slug: meeting-rooms-ii, difficulty: Medium, premium: true }
---
## Key idea

After sorting by start, two intervals `a` then `b` overlap exactly when `b.start <= a.end`. One
pass then handles everything.

- **Merging** → sort by start; extend the last merged interval or start a new one.
- **Max non-overlapping (greedy)** → sort by **end**; always keep the interval that finishes first.
- **How many at once** (meeting rooms) → a min-heap of end times, or sweep sorted starts and ends separately.

## Pitfalls

- Ask whether touching intervals (`[1,2]` and `[2,3]`) count as overlapping — it changes `<` vs `<=`.
- When merging, take `max(last.end, cur.end)` — the current interval may be fully inside the last one.
- Sorting by start for the greedy "keep the most" problem gives wrong answers; sort by end.
