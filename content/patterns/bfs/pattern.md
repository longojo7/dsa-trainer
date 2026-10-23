---
title: BFS (Level Order & Shortest Path)
category: Trees
order: 2
summary: Explore with a queue one layer at a time — gives level order and unweighted shortest paths.
signals:
  - Level-by-level tree output, right side view, or zigzag
  - Shortest path / minimum steps in an unweighted graph or grid
  - Spreading from multiple sources at once (rotting oranges, walls and gates)
  - Minimum number of transformations (word ladder)
complexity:
  time: O(V + E) — O(rows × cols) on a grid
  space: O(V) for the queue and visited set
problems:
  - { name: Binary Tree Level Order Traversal, id: 102, slug: binary-tree-level-order-traversal, difficulty: Medium }
  - { name: Binary Tree Right Side View, id: 199, slug: binary-tree-right-side-view, difficulty: Medium }
  - { name: Rotting Oranges, id: 994, slug: rotting-oranges, difficulty: Medium }
  - { name: Shortest Path in Binary Matrix, id: 1091, slug: shortest-path-in-binary-matrix, difficulty: Medium }
  - { name: Word Ladder, id: 127, slug: word-ladder, difficulty: Hard }
---
## Key idea

A queue processes nodes in the order they were discovered, so everything at distance `d` is handled
before anything at distance `d + 1`. That's why **the first time BFS reaches a node is via a shortest path**
(when every edge costs the same).

To work level by level, process `len(queue)` items in an inner loop — those are exactly the current level.

**Multi-source BFS:** put *all* starting points in the queue before you begin.

## Pitfalls

- Mark a node visited **when you enqueue it**, not when you dequeue it — otherwise it gets added many times.
- Use `collections.deque` and `popleft()`; `list.pop(0)` is O(n).
- Weighted edges → BFS is wrong; use Dijkstra.
