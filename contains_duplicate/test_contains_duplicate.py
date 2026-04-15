# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-14 20:19:00
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-15 10:16:56
"""
Test cases for the Contains Duplicate problem
"""

import pytest

from main import brute_force, sorting, hash_set

ARGS = {
    "argnames": ("nums", "expected"),
    "argvalues": (
        # Basic Cases
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 1], True),
        # Edge Cases
        ([], False),
        ([5], False),
        # Duplicates in Different Positions
        ([1, 2, 3, 2], True),
        ([2, 2, 3, 4], True),
        # Negative Numbers & Zeros
        ([-1, -2, -3, -1], True),
        ([0, 1, 2, 3, 0], True),
        ([-1, 0, 1, 2], False),
        # Large Input Cases
        (list(range(10_000)), False),
        (list(range(10_000)) + [9999], True),
        # Tricky Cases
        ([1, 2, 3, 4, 5, 5], True),
        ([10**9, -(10**9), 10**9], True),
        (list(range(1, 11)), False),
    ),
    "ids": (
        "Basic Case 1",
        "Basic Case 2",
        "Basic Case 3",
        "Edge Case 1: No Elements",
        "Edge Case 2: Single Element",
        "Duplicates in Different Positions 1",
        "Duplicates in Different Positions 2",
        "Negative Numbers & Zeros 1",
        "Negative Numbers & Zeros 2",
        "Negative Numbers & Zeros 3",
        "Large Input 1",
        "Large Input 2",
        "Tricky Case 1",
        "Tricky Case 2",
        "Tricky Case 3",
    ),
}


@pytest.mark.parametrize(**ARGS)
def test_brute_force(nums, expected):
    """
    Test the Brute Force solution
    """
    assert brute_force(nums) is expected


@pytest.mark.parametrize(**ARGS)
def test_sorting(nums, expected):
    """
    Test the Sorting solution
    """
    assert sorting(nums) is expected


@pytest.mark.parametrize(**ARGS)
def test_hash_set(nums, expected):
    """
    Test the Hash Set solution
    """
    assert hash_set(nums) is expected
