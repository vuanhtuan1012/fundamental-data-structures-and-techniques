# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-22 11:24:11
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-22 12:57:22
"""
Test for the Permutation in String problem.
"""

import pytest
from permutation_string import contains_permutation


@pytest.mark.parametrize(
    "pattern, string, expected",
    [
        # Basic cases
        pytest.param("ab", "eidbaooo", True, id="basic_positive"),
        pytest.param("ab", "eidboaoo", False, id="basic_negative"),
        pytest.param("abc", "bbbca", True, id="permutation_at_end"),
        pytest.param("xyz", "afdgzyxksldfm", True, id="permutation_in_middle"),
        # Exact match / whole string
        pytest.param("abc", "abc", True, id="identical_strings"),
        pytest.param("abc", "cba", True, id="whole_string_is_permutation"),
        pytest.param("abc", "def", False, id="same_length_no_match"),
        # Single character
        pytest.param("a", "a", True, id="single_character_match"),
        pytest.param("a", "b", False, id="single_character_no_match"),
        pytest.param("a", "aaaa", True, id="single_character_repeated_in_s2"),
        pytest.param("z", "abcdef", False, id="single_character_absent"),
        # Repeated characters in s1
        pytest.param("aa", "aaa", True, id="repeated_character_match"),
        pytest.param("aa", "abcaa", True, id="repeated_character_at_end"),
        pytest.param("aa", "abca", False, id="insufficient_repeated_characters"),
        pytest.param("aab", "eidbaaboo", True, id="repeated_characters_in_s1"),
        pytest.param("aaab", "abab", False, id="wrong_character_frequencies"),
        # Different order
        pytest.param("abc", "cba", True, id="reverse_order"),
        pytest.param("abc", "bac", True, id="different_order"),
        pytest.param("abc", "cab", True, id="rotated_order"),
        # Valid permutation appears at different positions
        pytest.param("ab", "abxxxx", True, id="permutation_at_start"),
        pytest.param("ab", "xabxxx", True, id="permutation_in_middle"),
        pytest.param("ab", "xxxab", True, id="permutation_at_end"),
        # Multiple windows / overlapping windows
        pytest.param("ab", "aab", True, id="overlapping_candidate_windows"),
        pytest.param("abc", "abcabc", True, id="multiple_valid_windows"),
        pytest.param("aa", "aaaa", True, id="multiple_overlapping_matches"),
        # No permutation
        pytest.param("abc", "ccccbbbbaaaa", False, id="no_matching_window"),
        pytest.param("hello", "ooolleoooleh", False, id="repeated_characters_no_match"),
        pytest.param("xyz", "abcdefghijkl", False, id="completely_different_characters"),
        # s1 longer than s2
        pytest.param("abcd", "abc", False, id="s1_longer_than_s2"),
        pytest.param("abcdef", "a", False, id="s1_much_longer_than_s2"),
        # Same characters but wrong frequencies
        pytest.param("aab", "abb", False, id="same_distinct_characters_wrong_counts"),
        pytest.param("aabb", "abab", True, id="same_frequencies_different_order"),
        pytest.param("aabb", "abbb", False, id="one_frequency_mismatch"),
        # Valid match after several invalid windows
        pytest.param("abc", "xxxxxxcab", True, id="match_after_many_invalid_windows"),
        pytest.param("abc", "xxxxxxacb", True, id="match_near_end"),
        pytest.param("aab", "ccccbaaccc", True, id="repeated_pattern_near_end"),
    ],
)
def test_check_permutation(pattern, string, expected):
    """
    Test check_permutation function
    """
    assert contains_permutation(pattern, string) is expected
