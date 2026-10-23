"""1-D DP: top-down with @cache, bottom-up with a table, and O(1) space."""
from functools import cache


def rob_top_down(nums: list[int]) -> int:
    @cache
    def best(i: int) -> int:             # state: most money from houses 0..i
        if i < 0:
            return 0                     # base case
        return max(best(i - 1), best(i - 2) + nums[i])   # skip i, or rob i
    return best(len(nums) - 1)


def rob_constant_space(nums: list[int]) -> int:
    prev2 = prev1 = 0                    # dp[i-2], dp[i-1]
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1


def coin_change(coins: list[int], amount: int) -> int:
    """Fewest coins that make amount, or -1. dp[a] = fewest coins to make a."""
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return int(dp[amount]) if dp[amount] != float("inf") else -1


def word_break(s: str, words: list[str]) -> bool:
    """dp[i] = can s[:i] be split into dictionary words?"""
    word_set = set(words)
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))
    return dp[len(s)]
