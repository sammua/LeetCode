#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Filename: 001.two_sum
@Date    : 2016/12/10 19:21
@Author  : bingo
@Software: PyCharm
"""

"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.
You may assume that each input would have exactly one solution.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        find_dic = {}
        for i, num in enumerate(nums):
            tmp = target - num
            if tmp in find_dic:
                return [find_dic[tmp], i]
            find_dic[num] = i
        return []


if __name__ == '__main__':
    nums = [0, 4, 1, 0]
    target = 0
    print(Solution().twoSum(nums, target))

"""
tips:
dict.get(key) return dict[key] if key in dict else return false.
so if dict[key] is 0, "if dict.get(key)" return 0, false
"""