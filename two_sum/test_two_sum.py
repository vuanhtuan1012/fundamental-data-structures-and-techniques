# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-13 09:29:35
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-13 22:12:39
"""
Unit tests for the Two Sum problem
"""

import pytest

from main import brute_force, two_pointers, hash_map

ARGS = {
    "names": ("nums", "target", "expected"),
    "values": (
        # Basic Cases
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
        # With Negative Numbers
        ([-1, -2, -3, -4, -5], -8, {2, 4}),
        ([-3, 4, 3, 90], 0, {0, 2}),
        # With Zeroes
        ([0, 4, 3, 0], 0, {0, 3}),
        ([0, 1, 2, 3], 3, ({0, 3}, {1, 2})),
        # Duplicate Numbers
        ([1, 5, 1, 5], 10, {1, 3}),
        ([2, 5, 5, 11], 10, {1, 2}),
        # Smallest Valid Input
        ([1, 2], 3, {0, 1}),
        # Large Numbers
        ([1_000_000, 500_000, 500_000], 1_000_000, {1, 2}),
        # Target is Sum of First and Last
        ([1, 2, 3, 4, 5], 6, ({0, 4}, {1, 3})),
        # Tricky Case
        ([5, 5, 5], 10, ({0, 1}, {0, 2}, {1, 2})),
        # Edge Case
        ([1, 2, 3, 9, 8], 17, {3, 4}),
    ),
    "ids": (
        "Basic Case 1",
        "Basic Case 2",
        "Basic Case 3",
        "With Negative Numbers 1",
        "With Negative Numbers 2",
        "With Zeroes 1",
        "With Zeroes 2",
        "Duplicate Numbers 1",
        "Duplicate Numbers 2",
        "Smallest Valid Input",
        "Large Numbers",
        "Target is Sum of First and Last",
        "Tricky Case",
        "Edge Case",
    ),
}


@pytest.mark.parametrize(
    ARGS["names"],
    ARGS["values"],
    ids=ARGS["ids"],
)
def test_brute_force(nums, target, expected):
    """
    Test the Brute Force solution
    """
    result = brute_force(nums, target)
    if isinstance(expected, set):
        assert result == expected
    if isinstance(expected, tuple):
        assert result in expected


@pytest.mark.parametrize(
    ARGS["names"],
    ARGS["values"],
    ids=ARGS["ids"],
)
def test_two_pointers(nums, target, expected):
    """
    Test the Two Pointers solution
    """
    result = two_pointers(nums, target)
    if isinstance(expected, set):
        assert result == expected
    if isinstance(expected, tuple):
        assert result in expected


@pytest.mark.parametrize(
    ARGS["names"],
    ARGS["values"],
    ids=ARGS["ids"],
)
def test_hash_map(nums, target, expected):
    """
    Test the Hash Map solution
    """
    result = hash_map(nums, target)
    if isinstance(expected, set):
        assert result == expected
    if isinstance(expected, tuple):
        assert result in expected
