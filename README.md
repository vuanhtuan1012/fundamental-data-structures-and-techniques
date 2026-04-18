# Introduction to Fundamental Data Structures and Techniques  <!-- omit in toc -->

This repository is a structured, comprehensive collection of notes designed based on the [Introduction to Fundamental Data Structures and Techniques](https://www.coursera.org/learn/packt-introduction-to-fundamental-data-structures-and-techniques-9zdns) course offered on Coursera.

- [Arrays, String: Manipulation \& Hashing](#arrays-string-manipulation--hashing)
  - [Two Sum](#two-sum)
  - [Contains Duplicate](#contains-duplicate)
  - [Valid Anagram](#valid-anagram)
  - [Group Anagrams](#group-anagrams)
  - [Top Frequent Elements](#top-frequent-elements)
- [Resources](#resources)


## Arrays, String: Manipulation & Hashing

### Two Sum

- **Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

  You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

  *For example:*
  - Input: `nums = [2, 7, 11, 15]`, `target = 9`
  - Output: `[0, 1]` since the sum of the first and second elements is `9`.
- **Approaches:**
  - *Brute Force:* The algorithm evaluates every pair of elements in the array and returns the indices of the first pair whose sum matches the `target`. This brute force strategy leads to a quadratic time complexity `O(n^2)`.
  - *Two Pointers:* The algorithm begins by sorting the arrayin ascending order. It then applies a two-pointer technique: one pointer starts at the beginning of the array, the other at the end.
    - If the sum of the values at these positions exceeds the target, the right pointer is moved left;
    - If the sum is below the target, the left pointer is moved right.
    - When the sum matches the target, the indices of the corresponding pair is returned.

    The sorting step dominates the runtime, giving the algorithm a time complexity `O(n log n)`.
  - *Hash Map:* The algorithm leverages a hash table, where both lookup and insertion take `O(1)` on average. It iterates through each element in the array, checks whether the element's component exists in the hash table.
    - If the complement is present, the indices of the corresponding pair is returned.
    - If not, the current element is inserted.

    Since both lookup and insertion takes `O(1)` in average, the algorithm only needs a single pass. This keeps the runtime at `O(n)`.
- **Implementation:** The implementation and test cases are provided in the [two sum](./two_sum/) directory.

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

### Top Frequent Elements

- **Problem:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

  For example:
  - Input: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2`
  - Output: `[1, 2]` since the frequencies of elements are: 1 (3), 2 (2), 3 (1), so the two most frequent elements are `[1, 2]`.
  - Input: `nums = [2, 2, 2, 5, 5, 7]`, `k = 3`
  - Output: `[2, 5, 7]`.
  - Input: `nums = [1]`, `k = 1`
  - Output: `[1]`
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`


## Resources
1. [Master Data Structures and Algorithms Interviews: Ace Leetcode Blind 75](https://github.com/PacktPublishing/-Master-Data-Structures-and-Algorithms-Interviews---Ace-Leetcode-Blind-75-/tree/main)
2. [DSA Sheet: Blind 75](https://dsa.unwiredlearning.com/)