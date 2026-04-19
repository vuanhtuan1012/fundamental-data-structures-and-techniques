# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-17 18:53:11
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-19 04:46:48
"""
Test cases for Top Frequent Elements
"""

import pytest

from main import top_k_frequent_buckets, top_k_frequent_sorting

ARGS = {
    "argnames": ("nums", "k", "expected"),
    "argvalues": (
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 4], 1, {4}),
        ([5, 5, 5, 6], 2, {5, 6}),
        ([7, 8, 9], 3, {7, 8, 9}),
        ([10], 0, set()),
        ([10], 2, {10}),
        ([], 1, set()),
    ),
    "ids": (
        "Basic Case",
        "Single Element",
        "All Elements Same",
        "Two Most Frequent",
        "All Unique",
        "K is Zero",
        "K Greater than Unique Elements",
        "Empty List",
    ),
}


@pytest.mark.parametrize(**ARGS)
def test_top_k_frequent_sorting(nums, k, expected):
    """
    Test the sorting approach
    """
    assert set(top_k_frequent_sorting(nums, k)) == expected


@pytest.mark.parametrize(**ARGS)
def test_top_k_frequent_buckets(nums, k, expected):
    """
    Test the bucket sort approach
    """
    assert set(top_k_frequent_buckets(nums, k)) == expected
