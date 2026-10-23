---
title: Hash Map & Set
category: Arrays & Strings
order: 4
summary: Trade memory for speed — O(1) lookups to replace an inner search loop.
signals:
  - '"Have I seen this before?" (duplicates, complements like Two Sum)'
  - Counting frequencies (anagrams, majority element)
  - Grouping items by a computed key
  - Need O(n) and the input is unsorted
complexity:
  time: O(n) average
  space: O(n)
problems:
  - { name: Two Sum, id: 1, slug: two-sum, difficulty: Easy }
  - { name: Contains Duplicate, id: 217, slug: contains-duplicate, difficulty: Easy }
  - { name: Valid Anagram, id: 242, slug: valid-anagram, difficulty: Easy }
  - { name: Group Anagrams, id: 49, slug: group-anagrams, difficulty: Medium }
  - { name: Longest Consecutive Sequence, id: 128, slug: longest-consecutive-sequence, difficulty: Medium }
---
## Key idea

If your brute force is "for each element, scan the rest looking for X", store what you've seen in a
`dict`/`set` so that scan becomes one lookup.

The creative part is choosing the **key**:

- Two Sum → key is the number, value is its index; look up `target - x`.
- Group Anagrams → key is `tuple(sorted(word))` or a 26-letter count tuple.
- Longest Consecutive → a `set`, and only start counting from `x` when `x - 1` isn't in it.

## Pitfalls

- Lists aren't hashable — convert to `tuple` for keys.
- In Two Sum, check for the complement **before** inserting the current number (so you don't pair an element with itself).
- Mention that hash maps are O(1) *average*; worst case O(n) per operation.
