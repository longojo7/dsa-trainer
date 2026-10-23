---
title: Tree DFS (Recursion)
category: Trees
order: 1
summary: Solve the problem for each subtree, then combine the left and right answers at the parent.
signals:
  - Binary tree height, depth, diameter, or path sums
  - Validate a BST, or anything comparing a node to its subtrees
  - Lowest common ancestor
  - '"For every node..." where the answer depends on its children'
complexity:
  time: O(n)
  space: O(h) recursion stack — O(log n) balanced, O(n) skewed
problems:
  - { name: Maximum Depth of Binary Tree, id: 104, slug: maximum-depth-of-binary-tree, difficulty: Easy }
  - { name: Invert Binary Tree, id: 226, slug: invert-binary-tree, difficulty: Easy }
  - { name: Diameter of Binary Tree, id: 543, slug: diameter-of-binary-tree, difficulty: Easy }
  - { name: Validate Binary Search Tree, id: 98, slug: validate-binary-search-tree, difficulty: Medium }
  - { name: Lowest Common Ancestor of a Binary Tree, id: 236, slug: lowest-common-ancestor-of-a-binary-tree, difficulty: Medium }
  - { name: Binary Tree Maximum Path Sum, id: 124, slug: binary-tree-maximum-path-sum, difficulty: Hard }
---
## Key idea

Ask yourself: **"If I already had the answer for my left and right subtrees, how would I compute
mine?"** That sentence *is* the recursion. Then handle the base case (`None`).

Two kinds of information flow:

- **Bottom-up (return values)** — height, diameter, "is balanced". The function returns something to its parent.
- **Top-down (parameters)** — valid BST bounds, the path sum so far. You pass information down to the children.

When the answer isn't what you return (diameter, max path sum), **return one thing and update a
separate best-so-far** variable.

## Pitfalls

- Validating a BST by only comparing a node with its direct children — you need min/max bounds from all ancestors.
- Python's default recursion limit (~1000) can be hit on a skewed tree. Mention an iterative stack as the fix.
- Confusing depth (from the root, goes down) with height (from the leaves, goes up).
