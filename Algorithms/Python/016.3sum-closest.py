#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-05-29
===================
[16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/description/) | Medium
===================
problem description
===================
Given an array nums of n integers and an integer target, find three integers
in nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    # solution 1
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 0
        nums.sort()
        closest = sum(nums[:3])
        for i, v in enumerate(nums[:-2]):
            if i > 1 and v == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = v + nums[l] + nums[r]
                if total == target:
                    return target
                if abs(target-total) < abs(target-closest):
                    closest = total
                if total < target:
                    l += 1
                else:
                    r -= 1
        return closest


if __name__ == '__main__':

    tests = [
        ([-1, 2, 1, -4], 1)
    ]
    for t in tests:
        print(t, Solution().threeSumClosest(t[0], t[1]))

"""tips
solution 1: https://leetcode.com/problems/3sum-closest/discuss/7883/
C++-solution-O(n2)-using-sort
"""
