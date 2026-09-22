# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-21 20:55:28
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-22 11:03:19
"""
Longest Repeating Character Replacement

Given a string s consisting of uppercase English letters and an integer k,
you can replace at most k characters in the string with any other uppercase letter.

Return the length of the longest substring containing only
one distinct character after performing at most k replacements.

Example:

s = "AABABBA"
k = 1

Output: 4
"""


def find_longest_repeating_substring(string: str, k: int) -> int:
    """
    Returns the length of the longest substring containing only
    one distinct character after performing at most k replacements.
    """
    # check pre-condition
    if not all("A" <= char <= "Z" for char in string):
        raise ValueError("String must contains only uppercase letters!")

    left = 0
    max_length = 0
    char_count = {}
    for right, char in enumerate(string):
        # add char to char_count
        char_count[char] = char_count.get(char, 0) + 1

        # update left position, char_count
        # window_size = right - left + 1
        # max_frequency = max(char_count.values()) - O(26) = O(1)
        while (right - left + 1) - max(char_count.values()) > k:
            left_char = string[left]
            char_count[left_char] -= 1

            if char_count[left_char] == 0:
                del char_count[left_char]

            left += 1

        # update max_length
        max_length = max(max_length, right - left + 1)
    return max_length


def run_examples():
    """
    Run examples
    """
    string, k = "AABABBCC", 1
    print(find_longest_repeating_substring(string, k))


if __name__ == "__main__":
    run_examples()
