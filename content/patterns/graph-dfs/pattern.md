---
title: Graph DFS / Flood Fill
category: Graphs
order: 1
summary: Visit everything reachable from a node — count islands, connected components, regions.
signals:
  - Count islands / connected components / regions in a grid
  - Can I reach B from A? (any path, not the shortest)
  - Clone or copy a graph
  - Mark everything connected to the border (surrounded regions)
complexity:
  time: O(V + E) — O(rows × cols) on a grid
  space: O(V) for visited plus the recursion stack
problems:
  - { name: Number of Islands, id: 200, slug: number-of-islands, difficulty: Medium }
  - { name: Max Area of Island, id: 695, slug: max-area-of-island, difficulty: Medium }
  - { name: Clone Graph, id: 133, slug: clone-graph, difficulty: Medium }
  - { name: Pacific Atlantic Water Flow, id: 417, slug: pacific-atlantic-water-flow, difficulty: Medium }
  - { name: Surrounded Regions, id: 130, slug: surrounded-regions, difficulty: Medium }
---
## Key idea

Loop over every cell or node. When you find an unvisited one, that's a **new component** — run DFS
from it to mark everything connected, so it's never counted again.

On grids, the "edges" are the 4 neighbors. Treat the grid as a graph rather than building one.

**Reverse the question** when it's easier: "which cells can reach the ocean?" becomes "which cells
can the ocean reach going uphill?", with DFS starting from the border.

## Pitfalls

- Bounds checks before indexing (`0 <= r < rows`).
- Forgetting to mark visited → infinite recursion.
- Ask before mutating the input grid to mark visited — some interviewers mind.
- Build an adjacency list first when you're given an edge list: `graph = defaultdict(list)`.
