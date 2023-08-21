"""Tests API for solving problem Add Two Numbers"""

import pytest

from leetcode_0002_add_two_numbers import api


@pytest.mark.parametrize(
    ["result", ...],
    (
        [..., ...],
        [..., ...],
    )
)
def test_add_two_numbers(result, ...) -> None:
    """Tests solution for problem Add Two Numbers"""

    assert api.add_two_numbers(...) == result