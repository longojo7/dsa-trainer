"""Two pointers (opposite ends): find two numbers in a SORTED list that sum to target."""


def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    l, r = 0, len(nums) - 1
    while l < r:
        total = nums[l] + nums[r]
        if total == target:      # ← the condition you're looking for
            return l, r
        if total < target:
            l += 1               # need a bigger sum → move the small side up
        else:
            r -= 1               # need a smaller sum → move the big side down
    return None


def remove_duplicates(nums: list[int]) -> int:
    """Same-direction variant: dedupe a sorted list in place, return new length."""
    write = 0
    for read in range(len(nums)):
        if read == 0 or nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
