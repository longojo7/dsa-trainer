---
title: Prefix Sum
category: Arrays & Strings
order: 3
summary: Precompute running totals so any range sum is one subtraction.
signals:
  - Many range-sum queries on a static array
  - Count subarrays whose sum equals K (especially with negative numbers)
  - Equal number of 0s and 1s, or a sum divisible by K
  - Product of array except self (prefix/suffix products)
complexity:
  time: O(n) to build, O(1) per query
  space: O(n) — or O(number of distinct sums) for the hash-map variant
problems:
  - { name: Range Sum Query - Immutable, id: 303, slug: range-sum-query-immutable, difficulty: Easy }
  - { name: Subarray Sum Equals K, id: 560, slug: subarray-sum-equals-k, difficulty: Medium }
  - { name: Product of Array Except Self, id: 238, slug: product-of-array-except-self, difficulty: Medium }
  - { name: Continuous Subarray Sum, id: 523, slug: continuous-subarray-sum, difficulty: Medium }
  - { name: Contiguous Array, id: 525, slug: contiguous-array, difficulty: Medium }
---
## Key idea

`prefix[i]` = sum of the first `i` elements, so `sum(nums[i:j]) == prefix[j] - prefix[i]`.

The interview-favorite twist: **"how many subarrays sum to k?"** A subarray ending here sums to
`k` exactly when some *earlier* prefix equals `running - k`. Keep a hash map of how many times each
prefix sum has appeared, and look it up as you go.

## Pitfalls

- Forget to seed the map with `{0: 1}` → you miss subarrays that start at index 0.
- Off-by-one: make `prefix` length `n + 1` with `prefix[0] = 0`.
- If all numbers are positive and you want *longest/shortest*, a sliding window is often simpler.
