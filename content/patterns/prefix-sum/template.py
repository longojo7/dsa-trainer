"""Prefix sums: range queries, and counting subarrays that sum to k."""
from collections import defaultdict


def build_prefix(nums: list[int]) -> list[int]:
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return prefix                       # sum(nums[i:j]) == prefix[j] - prefix[i]


def count_subarrays_with_sum(nums: list[int], k: int) -> int:
    seen: defaultdict[int, int] = defaultdict(int)
    seen[0] = 1                         # the empty prefix
    running = count = 0
    for x in nums:
        running += x
        count += seen[running - k]      # earlier prefixes that make a sum of k
        seen[running] += 1
    return count
