"""Tree DFS: bottom-up return values, top-down parameters, and a separate best-so-far."""
from __future__ import annotations
import math


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    if not root:
        return 0                                             # base case
    return 1 + max(max_depth(root.left), max_depth(root.right))  # combine children


def is_valid_bst(root: TreeNode | None, lo: float = -math.inf, hi: float = math.inf) -> bool:
    """Top-down: pass the allowed range to each child."""
    if not root:
        return True
    if not lo < root.val < hi:
        return False
    return is_valid_bst(root.left, lo, root.val) and is_valid_bst(root.right, root.val, hi)


def diameter(root: TreeNode | None) -> int:
    """Return height upward, but track the answer (longest path in edges) on the side."""
    best = 0

    def height(node: TreeNode | None) -> int:
        nonlocal best
        if not node:
            return 0
        left, right = height(node.left), height(node.right)
        best = max(best, left + right)    # path through this node
        return 1 + max(left, right)

    height(root)
    return best
