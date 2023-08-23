"""Tests API for solving problem Add Two Numbers"""

import pytest

from leetcode_0002_add_two_numbers import api


@pytest.mark.parametrize(
    ["result", "l1", "l2"],
    (
        [..., ...],
        [..., ...],
    ),
)
def test_add_two_numbers(
    result: api.ListNode, l1: api.ListNode, l2: api.ListNode
) -> None:
    """Tests solution for problem Add Two Numbers"""

    assert api.add_two_numbers(l1, l2) == result
