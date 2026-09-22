# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-20 02:33:42
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-20 18:14:59
"""
Longest Substring Without Repeating Characters

Given a string `s`,
find the length of the longest substring without repeating characters.

Example:
s = "abcabcbb"
abccdef
abbcc
abba
abcca
Output: 3
"""

def find_length_longest_substring(string: str) -> int:
    """
    Returns the length of the longest substring without repeating characters
    """
    max_length = 0
    left = 0
    last_seen = {}
    for right, char in enumerate(string):
        if char in last_seen:
            # update left position
            left = max(last_seen[char] + 1, left)

        # update last seen
        last_seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length



def run_examples():
    """
    Runs examples
    """
    string = "aAbB"
    print(find_length_longest_substring(string))


if __name__ == "__main__":
    run_examples()



















def find_length_longest_substring_1(string: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    """
    left = 0
    last_seen = {}
    longest = 0
    for right, char in enumerate(string):
        if char in last_seen:
            # update left position
            left = max(left, last_seen[char] + 1)

        # update last seen and the longest length
        last_seen[char] = right
        longest = max(longest, right - left + 1)

    return longest