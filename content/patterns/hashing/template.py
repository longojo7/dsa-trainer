"""Hash map lookups and grouping by a computed key."""
from collections import defaultdict


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    index_of: dict[int, int] = {}
    for i, x in enumerate(nums):
        if target - x in index_of:          # check BEFORE inserting x
            return index_of[target - x], i
        index_of[x] = i
    return None


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: defaultdict[tuple[str, ...], list[str]] = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)   # ← the key is the creative part
    return list(groups.values())


def longest_consecutive(nums: list[int]) -> int:
    values = set(nums)
    best = 0
    for x in values:
        if x - 1 not in values:              # only start at the beginning of a run
            length = 1
            while x + length in values:
                length += 1
            best = max(best, length)
    return best
