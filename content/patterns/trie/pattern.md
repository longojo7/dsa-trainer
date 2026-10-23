---
title: Trie (Prefix Tree)
category: Strings
order: 1
summary: A tree of characters for fast prefix lookups across many words.
signals:
  - Autocomplete, or "does any word start with this prefix?"
  - Search many words at once in a grid (Word Search II)
  - Wildcard matching against a dictionary
  - Replace words with their shortest root
complexity:
  time: O(L) per insert/search, where L is the word length
  space: O(total characters stored)
problems:
  - { name: Implement Trie (Prefix Tree), id: 208, slug: implement-trie-prefix-tree, difficulty: Medium }
  - { name: Design Add and Search Words Data Structure, id: 211, slug: design-add-and-search-words-data-structure, difficulty: Medium }
  - { name: Replace Words, id: 648, slug: replace-words, difficulty: Medium }
  - { name: Word Search II, id: 212, slug: word-search-ii, difficulty: Hard }
---
## Key idea

Each node is a `dict` from character → child node, plus a flag marking "a word ends here". Words
that share a prefix share a path, so checking a prefix costs only its length, no matter how many
words are stored.

In grid problems with many target words, walk the trie **alongside** the DFS: stop as soon as the
current path isn't a prefix of any word.

## Pitfalls

- `search` must check the end-of-word flag; `starts_with` must not.
- In Word Search II, remove found words (or clear the flag) to avoid duplicate results.
- For a single lookup, a `set` is simpler — a trie pays off for *prefix* queries.
