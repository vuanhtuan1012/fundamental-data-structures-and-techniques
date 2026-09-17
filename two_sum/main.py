# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-13 09:07:13
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-17 11:11:00
"""
Two Sum

Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

NOT_FOUND = [-1, -1]


def brute_force(nums: list[int], target: int) -> list[int]:
    """
    Brute Froce Solution

    Time complexity: O(n^2)
    Space complexity: O(1)

    Returns indices of the two numbers in `nums` such that
    they add up to `target`
    """

    no_elements = len(nums)
    for i in range(no_elements - 1):
        for j in range(i + 1, no_elements):
            if nums[i] + nums[j] == target:
                return [i, j]
    return NOT_FOUND


def two_pointers(nums: list[int], target: int) -> list[int]:
    """
    Two Pointers Solution

    Time complexity: O(n log n) due to sorting
    Space complexity: O(n) due to sorting

    Returns indices of the two numbers in `nums` such that
    they add up to `target`
    """

    index_num = list(enumerate(nums))
    index_num.sort(key=lambda x: x[1])
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = index_num[left][1] + index_num[right][1]
        if current_sum == target:
            return [index_num[left][0], index_num[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return NOT_FOUND


def hash_map(nums: list[int], target: int) -> list[int]:
    """
    Hash Map Solution

    Time complexity: O(n)
    Space complexity: O(n)

    Returns indices of the two numbers in `nums` such that
    they add up to `target`
    """

    num_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [num_index[complement], i]
        num_index[num] = i
    return NOT_FOUND


def run_examples():
    """
    Run examples
    """
    nums = [5, 5, 5]
    target = 10
    print(f"nums: {nums}")
    print(f"target: {target}")
    print(f"result: {brute_force(nums, target)}")
    print(f"result: {two_pointers(nums, target)}")
    print(f"result: {hash_map(nums, target)}")


if __name__ == "__main__":
    run_examples()
