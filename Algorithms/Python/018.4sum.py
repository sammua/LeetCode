#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-06-05
===================
[18. 4Sum](https://leetcode.com/problems/4sum/description/) | Medium
===================
problem description
===================
Given an array nums of n integers and an integer target, are there elements a,
b, c, and d in nums such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    # solution 1
    def fourSum(self, nums, target):
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        out = set()
        for i in range(length-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if sum(nums[i:i+4]) > target:
                break
            if nums[i] + sum(nums[-3:]) < target:
                continue
            for j in range(i+1, length-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + sum(nums[j:j+3]) > target:
                    break
                if nums[i] + nums[j] + sum(nums[-2:]) < target:
                    continue
                l = j + 1
                r = length - 1
                while l < r:
                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if cur_sum < target:
                        l += 1
                    elif cur_sum > target:
                        r -= 1
                    else:
                        out.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1

        return map(list, out)


if __name__ == '__main__':

    tests = [
        ([1, 0, -1, 0, -2, 2], 0)
    ]
    for t in tests:
        print(t, Solution().fourSum(t[0], t[1]))

"""tips

"""
