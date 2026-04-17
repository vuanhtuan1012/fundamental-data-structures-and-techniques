# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-17 18:53:11
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-17 19:02:47
"""
Test cases for Top Frequent Elements
"""

import pytest

from main import get_top_frequent_elements

ARGS = {
    "argnames": ("nums", "k", "expected"),
    "argvalues": (
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 4], 1, {4}),
        ([5, 5, 5, 6], 2, {5, 6}),
        ([7, 8, 9], 3, {7, 8, 9}),
        ([10], 2, {10}),
        ([], 1, set()),
    ),
    "ids": (
        "Basic Case",
        "Single Element",
        "All Elements Same",
        "Two Most Frequent",
        "All Unique",
        "K Greater than Unique Elements",
        "Empty List",
    ),
}


@pytest.mark.parametrize(**ARGS)
def test_get_top_frequent_elements(nums, k, expected):
    """
    Test the get_top_frequent_elements function
    """
    assert set(get_top_frequent_elements(nums, k)) == expected
