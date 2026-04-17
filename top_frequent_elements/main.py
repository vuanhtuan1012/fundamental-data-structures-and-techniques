# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-04-17 17:23:18
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-04-17 19:51:59
"""
Top Frequent Elements

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
You may return the answer in any order.
"""


def get_top_frequent_elements(nums: list[int], k: int) -> list[int]:
    """
    Returns the k most frequent elements in the input list

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # count the frequency of each element
    ele_freq = {}
    for ele in nums:
        ele_freq[ele] = ele_freq.get(ele, 0) + 1

    # create a bucket to group elements by their frequency
    bucket: list[list[int]] = [[] for _ in range(len(nums))]
    for ele, freq in ele_freq.items():
        bucket[freq - 1].append(ele)

    # collect the top k frequent elements from the bucket
    top_frequent_elements = []
    for elements in reversed(bucket):
        if not elements:
            continue
        for ele in elements:
            if len(top_frequent_elements) == k:
                return top_frequent_elements
            top_frequent_elements.append(ele)
    return top_frequent_elements


def dry_run():
    """
    Dry Run
    """
    nums = [1, 1, 2, 2, 2, 3]
    k = 4
    print(get_top_frequent_elements(nums, k))


if __name__ == "__main__":
    dry_run()
