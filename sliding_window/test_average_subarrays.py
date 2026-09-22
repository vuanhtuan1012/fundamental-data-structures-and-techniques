# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-19 17:46:31
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-19 17:59:22
"""
Tests for the Average Subarrays problem
"""

import pytest
from average_subarrays import find_averages


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, 2, 6, -1, 4, 1, 8, 2], 5, [2.2, 2.8, 2.4, 3.6, 2.8]),
        ([1, 2, 3, 4, 5], 1, [1.0, 2.0, 3.0, 4.0, 5.0]),
        ([1, 2, 3, 4, 5], 5, [3.0]),
        ([5], 1, [5.0]),
        ([-1, -2, -3, -4], 2, [-1.5, -2.5, -3.5]),
        ([-5, -2, -8, -1], 1, [-5.0, -2.0, -8.0, -1.0]),
        ([-5, -2, -8, -1], 4, [-4.0]),
        ([0, 0, 0, 0], 2, [0.0, 0.0, 0.0]),
        ([1, -1, 1, -1, 1], 2, [0.0, 0.0, 0.0, 0.0]),
        ([1, 2, 4, 8], 2, [1.5, 3.0, 6.0]),
        ([1, 2, 3, 4], 3, [2.0, 3.0]),
        ([10, 0, 0, 0, 10], 2, [5.0, 0.0, 0.0, 5.0]),
        ([-10, 0, 10], 2, [-5.0, 5.0]),
        ([1, 1, 1, 1, 1], 3, [1.0, 1.0, 1.0]),
        ([1, 2, 3, 4, 5, 6], 4, [2.5, 3.5, 4.5]),
    ],
    ids=[f"Valid Input {i}" for i in range(1, 16)],
)
def test_valid_input(nums, k, expected):
    """
    Test valid inputs
    """
    assert find_averages(nums, k) == expected


@pytest.mark.parametrize(
    "nums, k",
    [([], 1), ([1], 0)],
    ids=["K is greater than the length of nums", "K is less than 1"],
)
def test_invalid_inputs(nums, k):
    """
    Test invalid inputs
    """
    with pytest.raises(ValueError):
        find_averages(nums, k)
