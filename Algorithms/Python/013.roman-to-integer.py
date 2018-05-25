#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-05-24
===================
[13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/) | Easy
===================
problem description
===================
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and
M.

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
as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six
instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be
within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution(object):
    # solution 1
    def romanToInt(self, s):
        total = 0
        for c in s:
            if c == "M":
                total += 1000
            if c == "D":
                total += 500
            if c == "C":
                total += 100
            if c == "L":
                total += 50
            if c == "X":
                total += 10
            if c == "V":
                total += 5
            if c == "I":
                total += 1
        if s.count("CM") > 0:
            total -= 200
        if s.count("CD") > 0:
            total -= 200
        if s.count("XC") > 0:
            total -= 20
        if s.count("XL") > 0:
            total -= 20
        if s.count("IX") > 0:
            total -= 2
        if s.count("IV") > 0:
            total -= 2
        return total


if __name__ == '__main__':

    tests = [
        "III",
        "IV",
        "IX",
        "LVIII",
        "MCMXCIV"
    ]
    for t in tests:
        print(t, Solution().romanToInt(t))

"""tips

"""
