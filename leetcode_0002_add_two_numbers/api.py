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


LEN_MIN = 1
LEN_MAX = 100


def _check_length(l: ListNode) -> bool:
    return LEN_MIN <= len(l) <= LEN_MAX


VAL_MIN = 0
VAL_MAX = 9


def _check_vals(l: ListNode | None) -> bool:
    while l:
        if not VAL_MIN <= l.val <= VAL_MAX:
            return False

        l = l.next

    return True


def _check_leading_zeros(l: ListNode) -> bool:
    return not (l.next and l.val == 0)


def _check_preconditions(l: ListNode) -> bool:
    if not _check_length(l):
        return False

    if not _check_vals(l):
        return False

    if not _check_leading_zeros(l):
        return False

    return True


def _recursive_add_two_numbers(
    l1: ListNode | None, l2: ListNode | None, x: int
) -> ListNode | None:
    if not l1:
        return l2
    if not l2:
        return l1

    val = sum([l.val for l in [l1, l2] if l] + [x])

    if val > 9:
        next = _recursive_add_two_numbers(
            l1.next if l1 else l1, l2.next if l2 else l2, val // 10
        )
    else:
        next = None

    return ListNode(val % 10, next)


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Solves problem Add Two Numbers"""

    for l in [l1, l2]:
        if l:
            assert _check_preconditions(l)

    return _recursive_add_two_numbers(l1, l2, 0)
