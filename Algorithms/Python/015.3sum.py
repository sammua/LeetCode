#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-05-25
===================
[15. 3Sum](https://leetcode.com/problems/3sum/description/) | Medium
===================
problem description
===================
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    # solution 1  Time Limit Exceeded
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        out = set()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                ans = - (nums[i] + nums[j])
                if ans in nums[j+1:]:
                    out.add((nums[i], nums[j], ans))
        return map(list, out)

    # solution 2 Time Limit Exceeded
    def threeSum2(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        print nums
        out = set()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            for j in range(i + 1, len(nums) - 1):
                ans = - (nums[i] + nums[j])
                print i, j, nums[i], nums[j]
                if nums[j] > ans:
                    break
                if ans in nums[j + 1:]:
                    out.add((nums[i], nums[j], ans))
        return map(list, out)

    # solution 3
    def threeSum3(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        out = set()
        for i, v in enumerate(nums[:-2]):
            if v > 0:
                return map(list, out)
            if i >= 1 and v == nums[i-1]:
                continue
            # 在确定v的情况下, 考虑其他两个的值
            d = {}
            for e in nums[i+1:]:
                if e not in d:
                    d[-v-e] = 1
                else:
                    out.add((v, -v-e, e))
        return map(list, out)


if __name__ == '__main__':

    tests = [
        [-1, 0, 1, 2, -1, -4],
    ]
    for t in tests:
        print(t, Solution().threeSum3(t))

"""tips
对于 r0, r1, r2( r0 + r1 + r2 = 0)
在确定一个数值(r0)的前提下, 剩下的一个数为r1, 一个数为 (-r0 - r1)
二层循环的循环数(r1)为, 建立r2的词典, 记录能匹配到的值 -v-e

相当于假象 遇到的每一个 r1, 都会有一个与 r0, r1对应 的r2 (-r0-r1)

"""
