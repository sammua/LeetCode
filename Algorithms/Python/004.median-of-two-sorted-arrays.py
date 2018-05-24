#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2016-12-14
===================
[4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard
===================
problem description
===================
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution(object):
    # solution 1
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        mid = (m + n) / 2
        i, j = 0, 0
        last, current = 0, 0
        while(i + j <= mid):
            last = current
            if i == m:
                current = nums2[j]
                j += 1
            elif j == n:
                current = nums1[i]
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    current = nums1[i]
                    i += 1
                else:
                    current = nums2[j]
                    j += 1
        # if (m + n) % 2 == 0:
        #     return (last + current) / 2.0
        # else:
        #     return current / 1.0
        return last, current


if __name__ == '__main__':
    a = [1, 2]
    b = [3, 4]
    a = [1, 3]
    b = [2]

    print(Solution().findMedianSortedArrays(a, b))


"""tips

"""
