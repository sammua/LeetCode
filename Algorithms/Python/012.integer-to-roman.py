#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-05-24
===================
[12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/description/) | Medium
===================
problem description
===================
Roman numerals are represented by seven different symbols: I, V, X, L, C, D
and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added
together. Twelve is written as, XII, which is simply X + II. The number twenty
 seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be
within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution(object):
    # solution 1
    def intToRoman(self, num):
        """按照不同位置定制不同的符号
        t: 千分位
        h: 百分位
        d: 十分位
        u: 个位
        """
        out = ""
        symbol = {
            1000: ("M"),
            100: ("C", "D", "M"),
            10: ("X", "L", "C"),
            1: ("I", "V", "X")
        }
        for divisor in (1000, 100, 10, 1):
            pos = num / divisor % 10
            if pos == 0:
                continue
            if pos < 4:
                _str = symbol[divisor][0] * pos
            elif pos == 4:
                _str = symbol[divisor][0] + symbol[divisor][1]
            elif pos == 5:
                _str = symbol[divisor][1]
            elif pos < 9:
                _str = symbol[divisor][1] + symbol[divisor][0] * (pos - 5)
            elif pos == 9:
                _str = symbol[divisor][0] + symbol[divisor][2]
            out += _str
        return out


if __name__ == '__main__':

    tests = [
        3,
        4,
        9,
        58,
        1994
    ]
    for t in tests:
        print(t, Solution().intToRoman(t))

"""tips

"""
