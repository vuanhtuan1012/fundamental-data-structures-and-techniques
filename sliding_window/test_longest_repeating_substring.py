# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-21 22:45:26
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-21 23:20:48
"""
Tests for the Longest Repeating Character Replacement problem
"""

import pytest
from longest_repeating_substring import find_longest_repeating_substring


@pytest.mark.parametrize(
    "string, k, expected",
    [
        # Basic cases
        pytest.param("ABAB", 2, 4, id="basic_case"),
        pytest.param("AABABBA", 1, 4, id="standard_example"),
        pytest.param("ABBB", 2, 4, id="replace_one_character"),
        pytest.param("AAB", 1, 3, id="one_replacement_makes_all_equal"),
        # k = 0
        pytest.param("A", 0, 1, id="single_character_k0"),
        pytest.param("AAAA", 0, 4, id="already_repeating_k0"),
        pytest.param("ABAA", 0, 2, id="no_replacement_allowed"),
        pytest.param("ABCDE", 0, 1, id="all_different_k0"),
        # All characters are the same
        pytest.param("AAAAAA", 0, 6, id="all_same_k0"),
        pytest.param("AAAAAA", 3, 6, id="all_same_k3"),
        # All characters are different
        pytest.param("ABCDE", 1, 2, id="all_different_k1"),
        pytest.param("ABCDE", 2, 3, id="all_different_k2"),
        pytest.param("ABCDE", 4, 5, id="all_different_k4"),
        # k is large enough to cover the whole string
        pytest.param("ABCDE", 5, 5, id="k_equals_string_length"),
        pytest.param("ABCDEFG", 7, 7, id="k_equals_string_length_large"),
        pytest.param("ABCD", 10, 4, id="k_greater_than_string_length"),
        # Repeated characters with replacement
        pytest.param("BAAA", 0, 3, id="existing_repeated_block"),
        pytest.param("BAAA", 1, 4, id="replace_outlier"),
        pytest.param("AABBB", 1, 4, id="replace_one_a"),
        pytest.param("AABBB", 2, 5, id="replace_two_as"),
        # Alternating characters
        pytest.param("ABABAB", 1, 3, id="alternating_k1"),
        pytest.param("ABABAB", 2, 5, id="alternating_k2"),
        pytest.param("ABABAB", 3, 6, id="alternating_k3"),
        # Cases requiring the window to shrink
        pytest.param("AABABBA", 1, 4, id="shrink_after_invalid_window"),
        pytest.param("ABBBAC", 1, 4, id="shrink_after_long_run"),
        pytest.param("AAABBC", 1, 4, id="shrink_with_competing_frequencies"),
        # Dominant character changes
        pytest.param("AAABBBA", 1, 4, id="dominant_character_changes"),
        pytest.param("AAAABBBB", 2, 6, id="two_dominant_blocks"),
        # Longer / more complex cases
        pytest.param("ABBBCCCCC", 1, 6, id="longest_window_near_end"),
        pytest.param("AABCCBB", 2, 5, id="multiple_valid_windows"),
        pytest.param("ABCCCDD", 2, 5, id="competing_character_groups"),
    ],
)
def test_find_longest_repeating_substring(string, k, expected):
    """
    Test the find_longest_repeating_character_replacement function
    """
    assert find_longest_repeating_substring(string, k) == expected


def test_invalid_input():
    """
    Test invalid input
    """
    with pytest.raises(ValueError):
        find_longest_repeating_substring("abc", 1)
