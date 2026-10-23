---
title: Union-Find (Disjoint Set)
category: Graphs
order: 3
summary: Merge groups and ask "are these connected?" in nearly O(1) per operation.
signals:
  - Connected components when edges arrive one at a time
  - Detect the edge that creates a cycle in an undirected graph
  - Group items that are linked by equivalence (accounts with a shared email)
  - Number of provinces / friend circles
complexity:
  time: O(α(n)) per operation (effectively constant) with path compression + union by size
  space: O(n)
problems:
  - { name: Number of Provinces, id: 547, slug: number-of-provinces, difficulty: Medium }
  - { name: Redundant Connection, id: 684, slug: redundant-connection, difficulty: Medium }
  - { name: Accounts Merge, id: 721, slug: accounts-merge, difficulty: Medium }
  - { name: Number of Connected Components in an Undirected Graph, id: 323, slug: number-of-connected-components-in-an-undirected-graph, difficulty: Medium, premium: true }
  - { name: Graph Valid Tree, id: 261, slug: graph-valid-tree, difficulty: Medium, premium: true }
---
## Key idea

Every element points to a parent. Following parents leads to the group's **root**, which
identifies the group. `union(a, b)` attaches one root to the other, and `find(a) == find(b)` tells
you whether two elements are in the same group.

The two optimizations that make it fast are worth naming in an interview:

- **Path compression** — while finding the root, point nodes directly at it.
- **Union by size/rank** — attach the smaller tree under the bigger one.

## Pitfalls

- Comparing `parent[a] == parent[b]` instead of `find(a) == find(b)`.
- If `union` finds that both are already in the same group, that edge closes a **cycle** — that's the answer to Redundant Connection.
- DFS/BFS also counts components; union-find shines when edges are added *dynamically*.
