---
title: In-place Linked List Reversal
category: Linked Lists
order: 2
summary: Re-point next pointers one node at a time with prev / curr / next.
signals:
  - Reverse all or part of a linked list
  - Reorder or check a list from both ends (palindrome, reorder list)
  - O(1) extra space on a linked list
  - Reverse in groups of k
complexity:
  time: O(n)
  space: O(1)
problems:
  - { name: Reverse Linked List, id: 206, slug: reverse-linked-list, difficulty: Easy }
  - { name: Palindrome Linked List, id: 234, slug: palindrome-linked-list, difficulty: Easy }
  - { name: Reverse Linked List II, id: 92, slug: reverse-linked-list-ii, difficulty: Medium }
  - { name: Reorder List, id: 143, slug: reorder-list, difficulty: Medium }
  - { name: Reverse Nodes in k-Group, id: 25, slug: reverse-nodes-in-k-group, difficulty: Hard }
---
## Key idea

Three pointers: `prev` (the already-reversed part), `curr` (the node you're flipping), and the saved
`nxt` (so you don't lose the rest of the list). Each step: save `nxt`, point `curr.next` back at
`prev`, then advance both.

Many "hard" list problems are just **find the middle (fast/slow) → reverse the second half → walk
both halves together**.

## Pitfalls

- Save `curr.next` *before* overwriting it.
- Use a **dummy head** node when the head itself might change (reversing a sublist starting at position 1).
- Draw the pointers on paper — interviewers expect you to, and it prevents off-by-one bugs.
