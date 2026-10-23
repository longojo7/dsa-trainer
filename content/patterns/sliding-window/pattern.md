---
title: Sliding Window
category: Arrays & Strings
order: 2
summary: Grow a window on the right, shrink it on the left, and track the best window seen.
signals:
  - Contiguous subarray or substring
  - Longest / shortest / max / min window satisfying a condition
  - '"At most K" distinct, replacements, or zeros'
  - Anagram or permutation of a pattern inside a string
complexity:
  time: O(n) — each index enters and leaves the window once
  space: O(k) for the window's counts (often O(alphabet))
problems:
  - { name: Best Time to Buy and Sell Stock, id: 121, slug: best-time-to-buy-and-sell-stock, difficulty: Easy }
  - { name: Longest Substring Without Repeating Characters, id: 3, slug: longest-substring-without-repeating-characters, difficulty: Medium }
  - { name: Longest Repeating Character Replacement, id: 424, slug: longest-repeating-character-replacement, difficulty: Medium }
  - { name: Permutation in String, id: 567, slug: permutation-in-string, difficulty: Medium }
  - { name: Minimum Window Substring, id: 76, slug: minimum-window-substring, difficulty: Hard }
---
## Key idea

Keep a window `[left, right]` and some state about it (a counter, a sum, a set). For each `right`:

1. **Add** `s[right]` to the state.
2. **While the window is invalid**, remove `s[left]` and move `left` forward.
3. **Record** the answer (the window is now valid).

**Fixed-size windows** (size `k`) are simpler: add the new element, remove the one that fell out at `right - k`.

The trick is deciding what "invalid" means — say it in one sentence before coding
(e.g. *"invalid when some character appears twice"*).

## Pitfalls

- Shrinking with `if` instead of `while` — one step may not restore validity.
- For "minimum window" problems, record the answer *inside* the shrink loop (while valid), not after.
- Sliding window needs the condition to be **monotonic**: making the window bigger can only make it "more invalid". Negative numbers break this for sum problems → use prefix sums instead.
