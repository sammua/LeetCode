#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-03-15
===================
[Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Easy
===================
problem description
===================
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""


# solution 1
class Solution(object):
    def reverse(self, x):
        out = int(str(abs(x))[::-1])
        if len(bin(out)) > 33:
            return 0
        if x < 0:
            return -1 * out
        return out


if __name__ == '__main__':

    print(Solution().reverse(-120))
    print(Solution().reverse(2147483648))


"""tips

"""
