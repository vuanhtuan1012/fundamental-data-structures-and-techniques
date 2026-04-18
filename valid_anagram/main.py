# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-15 08:53:13
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-18 17:00:40
"""
Valid Anagram

Given two strings `source` and `target`,
return True if `target` is an anagram of `source`, and False otherwise.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters exactly once.
"""


def brute_force(source: str, target: str) -> bool:
    """
    Brute Force Solution

    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(source) != len(target):
        return False
    return sorted(source) == sorted(target)


def counting_frequency(source: str, target: str) -> bool:
    """
    Counting Solution

    Time complexity: O(n) where n is the length of source and target
    Space complexity: O(1) or O(k) where k is the number of unique characters
    """
    if len(source) != len(target):
        return False

    char_freq = {}

    for char in source:
        char_freq[char] = char_freq.get(char, 0) + 1

    for char in target:
        if char not in char_freq or char_freq[char] == 0:
            return False
        char_freq[char] -= 1

    return True


def dry_run():
    """
    Dry Run
    """
    print(
        f"brute_force('anagram', 'nagaram'): {brute_force('anagram', 'nagaram')}"
    )  # True
    print(f"brute_force('state', 'tea'): {brute_force('state', 'tea')}")  # False
    print(
        "brute_force('school master', 'the classroom'): "
        f"{brute_force('school master', 'the classroom')}"
    )  # True
    print(f"brute_force('rat', 'car'): {brute_force('rat', 'car')}")  # False
    print(f"counting_frequency('anagram', 'nagaram'): {counting_frequency('anagram', 'nagaram')}")  # True
    print(f"counting_frequency('state', 'tea'): {counting_frequency('state', 'tea')}")  # False
    print(
        "counting_frequency('school master', 'the classroom'): "
        f"{counting_frequency('school master', 'the classroom')}"
    )  # True
    print(f"counting_frequency('rat', 'car'): {counting_frequency('rat', 'car')}")  # False


if __name__ == "__main__":
    dry_run()
