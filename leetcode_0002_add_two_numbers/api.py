"""API for solving problem Add Two Numbers"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list"""

    def __init__(
        self,
        val: int = 0,
        next: Optional["ListNode"] = None,  # pylint: disable=redefined-builtin
    ):
        self.val = val
        self.next = next


def _check_preconditions(l1: ListNode, l2: ListNode) -> bool:
    pass


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """Solves problem Add Two Numbers"""

    assert _check_preconditions(l1, l2)

    pass
