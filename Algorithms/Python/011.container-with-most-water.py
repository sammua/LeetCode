#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-05-24
===================
[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/) | Medium
===================
problem description
===================
Given n non-negative integers a1, a2, ..., an, where each represents a point at
 coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
 line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
 forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    # solution 1
    def maxArea(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_area = max(max_area, (j-i)*min(height[i], height[j]))
        return max_area

    # solution 2
    def maxArea2(self, height):
        # 从两边想中间夹
        max_area = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            max_area = max(max_area, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == '__main__':

    tests = [
        [1, 2, 3, 4, 5, 6, 7],
        [5, 1, 2, 3, 4, 5, 7]
    ]
    for t in tests:
        print(t, Solution().maxArea2(t))

"""tips

"""
