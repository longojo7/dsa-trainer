"""Binary search: one template — find the first value where condition() is True."""
from typing import Callable


def first_true(lo: int, hi: int, condition: Callable[[int], bool]) -> int:
    """Smallest x in [lo, hi] with condition(x) True. Returns hi if none (pick hi accordingly)."""
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(mid):
            hi = mid          # mid might be the answer — keep it
        else:
            lo = mid + 1      # mid is definitely not the answer
    return lo


def search(nums: list[int], target: int) -> int:
    """Classic: index of target in sorted nums, or -1."""
    i = first_true(0, len(nums), lambda m: nums[m] >= target)
    return i if i < len(nums) and nums[i] == target else -1


def min_eating_speed(piles: list[int], h: int) -> int:
    """Binary search on the answer: slowest speed that finishes within h hours."""
    def hours_needed(speed: int) -> int:
        return sum((p + speed - 1) // speed for p in piles)   # ceil division
    return first_true(1, max(piles), lambda speed: hours_needed(speed) <= h)
