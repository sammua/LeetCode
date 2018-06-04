#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-06-04
===================
[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/) | Medium
===================
problem description
===================
Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in
any order you want.
"""


class Solution(object):
    # solution 1
    def letterCombinations(self, digits):
        s_dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if len(digits) < 1:
            return []
        elif len(digits) == 1:
            return s_dic[digits]
        start = s_dic[digits[0]]
        end = list(start)

        def add_new(old_list, new_list):
            out_list = []
            for old in old_list:
                for new in new_list:
                    out_list.append(old+new)
            return out_list
        for digit in digits[1:]:
            end = add_new(start, s_dic[digit])
            start = list(end)
        return end


if __name__ == '__main__':

    tests = [
        '23'
    ]
    for t in tests:
        print(t, Solution().letterCombinations(t))

"""tips

"""
