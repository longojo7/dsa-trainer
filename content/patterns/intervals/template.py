"""Intervals: merge overlaps, and count rooms needed at once."""
import heapq


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:        # overlaps the last one
            merged[-1][1] = max(merged[-1][1], end)   # max: it might be nested
        else:
            merged.append([start, end])
    return merged


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    ends: list[int] = []                 # min-heap of end times of meetings in progress
    for start, end in sorted(intervals):
        if ends and ends[0] <= start:    # earliest meeting has finished → reuse its room
            heapq.heappop(ends)
        heapq.heappush(ends, end)
    return len(ends)
