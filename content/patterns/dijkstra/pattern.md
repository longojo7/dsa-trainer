---
title: Dijkstra (Weighted Shortest Path)
category: Graphs
order: 4
summary: BFS with a min-heap — always expand the closest unfinished node next.
signals:
  - Shortest path or minimum cost with non-negative edge weights
  - Network delay / time for a signal to reach every node
  - Minimize the maximum effort along a path (a modified Dijkstra)
  - The graph is weighted, so plain BFS isn't enough
complexity:
  time: O((V + E) log V)
  space: O(V + E)
problems:
  - { name: Network Delay Time, id: 743, slug: network-delay-time, difficulty: Medium }
  - { name: Path With Minimum Effort, id: 1631, slug: path-with-minimum-effort, difficulty: Medium }
  - { name: Cheapest Flights Within K Stops, id: 787, slug: cheapest-flights-within-k-stops, difficulty: Medium }
  - { name: Swim in Rising Water, id: 778, slug: swim-in-rising-water, difficulty: Hard }
---
## Key idea

Keep a min-heap of `(distance, node)`. Pop the smallest: since all weights are non-negative, nothing
discovered later can make that distance shorter, so it's **final**. Then relax its edges — push any
neighbor whose distance improved.

The same skeleton solves "minimize the worst edge on the path": just change how the cost of a path is
combined (`max` instead of `+`).

## Pitfalls

- Negative edge weights break Dijkstra (use Bellman-Ford).
- Python's `heapq` has no decrease-key. Push duplicates and **skip stale entries** when you pop them.
- "Within K stops" adds a constraint Dijkstra doesn't track. Use Bellman-Ford limited to K + 1 rounds, or BFS by levels.
