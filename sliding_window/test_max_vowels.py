# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-19 18:40:06
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-19 19:18:11
"""
Tests for the Maximum Number of Vowels in a Substring of Given Length problem.
"""

import pytest
from max_vowels import find_max_vowels


@pytest.mark.parametrize(
    "string, k, expected",
    [
        pytest.param("abciiidef", 3, 3, id="mixed_vowels_example"),
        pytest.param("aeiou", 2, 2, id="all_vowels_k2"),
        pytest.param("leetcode", 3, 2, id="leetcode_k3"),
        pytest.param("rhythms", 3, 0, id="no_vowels"),
        pytest.param("hello", 2, 1, id="hello_k2"),
        pytest.param("abcde", 3, 1, id="alternating_vowels"),
        pytest.param("abcdef", 1, 1, id="k1_with_vowel"),
        pytest.param("abcdef", 2, 1, id="k2"),
        pytest.param("a", 1, 1, id="single_vowel"),
        pytest.param("b", 1, 0, id="single_consonant"),
        pytest.param("aeiou", 5, 5, id="full_string_all_vowels"),
        pytest.param("bcdfg", 5, 0, id="full_string_no_vowels"),
        pytest.param("aaaaaa", 3, 3, id="all_vowels_repeated"),
        pytest.param("bbbbbb", 3, 0, id="all_consonants_repeated"),
        pytest.param("ababab", 3, 2, id="alternating_vowels_consonants"),
        pytest.param("xyzaiou", 3, 3, id="vowels_at_end"),
        pytest.param("uoiea", 1, 1, id="reverse_vowels_k1"),
        pytest.param("uoiea", 5, 5, id="reverse_vowels_full_string"),
        pytest.param("aab", 2, 2, id="vowels_at_start"),
        pytest.param("baa", 2, 2, id="vowels_at_end"),
        pytest.param("abca", 2, 1, id="vowels_at_both_ends"),
        pytest.param("zzzaaa", 3, 3, id="vowels_in_second_half"),
        pytest.param("aaazzz", 3, 3, id="vowels_in_first_half"),
        pytest.param("zaezi", 3, 2, id="vowels_mixed_with_consonants"),
        pytest.param("aezio", 4, 3, id="four_vowels_in_window"),
        pytest.param("bcdaei", 3, 3, id="one_vowel_in_window"),
        pytest.param("aaaaabbbbb", 5, 5, id="vowels_then_consonants"),
        pytest.param("bbbbbaaaaa", 5, 5, id="consonants_then_vowels"),
    ],
)
def test_valid_input(string, k, expected):
    """
    Test valid inputs
    """
    assert find_max_vowels(string, k) == expected


@pytest.mark.parametrize(
    "string, k",
    [("", 1), ("1", 0)],
    ids=["K is greater than the string length", "K is less than 1"],
)
def test_invalid_input(string, k):
    """
    Test invalid input
    """
    with pytest.raises(ValueError):
        find_max_vowels(string, k)
