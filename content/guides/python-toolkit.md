---
title: Python Interview Toolkit
order: 2
summary: The standard-library tools that turn 15 lines into 1 — and their costs.
---
## Collections

```python
from collections import Counter, defaultdict, deque

Counter("banana")              # {'a': 3, 'n': 2, 'b': 1}
Counter(nums).most_common(2)   # [(val, count), ...] top 2
graph = defaultdict(list)      # missing key → []
q = deque([start]); q.append(x); q.popleft()   # O(1) both ends
```

## Heaps — `heapq` is a MIN-heap

```python
import heapq
heapq.heapify(nums)            # O(n), in place
heapq.heappush(h, (priority, item))
heapq.heappop(h)               # smallest
heapq.heappush(h, -x)          # max-heap trick: negate
heapq.nlargest(k, nums, key=...)
```

## Binary search — `bisect`

```python
import bisect
bisect.bisect_left(a, x)       # first index with a[i] >= x
bisect.bisect_right(a, x)      # first index with a[i] > x
bisect.insort(a, x)            # insert keeping a sorted (O(n) shift)
```

## Sorting

```python
nums.sort()                            # in place, O(n log n), stable
sorted(pairs, key=lambda p: (p[1], -p[0]))   # by second asc, then first desc
```

## Memoization

```python
from functools import cache

@cache
def dp(i, j): ...
```

## Handy built-ins

```python
for i, x in enumerate(nums): ...
for a, b in zip(xs, ys): ...
float("inf"), float("-inf")
divmod(17, 5)                  # (3, 2)
-7 // 2                        # -4  (floors toward -inf!)
int(-7 / 2)                    # -3  (truncates toward 0)
ord("a"), chr(97)
"".join(chars)                 # strings are immutable — build a list, then join
grid = [[0] * cols for _ in range(rows)]   # NOT [[0] * cols] * rows
```

## Complexity of common operations

| Operation | Cost |
| --- | --- |
| `list.append`, `list.pop()` | O(1) |
| `list.pop(0)`, `list.insert(0, x)`, `x in list` | O(n) |
| `dict` / `set` get, set, `in` | O(1) average |
| `deque.appendleft`, `deque.popleft` | O(1) |
| `heappush`, `heappop` | O(log n) |
| `s[a:b]` slicing | O(b − a) — it copies |
