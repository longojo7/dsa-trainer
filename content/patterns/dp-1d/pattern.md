---
title: 1-D Dynamic Programming
category: Dynamic Programming
order: 1
summary: The answer for i is built from answers for smaller i — define the state, then the recurrence.
signals:
  - Count the number of ways to do something
  - Min / max cost to reach the end, with choices at each step
  - '"Can you make X?" from pieces (coin change, word break)'
  - A brute-force recursion that recomputes the same subproblems
complexity:
  time: O(n × choices per step)
  space: O(n), often reducible to O(1)
problems:
  - { name: Climbing Stairs, id: 70, slug: climbing-stairs, difficulty: Easy }
  - { name: House Robber, id: 198, slug: house-robber, difficulty: Medium }
  - { name: Coin Change, id: 322, slug: coin-change, difficulty: Medium }
  - { name: Word Break, id: 139, slug: word-break, difficulty: Medium }
  - { name: Longest Increasing Subsequence, id: 300, slug: longest-increasing-subsequence, difficulty: Medium }
---
## Key idea

Answer four questions **out loud**, in this order:

1. **State** — what does `dp[i]` mean, in one English sentence? (*"the most money robbing houses 0..i"*)
2. **Recurrence** — how does `dp[i]` use smaller states? (*rob i: `dp[i-2] + nums[i]`, skip i: `dp[i-1]`*)
3. **Base cases** — the smallest `i` values you can answer directly.
4. **Answer** — which cell holds the final result? (`dp[n-1]`, `max(dp)`, ...)

Start with a recursive solution + `@cache` (top-down), which is easy to derive. Convert it to a
table (bottom-up) if asked. Then notice when you only need the last one or two values → O(1) space.

## Pitfalls

- Vague state definitions. If you can't say what `dp[i]` means in one sentence, the recurrence will be wrong.
- Initializing a min-cost table with 0 instead of `inf`.
- Loop order: bottom-up must compute every state before it's used.
