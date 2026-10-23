"""Variable-size sliding window: longest substring without repeating characters."""
from collections import Counter


def longest_unique_substring(s: str) -> int:
    counts: Counter[str] = Counter()
    left = best = 0
    for right, ch in enumerate(s):
        counts[ch] += 1                      # 1. add s[right] to the window
        while counts[ch] > 1:                # 2. shrink while invalid  ← your condition
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)   # 3. window is valid → record
    return best


def max_sum_fixed_window(nums: list[int], k: int) -> int:
    """Fixed-size variant: max sum of any k consecutive elements."""
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best
