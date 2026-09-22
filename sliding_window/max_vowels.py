# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-19 18:05:13
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-19 19:23:05
"""
Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k,
find the maximum number of vowels contained in any substring of length k.

Suppose: 1 <= k <= len(s) <= 10^5

The vowels are a, e, i, o, and u.
"""


def find_max_vowels(string: str, k: int) -> int:
    """
    Returns the maximum number of vowels contained in any substring
    """
    # check pre-condition
    if k < 1 or k > len(string):
        raise ValueError("k must be within the range of 1 and the length of the string!")

    # declare vowels
    vowels = set("aeiou")

    left = 0
    max_vowels_count = 0
    current_vowels_count = 0
    for right, char in enumerate(string):
        if right - left + 1 == k + 1:
            # update current number of vowels and left position
            if string[left] in vowels:
                current_vowels_count -= 1
            left += 1

        if char in vowels:
            current_vowels_count += 1
        if right - left + 1 == k:
            max_vowels_count = max(max_vowels_count, current_vowels_count)
    return max_vowels_count


def run_examples():
    """
    Run examples
    """
    string, k = "abciiidef", 3
    string, k = "xx", 3
    print(find_max_vowels(string, k))


if __name__ == "__main__":
    run_examples()
