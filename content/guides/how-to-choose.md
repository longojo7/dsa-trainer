---
title: How to Pick a Pattern
order: 1
summary: Read the constraints first — they tell you the target complexity before you've thought about the algorithm.
---
## 1. Let the constraints tell you the target complexity

Most interview judges allow roughly **10⁸ simple operations**. Work backwards from `n`:

| If n is up to… | You can afford | Usually means |
| --- | --- | --- |
| 10–12 | O(n!) | Permutations, brute-force backtracking |
| 20–25 | O(2ⁿ) | Subsets, bitmask DP |
| 100–500 | O(n³) | Triple loops, interval DP, Floyd–Warshall |
| 1,000–5,000 | O(n²) | 2-D DP, all pairs |
| 10⁵–10⁶ | O(n log n) or O(n) | Sorting, heap, two pointers, sliding window, hashing, prefix sums |
| 10⁹ or more | O(log n) or O(1) | Binary search (often on the answer), math |

## 2. Run through the questions

1. **Is the input sorted, or would sorting help?** → Two Pointers, Binary Search, Intervals
2. **Contiguous subarray or substring?** → Sliding Window (all positive) or Prefix Sum (negatives / exact counts)
3. **"Have I seen this?" or counting?** → Hash Map & Set
4. **"Next greater / smaller"?** → Monotonic Stack
5. **K best / smallest / most frequent, or a stream?** → Heap
6. **Tree?** → DFS for anything about subtrees and paths, BFS for levels
7. **Grid or graph?**
   - any path / count regions → Graph DFS
   - fewest steps, unweighted → BFS
   - weighted → Dijkstra
   - dependencies → Topological Sort
   - groups merging over time → Union-Find
8. **All combinations / permutations, small n?** → Backtracking
9. **Count ways, or min/max with overlapping choices?** → Dynamic Programming
10. **Many prefix lookups?** → Trie

## 3. Say this out loud in the interview

1. Restate the problem and confirm inputs, outputs, and edge cases (empty input, duplicates, negatives).
2. Describe the **brute force** and its complexity — even if it's slow.
3. Name what makes it slow ("we rescan the window each time"), then name the pattern that removes it.
4. Talk through an example by hand *before* writing code.
5. Code, then test with your example plus one edge case. State the final time and space complexity.
