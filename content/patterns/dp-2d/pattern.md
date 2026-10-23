---
title: 2-D Dynamic Programming
category: Dynamic Programming
order: 2
summary: State needs two indices — two strings, a grid, or (item, capacity) for knapsack.
signals:
  - Compare two strings (LCS, edit distance, matching)
  - Count or optimize paths through a grid
  - Choose items under a capacity or target sum (0/1 knapsack, partition)
  - Substrings or intervals defined by (start, end)
complexity:
  time: O(n × m)
  space: O(n × m), often reducible to O(m) with a rolling row
problems:
  - { name: Unique Paths, id: 62, slug: unique-paths, difficulty: Medium }
  - { name: Longest Common Subsequence, id: 1143, slug: longest-common-subsequence, difficulty: Medium }
  - { name: Longest Palindromic Substring, id: 5, slug: longest-palindromic-substring, difficulty: Medium }
  - { name: Partition Equal Subset Sum, id: 416, slug: partition-equal-subset-sum, difficulty: Medium }
  - { name: Edit Distance, id: 72, slug: edit-distance, difficulty: Medium }
---
## Key idea

Same four questions as 1-D DP, but the state is `dp[i][j]`.

- **Two strings:** `dp[i][j]` = answer for the prefixes `a[:i]` and `b[:j]`. Look at the last characters: if they match, use `dp[i-1][j-1]`; otherwise combine `dp[i-1][j]` and `dp[i][j-1]`.
- **Grids:** `dp[r][c]` comes from the cell above and the cell to the left.
- **0/1 knapsack:** `dp[i][cap]` = best using the first `i` items with capacity `cap`. Each item is either skipped or taken once.

Draw the table for a tiny example. Seeing which neighbors each cell depends on tells you the loop order.

## Pitfalls

- Sizing the table `(n+1) × (m+1)` so row/column 0 represent the empty prefix — this removes many edge cases.
- In 1-D knapsack space optimization, iterate capacity **downward** so each item is used at most once.
- Mixing up subsequence (can skip characters) with substring (contiguous).
