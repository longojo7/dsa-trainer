---
title: Fast & Slow Pointers
category: Linked Lists
order: 1
summary: Move one pointer twice as fast as the other to find cycles and midpoints.
signals:
  - Detect a cycle in a linked list (or in a sequence like f(x) → f(f(x)))
  - Find the middle of a linked list in one pass
  - Find where a cycle begins
  - O(1) extra space required on a linked list
complexity:
  time: O(n)
  space: O(1)
problems:
  - { name: Linked List Cycle, id: 141, slug: linked-list-cycle, difficulty: Easy }
  - { name: Middle of the Linked List, id: 876, slug: middle-of-the-linked-list, difficulty: Easy }
  - { name: Happy Number, id: 202, slug: happy-number, difficulty: Easy }
  - { name: Linked List Cycle II, id: 142, slug: linked-list-cycle-ii, difficulty: Medium }
  - { name: Find the Duplicate Number, id: 287, slug: find-the-duplicate-number, difficulty: Medium }
---
## Key idea

Slow moves 1 step, fast moves 2. If there's a cycle, fast laps slow and they meet. If there isn't,
fast hits the end. When fast reaches the end, slow is at the **middle**.

**Cycle start (Floyd's algorithm):** after they meet, reset one pointer to the head and move both
one step at a time. Where they meet again is the start of the cycle.

## Pitfalls

- Check `fast and fast.next` before stepping twice — otherwise you crash on `None.next`.
- For even-length lists, decide which "middle" you want; `while fast and fast.next` gives the second one.
- A visited `set` also works, but it's O(n) space — the interviewer usually wants O(1).
