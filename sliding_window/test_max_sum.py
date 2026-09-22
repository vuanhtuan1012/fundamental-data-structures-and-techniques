# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-19 15:38:03
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-19 18:00:02
"""
Tests for the Maximum Sum Subarray problem.
"""

import pytest
from max_sum_subarray import find_max_sum_subarray


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([1, 2, 3, 4, 5], 5, 15),
        ([5], 1, 5),
        ([-1, -2, -3, -4], 2, -3),
        ([-5, -2, -8, -1], 1, -1),
        ([-5, -2, -8, -1], 4, -16),
        ([0, 0, 0, 0], 2, 0),
        ([5, -1, 5, -1, 5], 3, 9),
        ([100, -100, 100, -100, 100], 2, 0),
        ([1, -1, 1, -1, 1], 2, 0),
        ([10, 2, -1, 4, 7], 2, 12),
        ([-10, -20, 5, -2, -1], 2, 3),
        ([7, 7, 7, 7], 3, 21),
        ([1, 2, 3, 4, 5, 6], 4, 18),
    ],
    ids=(f"Valid Input {i}" for i in range(1, 15)),
)
def test_valid_inputs(nums, k, expected):
    """
    Valid inputs
    """
    assert find_max_sum_subarray(nums, k) == expected


@pytest.mark.parametrize(
    "nums, k",
    [([], 1), ([1], 0)],
    ids=["K is greater than the length of nums", "K is less than 1"],
)
def test_invalid_input(nums, k):
    """
    Invalid inputs
    """
    with pytest.raises(ValueError):
        find_max_sum_subarray(nums, k)
