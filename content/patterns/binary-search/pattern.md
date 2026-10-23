---
title: Binary Search
category: Searching
order: 1
summary: Halve the search space each step — on a sorted array, or on the answer itself.
signals:
  - Sorted (or rotated sorted) input
  - Required time is O(log n)
  - '"Find the minimum X such that it''s feasible" (binary search on the answer)'
  - A yes/no condition that flips exactly once (False False ... True True)
complexity:
  time: O(log n) — or O(n log(range)) when searching on the answer
  space: O(1)
problems:
  - { name: Binary Search, id: 704, slug: binary-search, difficulty: Easy }
  - { name: Search in Rotated Sorted Array, id: 33, slug: search-in-rotated-sorted-array, difficulty: Medium }
  - { name: Find Minimum in Rotated Sorted Array, id: 153, slug: find-minimum-in-rotated-sorted-array, difficulty: Medium }
  - { name: Koko Eating Bananas, id: 875, slug: koko-eating-bananas, difficulty: Medium }
  - { name: Median of Two Sorted Arrays, id: 4, slug: median-of-two-sorted-arrays, difficulty: Hard }
---
## Key idea

Don't memorize five binary search variants — memorize **one**: *find the first index where a
condition becomes true*. If `condition(mid)` is true, the answer is `mid` or to its left
(`hi = mid`); otherwise it's to the right (`lo = mid + 1`). When `lo == hi`, you're done.

**Binary search on the answer:** when you can't search the input but you *can* check "is speed `k`
fast enough?", search over the possible values of `k`. Koko Eating Bananas is the classic example.

## Pitfalls

- Infinite loops from `lo = mid` — with the template below, always use `lo = mid + 1`.
- Decide whether `hi` starts at `n - 1` or `n` (`n` if the answer might be "nowhere").
- Python ints don't overflow, but mention `lo + (hi - lo) // 2` — interviewers in other languages expect it.
