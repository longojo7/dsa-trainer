"""Monotonic stack: for each day, how many days until a warmer temperature."""
from collections import deque


def daily_temperatures(temps: list[int]) -> list[int]:
    answer = [0] * len(temps)
    waiting: list[int] = []                        # indices; temps decreasing bottom → top
    for i, t in enumerate(temps):
        while waiting and temps[waiting[-1]] < t:  # t answers everyone colder on the stack
            j = waiting.pop()
            answer[j] = i - j
        waiting.append(i)
    return answer                                  # leftovers keep the default 0


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Monotonic deque variant: front of the deque is always the window's max."""
    dq: deque[int] = deque()
    out: list[int] = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:                         # front fell out of the window
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
