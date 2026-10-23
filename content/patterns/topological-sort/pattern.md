---
title: Topological Sort
category: Graphs
order: 2
summary: Order tasks so every prerequisite comes first — and detect impossible (cyclic) dependencies.
signals:
  - Prerequisites, dependencies, or "X must happen before Y"
  - Course schedule / build order / task ordering
  - Detect a cycle in a directed graph
  - Derive an ordering from sorted examples (alien dictionary)
complexity:
  time: O(V + E)
  space: O(V + E)
problems:
  - { name: Course Schedule, id: 207, slug: course-schedule, difficulty: Medium }
  - { name: Course Schedule II, id: 210, slug: course-schedule-ii, difficulty: Medium }
  - { name: Find Eventual Safe States, id: 802, slug: find-eventual-safe-states, difficulty: Medium }
  - { name: Minimum Height Trees, id: 310, slug: minimum-height-trees, difficulty: Medium }
  - { name: Alien Dictionary, id: 269, slug: alien-dictionary, difficulty: Hard, premium: true }
---
## Key idea

**Kahn's algorithm (BFS):** count each node's incoming edges (its *indegree*). Every node with
indegree 0 has no remaining prerequisites, so it can go next. When you take one, decrement its
neighbors' indegrees, and enqueue any that reach 0.

If you finish with fewer than `V` nodes in the order, the rest are stuck in a **cycle**, so no valid
order exists.

## Pitfalls

- Getting the edge direction backwards. `[a, b]` in Course Schedule means *b → a* (take b first).
- Topological sort only applies to **directed** graphs.
- There can be many valid orders; any one is usually accepted.
