# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-15 08:57:29
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-15 10:07:27
"""
Test cases for the Valid Anagram problem.
"""

import pytest

from main import brute_force, counting_frequency

ARGS = {
    "argnames": ("source", "target", "expected"),
    "argvalues": (
        # Basic Valid Cases
        ("anagram", "nagaram", True),
        ("listen", "silent", True),
        ("evil", "vile", True),
        # Basic Invalid Cases
        ("rat", "car", False),
        ("hello", "bello", False),
        ("test", "ttew", False),
        # Different Lengths
        ("ab", "a", False),
        ("abc", "abcc", False),
        # Case Sensitivity
        ("a", "A", False),
        ("Listen", "silent", False),
        ("Triangle", "Integral", False),
        # Spaces Treated as Characters
        ("a gentleman", "elegant  man", False),
        # Special Characters
        ("a!b@c", "c@b!a", True),
        ("abc!", "abcc", False),
        ("123", "321", True),
        # Repeated Characters
        ("aabbcc", "abcabc", True),
        ("aabbcc", "aabbc", False),
        ("aaab", "abaa", True),
        ("aaab", "aaba", True),
        ("aaab", "abbb", False),
        # Empty & Minimal Inputs
        ("", "", True),
        ("a", "", False),
        ("", "a", False),
        ("a", "a", True),
        # Unicode Characters
        ("café", "facé", True),
        ("àéî", "îéà", True),
        ("你好", "好你", True),
        ("你好", "你他", False),
        # Large Inputs
        ("a" * 100_000 + "b" * 100_000, "b" * 100_000 + "a" * 100_000, True),
        ("a" * 100_000 + "b" * 99_999, "b" * 100_000 + "a" * 100_000, False),
        # Tricky Edge Case
        ("aab", "ab", False),
    ),
    "ids": (
        "Basic Valid 1",
        "Basic Valid 2",
        "Basic Valid 3",
        "Basic Invalid 1",
        "Basic Invalid 2",
        "Basic Invalid 3",
        "Different Lengths 1",
        "Different Lengths 2",
        "Case Sensitivity 1",
        "Case Sensitivity 2",
        "Case Sensitivity 3",
        "Spaces Treated as Characters",
        "Special Characters 1",
        "Special Characters 2",
        "Special Characters 3",
        "Repeated Characters 1",
        "Repeated Characters 2",
        "Repeated Characters 3",
        "Repeated Characters 4",
        "Repeated Characters 5",
        "Empty & Minimal 1",
        "Empty & Minimal 2",
        "Empty & Minimal 3",
        "Empty & Minimal 4",
        "Unicode Characters 1",
        "Unicode Characters 2",
        "Unicode Characters 3",
        "Unicode Characters 4",
        "Large Inputs 1",
        "Large Inputs 2",
        "Tricky Edge Case",
    ),
}


@pytest.mark.parametrize(**ARGS)
def test_brute_force(source, target, expected):
    """
    Test the Brute Force solution.
    """
    assert brute_force(source, target) is expected


@pytest.mark.parametrize(**ARGS)
def test_counting_frequency(source, target, expected):
    """
    Test the Counting Frequency solution.
    """
    assert counting_frequency(source, target) is expected
