# Introduction to Fundamental Data Structures and Techniques  <!-- omit in toc -->

This repository is a structured, comprehensive collection of notes designed based on the [Introduction to Fundamental Data Structures and Techniques](https://www.coursera.org/learn/packt-introduction-to-fundamental-data-structures-and-techniques-9zdns) course offered on Coursera.

- [Arrays, String: Manipulation \& Hashing](#arrays-string-manipulation--hashing)
  - [Two Sum](#two-sum)
  - [Contains Duplicate](#contains-duplicate)
  - [Valid Anagram](#valid-anagram)
  - [Group Anagrams](#group-anagrams)
- [Resources](#resources)


## Arrays, String: Manipulation & Hashing

### Two Sum

- **Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

  You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
- **Approaches:**
  - *Brute Force:* `O(n^2)`
  - *Two Pointers:* `O(n log n)`
  - *Hash Map:* `O(n)`

### Contains Duplicate

- **Problem:** Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.
- **Approaches:**
  - *Brute Force:* `O(n^2)`
  - *Sorting:* `O(n log n)`
  - *Hash Set:* `O(n)`

### Valid Anagram

- **Problem:** Given two strings `source` and `target`, return `True` if `target` is an anagram of `source`, and `False` otherwise.

  An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

  *For example:*
  - `is_anagram("anagram", "nagaram") = True`
  - `is_anagram("state", "tea") = False`
  - `is_anagram("school master", "the classroom") = True`
- **Approaches:**
  - *Brute Force:* `O(n log n)`
  - *Counting Frequency (Hash Map):* `O(max(n, m))` where `n` and `m` are the lengths of `source` and `target`.

### Group Anagrams

- **Problem:** Given an array of strings `strings`, group the anagrams together. You can return the answer in any order.

  An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

  *For example:*
  - Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
  - Output: `[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]`
- **Approaches:**
  - *Brute Force:* `O(n^2 * k)`, where:
    - `n` is the number of strings and
    - `k` is the average length of the strings.
  - *Sorting String:* `O(n * k log k)`, where:
    - `n` is the number of strings and
    - `k` is the average length of the strings.
  - *Counting Frequency:* `O(n * k)`, where:
    - `n` is the number of strings and
    - `k` is the average length of the strings.


## Resources
1. [Master Data Structures and Algorithms Interviews: Ace Leetcode Blind 75](https://github.com/PacktPublishing/-Master-Data-Structures-and-Algorithms-Interviews---Ace-Leetcode-Blind-75-/tree/main)
2. [DSA Sheet: Blind 75](https://dsa.unwiredlearning.com/)