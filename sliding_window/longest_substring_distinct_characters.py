# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-20 03:36:08
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-21 23:00:53
"""
Longest Substring with At Most K Distinct Characters
Given a string s and an integer k,
find the length of the longest substring that contains at most k distinct characters.

Example:

s = "eceba"
k = 2

Output: 3
"""


def find_length_longest_substring(string: str, k: int) -> int:
    """
    Returns the length of the longest substring that contains at most k distisct characters
    """
    left = 0
    max_length = 0
    char_count = {}
    for right, char in enumerate(string):
        # update char_count
        char_count[char] = char_count.get(char, 0) + 1

        # update left position
        while len(char_count) > k:
            left_char = string[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        # update max length
        max_length = max(max_length, right - left + 1)
    return max_length


def run_examples():
    """
    Run example
    """
    string, k = "eceba", 2
    print(find_length_longest_substring(string, k))


if __name__ == "__main__":
    run_examples()
