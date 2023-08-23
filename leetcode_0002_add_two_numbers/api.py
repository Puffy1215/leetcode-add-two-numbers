"""API for solving problem Add Two Numbers"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list"""

    @classmethod
    def from_list(cls, l: list[int]) -> Optional["ListNode"] | None:
        """Converts Python list to LeetCode list"""

        if not l:
            return None

        nodes = [ListNode(val) for val in l]
        for this, next in zip(  # pylint: disable=redefined-builtin
            nodes[:-1],
            nodes[1:],
        ):
            this.next = next

        return nodes[0]

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
