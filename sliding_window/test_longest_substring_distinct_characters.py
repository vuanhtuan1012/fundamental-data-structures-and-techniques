# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-21 20:31:32
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-21 20:39:48
"""
Tests for the Longest Substring with At Most K Distinct Characters problem.
"""

import pytest
from longest_substring_distinct_characters import find_length_longest_substring


@pytest.mark.parametrize(
    "string, k, expected",
    [
        # Basic cases
        pytest.param("eceba", 2, 3, id="basic_case"),
        pytest.param("aa", 1, 2, id="all_same_characters"),
        pytest.param("abc", 2, 2, id="three_unique_characters_k2"),
        pytest.param("aabacbebebe", 3, 7, id="longest_window_in_the_middle"),
        # k = 1
        pytest.param("abcba", 1, 1, id="k1_all_different"),
        pytest.param("aaabbbaaa", 1, 3, id="k1_longest_repeated_block"),
        pytest.param("aabbcc", 1, 2, id="k1_multiple_blocks"),
        # k >= number of distinct characters
        pytest.param("abcabc", 3, 6, id="k_equals_distinct_count"),
        pytest.param("abcabc", 10, 6, id="k_greater_than_distinct_count"),
        pytest.param("aaaa", 5, 4, id="k_greater_than_string_length"),
        # k = 0
        pytest.param("", 0, 0, id="empty_string_k0"),
        pytest.param("abc", 0, 0, id="k0_non_empty_string"),
        # Empty string
        pytest.param("", 1, 0, id="empty_string"),
        pytest.param("", 5, 0, id="empty_string_large_k"),
        # Single character
        pytest.param("a", 1, 1, id="single_character_k1"),
        pytest.param("a", 0, 0, id="single_character_k0"),
        pytest.param("a", 5, 1, id="single_character_large_k"),
        # Repeated characters
        pytest.param("aaaaaa", 1, 6, id="all_characters_same"),
        pytest.param("aabbcc", 2, 4, id="two_distinct_characters"),
        pytest.param("aabbcc", 1, 2, id="one_distinct_character"),
        # Spaces / special characters
        pytest.param("a b c", 2, 3, id="spaces_are_characters"),
        pytest.param("!!@@##", 2, 4, id="special_characters"),
        pytest.param("a!a!b", 2, 4, id="letters_and_special_characters"),
        # Case sensitivity
        pytest.param("aAbB", 2, 2, id="case_sensitive_characters"),
        pytest.param("aAaA", 1, 1, id="uppercase_and_lowercase"),
        # Cases requiring multiple left-pointer movements
        pytest.param("abcde", 2, 2, id="many_shrinks_required"),
        pytest.param("aaabcbb", 2, 4, id="shrink_multiple_characters"),
        pytest.param("abaccc", 2, 4, id="shrink_until_window_valid"),
        # Longest valid window is at different positions
        pytest.param("aabccbb", 2, 5, id="longest_window_at_end"),
        pytest.param("ccaabbb", 2, 5, id="longest_window_at_end_repeated"),
        pytest.param("abcaa", 2, 3, id="longest_window_at_end_after_shrink"),
    ],
)
def test_find_length_longest_substring(string, k, expected):
    """
    Test find_length_longest_substring
    """
    assert find_length_longest_substring(string, k) == expected
