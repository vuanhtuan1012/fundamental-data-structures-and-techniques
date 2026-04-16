# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-16 09:07:17
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-16 12:11:00
"""
Group Anagrams

Given an array of strings `strings`, group anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters exactly once.

Example 1:
- Input: strings = ["eat","tea","tan","ate","nat","bat"]
- Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


def is_anagram(source: str, target: str) -> bool:
    """
    Checks if the source string is an anagram of the target string
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
    Space Complexity: O(n * k), where:
    - n is the number of strings and
    - k is the average length of the strings
    """
    res = []
    added = set()
    for i, source in enumerate(strings):
        if source in added:
            continue

        added.add(source)
        temp = [source]
        for j in range(i + 1, len(strings)):
            target = strings[j]
            if is_anagram(source, target):
                temp.append(target)
                added.add(target)
        res.append(temp)
    return res


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
    string_map: dict[str, list[str]] = {}
    for string in strings:
        sorted_string = "".join(sorted(string))
        if sorted_string not in string_map:
            string_map[sorted_string] = []
        string_map[sorted_string].append(string)
    return list(string_map.values())


def get_frequency_string(string: str) -> str:
    """
    Converts a string into a frequency string,
    which is a string representation of the frequency of each character in the input string.

    For example, the string "eat" would be converted to "a1e1t1".
    """
    # create a char frequency map
    char_freq = {chr(c): 0 for c in range(ord("a"), ord("z") + 1)}
    char_freq.update({chr(c): 0 for c in range(ord("A"), ord("Z") + 1)})

    for char in string:
        char_freq[char] = char_freq[char] + 1
    return "".join([f"{char}{freq}" for char, freq in char_freq.items() if freq > 0])


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
    freq_map: dict[str, list[str]] = {}
    for string in strings:
        freq_string = get_frequency_string(string)
        if freq_string not in freq_map:
            freq_map[freq_string] = []
        freq_map[freq_string].append(string)
    return list(freq_map.values())


def dry_run():
    """
    Dry Run
    """
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(brute_force(strings))


if __name__ == "__main__":
    dry_run()
