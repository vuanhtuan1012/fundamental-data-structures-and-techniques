## Sliding Window

- Level 1: 1-3
- Level 2: 4-6
- Level 3: 7-9
- Level 4: 10-12

### 1. Maximum Sum Subarray of Size K

Given an integer array `nums` and an integer `k`, find the maximum sum of any contiguous subarray containing exactly `k` elements.

*Example:*

```
nums = [2, 1, 5, 1, 3, 2]
k = 3

Output: 9
```

---

### 2. Average of Subarrays of Size K

Given an integer array `nums` and an integer `k`, return an array containing the average of every contiguous subarray of exactly `k` elements.

*Example:*

```
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

Output: [2.2, 2.8, 2.4, 3.6, 2.8]
```

---

### 3. Maximum Number of Vowels in a Substring of Given Length

Given a string `s` and an integer `k`, find the maximum number of vowels contained in any substring of length `k`.

The vowels are `a`, `e`, `i`, `o`, and `u`.

*Example:*

```
s = "abciiidef"
k = 3

Output: 3
```

---

### 4. Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating characters.

*Example:*

```
s = "abcabcbb"

Output: 3
```

---

### 5. Longest Substring with At Most K Distinct Characters

Given a string `s` and an integer `k`, find the length of the longest substring that contains at most `k` distinct characters.

*Example:*

```
s = "eceba"
k = 2

Output: 3
```

---

### 6. Longest Repeating Character Replacement

Given a string `s` consisting of uppercase English letters and an integer `k`, you can replace at most `k` characters in the string with any other uppercase letter.

Return the length of the longest substring containing only one distinct character after performing at most `k` replacements.

*Example:*

```
s = "AABABBA"
k = 1

Output: 4
```

---

### 7. Permutation in String

Given two strings `s1` and `s2`, return `true` if `s2` contains a substring that is a permutation of `s1`, and `false` otherwise.

*Example:*

```
s1 = "ab"
s2 = "eidbaooo"

Output: True
```

---

### 8. Find All Anagrams in a String

Given two strings `s` and `p`, return an array containing the starting indices of all substrings of `s` that are anagrams of `p`.

*Example:*

```
s = "cbaebabacd"
p = "abc"

Output: [0, 6]
```

---

### 9. Minimum Size Subarray Sum

Given a positive integer `target` and an array of positive integers `nums`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`.

If no such subarray exists, return `0`.

*Example:*

```
target = 7
nums = [2, 3, 1, 2, 4, 3]

Output: 2
```

---

### 10. Minimum Window Substring

Given two strings `s` and `t`, return the shortest substring of `s` that contains all the characters in `t`, including duplicate characters.

If no such substring exists, return an empty string.

*Example:*

```
s = "ADOBECODEBANC"
t = "ABC"

Output: "BANC"
```

---

### 11. Longest Subarray of 1's After Deleting One Element

Given a binary array `nums`, you must delete exactly one element from the array.

Return the length of the longest non-empty subarray containing only `1`s after the deletion.

*Example:*

```
nums = [1,1,0,1]

Output: 3
```

---

### 12. Fruit Into Baskets

You are given an integer array `fruits`, where `fruits[i]` represents the type of fruit in the `i`-th tree.

You have two baskets, and each basket can hold only one type of fruit. Starting from any tree, you must collect exactly one fruit from every tree while moving to the right.

Return the maximum number of fruits you can collect.

*Example:*

```
fruits = [1,2,1]

Output: 3
```
