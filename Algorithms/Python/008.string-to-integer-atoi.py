#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-03-19
===================
[8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/description/) | Medium
===================
problem description
===================
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.



Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""


# solution 1
class Solution(object):
    def myAtoi(self, str):
        # del head and tail whitespaces
        s = str.strip()
        # check the sign
        sign = "+"
        if s.startswith("-"):
            sign = "-"
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]
        # ascii to integer
        total = 0
        for c in s:
            num = ord(c) - 48
            if num < 0 or num > 9:
                break
            total = total * 10 + num
        if sign == "-":
            if total > 2147483648:
                return -2147483648
            return -1 * total
        if sign == "+":
            if total > 2147483647:
                return 2147483647
            return total
        return 0
    
    def myAtoi2(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # del head and tail whitespaces
        s = str.strip()
        # check the sign
        sign = 1
        if s.startswith("-"):
            sign = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]
        # ascii to integer
        total = 0
        for c in s:
            num = ord(c) - 48
            if num < 0 or num > 9:
                break
            if total > (INT_MAX - num) / 10:
                return INT_MAX if sign > 0 else INT_MIN
            total = total * 10 + num
        return sign * total


if __name__ == '__main__':

    _list = [
        "- 21432413424",
        "-21432413424",
        "--2313",
        "1",
        "+1",
        "    +012a",
        "   +0 123",
        "2147483648",
        "-2147483648"
    ]
    for a in _list:
        print(a, Solution().myAtoi2(a))


"""tips

"""
