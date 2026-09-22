# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-19 17:28:11
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-19 17:48:37
"""
Given an integer array `nums` and an integer `k`,
return an array containing the average of every contiguous subarray of exactly `k` elements.

Suppose: 1 <= k <= len(nums)
"""


def find_averages(nums: list[int], k: int) -> list[float]:
    """
    Returns the average of every contiguous subarrays
    """
    # check pre-condition
    if k < 1 or k > len(nums):
        raise ValueError("k must be within the range of 1 and the length of nums!")

    current_sum = sum(nums[:k])
    left = 0
    averages = [current_sum / k]
    for right in range(k, len(nums)):
        # update current sum
        current_sum -= nums[left]
        left += 1
        current_sum += nums[right]

        # update averages
        averages.append(current_sum / k)
    return averages


def run_examples():
    """
    Run examples
    """
    nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    expected = [2.2, 2.8, 2.4, 3.6, 2.8]
    print(find_averages(nums, k) == expected)


if __name__ == "__main__":
    run_examples()
