---
title: Backtracking
category: Recursion
order: 1
summary: Build candidates one choice at a time; undo the choice and try the next.
signals:
  - Generate ALL subsets, permutations, or combinations
  - Constraints are small (n ≤ ~20) — exponential time is acceptable
  - Place items under rules (N-Queens, Sudoku)
  - Search for a word or path in a grid
complexity:
  time: Exponential — O(2ⁿ) subsets, O(n!) permutations (times the cost to copy each answer)
  space: O(n) recursion depth, plus the output
problems:
  - { name: Subsets, id: 78, slug: subsets, difficulty: Medium }
  - { name: Permutations, id: 46, slug: permutations, difficulty: Medium }
  - { name: Combination Sum, id: 39, slug: combination-sum, difficulty: Medium }
  - { name: Word Search, id: 79, slug: word-search, difficulty: Medium }
  - { name: N-Queens, id: 51, slug: n-queens, difficulty: Hard }
---
## Key idea

Every backtracking solution is the same three lines inside a loop:

1. **Choose** — append a candidate to `path`.
2. **Explore** — recurse.
3. **Un-choose** — `path.pop()`.

What changes between problems is **what the choices are** at each step and **when `path` is a
complete answer**. Sketch the decision tree for a tiny input before coding.

- **Subsets / combinations** → pass a `start` index so you only look forward (no duplicates in a different order).
- **Permutations** → any unused element can come next; track `used`.

**Prune** early: stop exploring a branch the moment it can't lead to a valid answer.

## Pitfalls

- Appending `path` instead of `path[:]` — every saved answer ends up as the same (empty) list.
- With duplicates in the input: sort first, then skip `nums[i] == nums[i - 1]` at the same depth.
- Forgetting to undo state (the `pop()`, or un-marking a grid cell).
