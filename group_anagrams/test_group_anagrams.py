# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-16 09:27:51
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-16 12:08:16
"""
Test cases for the Group Anagrams problem
"""

import pytest

from main import brute_force, sorting_string, counting_frequency

ARGS = {
    "argnames": ("strings", "expected"),
    "argvalues": (
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        (["hello"], [["hello"]]),
        ([], []),
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
        (["abc", "bca", "cab", "cba"], [["abc", "bca", "cab", "cba"]]),
        (["eat", "tea", "eat"], [["eat", "tea", "eat"]]),
        (["", "", "a"], [["", ""], ["a"]]),
        (["Eat", "tEa", "ate"], [["Eat", "tEa"], ["ate"]]),
        (["aab", "aba", "baa", "aa"], [["aab", "aba", "baa"], ["aa"]]),
    ),
    "ids": (
        "Basic Case",
        "Single Word",
        "Empty List",
        "No Anagrams",
        "All Anagrams",
        "Duplicate Words",
        "Empty Strings",
        "Case Sensitivity",
        "Different Lengths",
    ),
}


def normalize(nested_list: list[list[str]]) -> list[list[str]]:
    """
    Normalizes a nested list of strings by sorting the inner lists and then sorting the outer list.
    """
    sorted_sublists = []
    for sublist in nested_list:
        sorted_sublists.append(sorted(sublist))
    return sorted(sorted_sublists)


@pytest.mark.parametrize(**ARGS)
def test_brute_force(strings, expected):
    """
    Test the Brute Force solution
    """
    assert normalize(brute_force(strings)) == normalize(expected)


@pytest.mark.parametrize(**ARGS)
def test_sorting_string(strings, expected):
    """
    Test the Sorting String solution
    """
    assert normalize(sorting_string(strings)) == normalize(expected)


@pytest.mark.parametrize(**ARGS)
def test_counting_frequency(strings, expected):
    """
    Test the Counting Frequency solution
    """
    assert normalize(counting_frequency(strings)) == normalize(expected)
