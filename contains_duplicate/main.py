# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-14 16:31:25
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-17 11:34:11
"""
Contains Duplicate

Given an integer array `nums`, return `True` if any value appears at least twice
in the array, and return `False` if every element is distinct.
"""


def brute_force(nums: list[int]) -> bool:
    """
    Brute Force Solution

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if num == nums[j]:
                return True
    return False


def sorting(nums: list[int]) -> bool:
    """
    Sorting Solution

    Time complexity: O(n log n)
    Space complexity: O(1) or O(n) depending on the sorting algorithm used
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


def hash_set(nums: list[int]) -> bool:
    """
    Hash Set Solution

    Time complexity: O(n)
    Space complexity: O(n)
    """
    visited = set()
    for num in nums:
        if num in visited:
            return True
        visited.add(num)
    return False


def run_examples():
    """
    Run examples
    """
    nums = [1, 2, 3, 1, 5]
    print(f"Brute Force: {brute_force(nums)}")
    print(f"Sorting: {sorting(nums)}")
    print(f"Hash Set: {hash_set(nums)}")


if __name__ == "__main__":
    run_examples()
