---
title: Monotonic Stack
category: Stacks & Queues
order: 1
summary: Keep a stack in sorted order to find the next greater/smaller element in O(n).
signals:
  - '"Next greater element" / "next warmer day" / "previous smaller"'
  - For each element, how far until something bigger or smaller
  - Largest rectangle, or how far each bar extends
  - Sliding window maximum (monotonic deque)
complexity:
  time: O(n) — each index is pushed and popped at most once
  space: O(n)
problems:
  - { name: Next Greater Element I, id: 496, slug: next-greater-element-i, difficulty: Easy }
  - { name: Daily Temperatures, id: 739, slug: daily-temperatures, difficulty: Medium }
  - { name: Online Stock Span, id: 901, slug: online-stock-span, difficulty: Medium }
  - { name: Largest Rectangle in Histogram, id: 84, slug: largest-rectangle-in-histogram, difficulty: Hard }
  - { name: Sliding Window Maximum, id: 239, slug: sliding-window-maximum, difficulty: Hard }
---
## Key idea

The stack holds indices of elements **still waiting for their answer**. When a new element arrives
that answers some of them (it's bigger, for "next greater"), pop them and record the answer. Then
push the new element — it's waiting now too.

Because you pop everything smaller before pushing, the stack is always decreasing from bottom to top.

## Pitfalls

- Store **indices**, not values, so you can compute distances and write into the result array.
- Elements left on the stack at the end never found an answer — fill them with the default (0 or -1).
- Strict vs non-strict comparison (`<` vs `<=`) matters when there are duplicates.
