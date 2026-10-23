---
title: Heap / Top-K
category: Heaps
order: 1
summary: A heap gives the smallest (or largest) item in O(log n) — ideal for "k best" and streaming problems.
signals:
  - K largest / K smallest / K most frequent / K closest
  - Merge K sorted lists or arrays
  - Running median of a data stream
  - Repeatedly take the best remaining option (scheduling, greedy)
complexity:
  time: O(n log k) for top-k with a heap of size k
  space: O(k)
problems:
  - { name: Kth Largest Element in an Array, id: 215, slug: kth-largest-element-in-an-array, difficulty: Medium }
  - { name: Top K Frequent Elements, id: 347, slug: top-k-frequent-elements, difficulty: Medium }
  - { name: K Closest Points to Origin, id: 973, slug: k-closest-points-to-origin, difficulty: Medium }
  - { name: Merge k Sorted Lists, id: 23, slug: merge-k-sorted-lists, difficulty: Hard }
  - { name: Find Median from Data Stream, id: 295, slug: find-median-from-data-stream, difficulty: Hard }
---
## Key idea

To keep the **k largest**, use a **min-heap of size k**: the smallest of your top-k sits on top, and
any new item bigger than it kicks it out. That's O(n log k) instead of sorting in O(n log n).

**Running median:** keep two heaps — a max-heap for the lower half and a min-heap for the upper half —
balanced so their sizes differ by at most one.

## Pitfalls

- Python's `heapq` is a **min-heap only**. For a max-heap, push negated values.
- Push tuples `(priority, tiebreaker, item)` so the heap never has to compare items that can't be compared (like `ListNode`).
- `heapq.nlargest(k, nums)` is fine in an interview, but be ready to explain how it works.
