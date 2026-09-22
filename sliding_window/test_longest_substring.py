# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-20 03:01:55
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-20 03:15:11
"""
Tests for the Longest Substring Without Repeating Characters problem.
"""

import pytest
from longest_substring import find_length_longest_substring


@pytest.mark.parametrize(
    "string, expected",
    [
        pytest.param("abcabcbb", 3, id="basic case"),
        pytest.param("bbbbb", 1, id="all characters are the same"),
        pytest.param("pwwkew", 3, id="repeated character after a valid window"),
        pytest.param("abcdef", 6, id="all characters are unique"),
        pytest.param("a", 1, id="single character"),
        pytest.param("", 0, id="empty string"),
        pytest.param("ab", 2, id="two unique characters"),
        pytest.param("aa", 1, id="two identical characters"),
        pytest.param("aba", 2, id="repeated character at the end"),
        pytest.param("abcba", 3, id="palindrome with repeated characters"),
        pytest.param("aab", 2, id="repetition at the beginning"),
        pytest.param("abb", 2, id="repetition at the end"),
        pytest.param("abba", 2, id="repeated character moves the left pointer"),
        pytest.param("tmmzuxt", 5, id="left pointer must not move backward"),
        pytest.param("dvdf", 3, id="repeated character inside the window"),
        pytest.param("anviaj", 5, id="longest substring appears after a repeat"),
        pytest.param("ohvhjdml", 6, id="long unique substring after repetition"),
        pytest.param("aabcde", 5, id="unique substring after initial repetition"),
        pytest.param("abcadef", 6, id="repeat followed by longer substring"),
        pytest.param("abccdef", 4, id="repetition in the middle"),
        pytest.param("abcddefgh", 5, id="repetition splits the string"),
        pytest.param("aaaaab", 2, id="many repeated characters followed by unique"),
        pytest.param("abbbbbc", 2, id="unique characters around repeated block"),
        pytest.param("abcdeafgh", 8, id="repeat near the middle"),
        pytest.param("aAbB", 4, id="case sensitive characters"),
        pytest.param("123123", 3, id="digits"),
        pytest.param("!@#!@", 3, id="special characters"),
        pytest.param("a b c", 3, id="spaces are valid characters"),
    ],
)
def test_find_length_longest_substring(string, expected):
    """
    Test the find_length_longest_substring function.
    """
    assert find_length_longest_substring(string) == expected
