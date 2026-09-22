# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-09-19 15:35:28
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-09-19 17:25:59
"""
Maximum Sum Subarray of Size K

Given an integer array `nums` and an integer `k`,
find the maximum sum of any contiguous subarray containing exactly `k` elements.

Suppose: 1 <= k <= len(nums)
"""


def find_max_sum_subarray(nums: list[int], k: int) -> int:
    """
    Find the maximum sum of a contiguous subarray of size k.
    :param nums: List of integers
    :param k: Size of the subarray, 1 <= k <= len(nums)
    :return: Maximum sum of a contiguous subarray of size k
    """
    # check pre-condition
    if k < 1 or k > len(nums):
        raise ValueError("`k` must be within the range of 1 and the array size!")

    left = 0
    max_sum = sum(nums[:k])
    current_sum = max_sum
    for right in range(k, len(nums)):
        # update current sum and left position
        current_sum = current_sum - nums[left]
        left += 1
        current_sum += nums[right]

        # update max sum
        max_sum = max(current_sum, max_sum)
    return max_sum


def run_example():
    """
    Run example for the function
    """
    nums, k, _ = [2, 1, 5, 1, 3, 2], 3, 9
    print(nums, k)
    print(find_max_sum_subarray(nums, k))


if __name__ == "__main__":
    run_example()
