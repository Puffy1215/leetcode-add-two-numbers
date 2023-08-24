"""Tests API for solving problem Add Two Numbers"""

import pytest

from leetcode_0002_add_two_numbers import api


@pytest.mark.parametrize(
    ["result", "l1", "l2"],
    (
        [
            api.ListNode.from_list([7, 0, 8]),
            api.ListNode.from_list([2, 4, 3]),
            api.ListNode.from_list([5, 6, 4]),
        ],
        [
            api.ListNode.from_list([0]),
            api.ListNode.from_list([0]),
            api.ListNode.from_list([0]),
        ],
        [
            api.ListNode.from_list([8, 9, 9, 9, 0, 0, 0, 1]),
            api.ListNode.from_list([9, 9, 9, 9, 9, 9, 9]),
            api.ListNode.from_list([9, 9, 9, 9]),
        ],
    ),
)
def test_add_two_numbers(
    result: api.ListNode | None, l1: api.ListNode | None, l2: api.ListNode | None
) -> None:
    """Tests solution for problem Add Two Numbers"""

    assert api.add_two_numbers(l1, l2) == result
