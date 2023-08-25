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

    def __len__(self) -> int:
        if self.next:
            return 1 + len(self.next)

        return 1

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return NotImplemented

        if self.val != other.val:
            return False

        if not self.next and not other.next:
            return True

        if not self.next or not other.next:
            return False

        return self.next == other.next


def _check_preconditions(l1: ListNode | None, l2: ListNode | None) -> bool:
    pass


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Solves problem Add Two Numbers"""

    assert _check_preconditions(l1, l2)

    pass
