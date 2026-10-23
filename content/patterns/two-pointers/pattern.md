---
title: Two Pointers
category: Arrays & Strings
order: 1
summary: Walk two indices toward each other (or in the same direction) to avoid a nested loop.
signals:
  - Input array/string is sorted (or you can sort it)
  - Find a pair/triplet that sums to a target
  - Palindrome checks, or comparing from both ends
  - Remove duplicates / partition in place with O(1) extra space
complexity:
  time: O(n) — O(n log n) if you sort first
  space: O(1)
problems:
  - { name: Valid Palindrome, id: 125, slug: valid-palindrome, difficulty: Easy }
  - { name: Two Sum II - Input Array Is Sorted, id: 167, slug: two-sum-ii-input-array-is-sorted, difficulty: Medium }
  - { name: 3Sum, id: 15, slug: 3sum, difficulty: Medium }
  - { name: Container With Most Water, id: 11, slug: container-with-most-water, difficulty: Medium }
  - { name: Trapping Rain Water, id: 42, slug: trapping-rain-water, difficulty: Hard }
---
## Key idea

Every step should **eliminate a possibility you'd otherwise check with an inner loop**. On a sorted
array, if `nums[l] + nums[r]` is too small, nothing paired with `l` can work (everything to its
left of `r` is even smaller), so you move `l`. That reasoning is what makes it O(n), and it's what
interviewers want you to *say out loud*.

Two flavors:

- **Opposite ends** — `l = 0, r = n - 1`, move inward (pair sums, palindromes, container).
- **Same direction** — a slow "write" pointer and a fast "read" pointer (remove duplicates, move zeroes).

## Pitfalls

- Forgetting to skip duplicates in 3Sum → duplicate triplets in the output.
- Using `l <= r` when the two pointers must be distinct elements (use `l < r`).
- The array isn't sorted and sorting would destroy the indices you're asked to return — use a hash map instead.
