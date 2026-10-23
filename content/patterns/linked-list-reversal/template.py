"""In-place linked list reversal."""
from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev, curr = None, head
    while curr:
        nxt = curr.next       # 1. save the rest of the list
        curr.next = prev      # 2. flip the pointer
        prev, curr = curr, nxt  # 3. advance
    return prev               # prev is the new head


def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    """Reverse positions left..right (1-indexed). The dummy handles left == 1."""
    dummy = ListNode(0, head)
    before = dummy
    for _ in range(left - 1):
        before = before.next
    prev, curr = None, before.next
    for _ in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    before.next.next = curr   # old sublist head is now its tail; reconnect to the rest
    before.next = prev
    return dummy.next
