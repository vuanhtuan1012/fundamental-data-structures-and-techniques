# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-16 09:07:17
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-17 18:24:21
"""
Group Anagrams

Given an array of strings `strings`, group anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters exactly once.

Example 1:
- Input : ["eat", "tea", "tan", "ate", "nat", "bat"]
- Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
"""


def are_anagrams(source: str, target: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    """
    # validate the length of strings
    if len(source) != len(target):
        return False

    # count char frequency in source
    char_freq = {}
    for char in source:
        char_freq[char] = char_freq.get(char, 0) + 1

    # validate char frequency in target
    for char in target:
        if char not in char_freq or char_freq[char] == 0:
            return False

    return True


def brute_force(strings: list[str]) -> list[list[str]]:
    """
    Brute Force Solution

    Time Complexity: O(n^2 * k), where:
    - n is the number of strings and
    - k is the average length of the strings
    Space Complexity: O(n), where:
    - n is the number of strings
    """
    result = []
    used = [False] * len(strings)
    for i, source in enumerate(strings):
        if used[i]:
            continue

        used[i] = True
        group = [source]
        for j in range(i + 1, len(strings)):
            target = strings[j]
            if not used[j] and are_anagrams(source, target):
                group.append(target)
                used[j] = True
        result.append(group)
    return result


def sorting_string(strings: list[str]) -> list[list[str]]:
    """
    Sorting String Solution

    Time Complexity: O(n * k log k), where:
    - n is the number of strings and
    - k is the average length of the strings
    Space Complexity: O(n * k), where:
    - n is the number of strings and
    - k is the average length of the strings
    """
    groups: dict[str, list[str]] = {}
    for string in strings:
        sorted_string = "".join(sorted(string))
        if sorted_string not in groups:
            groups[sorted_string] = []
        groups[sorted_string].append(string)
    return list(groups.values())


def build_string_signature(string: str) -> str:
    """
    Builds a string into a character frequency signature,
    which is a string representation of the frequency of each character in the input string.

    For example, the string "eat" would be converted to
    "a1e1t1" (characters are ordered alphabetically).
    """
    # initialize alphabet frequency dictionary
    alphabet_freq = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}
    alphabet_freq.update({chr(i): 0 for i in range(ord("A"), ord("Z") + 1)})

    for char in string:
        if char in alphabet_freq:
            alphabet_freq[char] = alphabet_freq[char] + 1
    return "".join([f"{char}{freq}" for char, freq in alphabet_freq.items() if freq > 0])


def counting_frequency(strings: list[str]) -> list[list[str]]:
    """
    Counting Frequency Solution

    Time Complexity: O(n * k), where:
    - n is the number of strings and
    - k is the average length of the strings
    Space Complexity: O(n * k), where:
    - n is the number of strings and
    - k is the average length of the strings
    """
    groups: dict[str, list[str]] = {}
    for string in strings:
        signature = build_string_signature(string)
        if signature not in groups:
            groups[signature] = []
        groups[signature].append(string)
    return list(groups.values())


def run_examples():
    """
    Run examples
    """
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"       brute force: {brute_force(strings)}")
    print(f"    sorting string: {sorting_string(strings)}")
    print(f"counting frequency: {counting_frequency(strings)}")


if __name__ == "__main__":
    run_examples()
