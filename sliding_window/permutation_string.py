# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-22 11:01:53
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-22 13:01:58
"""
Permutation in String
Given two strings s1 and s2, return true if s2 contains a substring that is a permutation of s1, and false otherwise.

Example:

s1 = "ab"
s2 = "eidbaooo"

Output: True
"""


def contains_permutation(pattern: str, string: str) -> bool:
    """
    Returns True if string contains a substring that
    is a permutation of pattern, and False otherwise.
    """
    # check pre-condition
    if len(pattern) > len(string):
        return False

    # count char frequency in pattern
    pattern_chars = {}
    for char in pattern:
        pattern_chars[char] = pattern_chars.get(char, 0) + 1

    left = 0
    window = {}
    matches = 0
    pattern_size = len(pattern)
    for right, char in enumerate(string):
        # add char to window
        window[char] = window.get(char, 0) + 1

        # update matches
        if char in pattern_chars and window[char] == pattern_chars[char]:
            matches += 1

        # keep window size equal to pattern size
        if (right - left + 1) > pattern_size:
            # remove left char, update matches
            left_char = string[left]
            if left_char in pattern_chars and window[left_char] == pattern_chars[left_char]:
                matches -= 1

            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            left += 1

        if matches == len(pattern_chars):
            return True
    return False


def run_examples():
    """
    Run example
    """
    pattern, string = "hello", "ooolleoooleh"
    pattern, string = "ab", "eidbaooo"
    pattern, string = "aab", "abab"
    print(contains_permutation(pattern, string))


if __name__ == "__main__":
    run_examples()
