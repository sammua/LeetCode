#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-06-11
===================
[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/) | Easy
===================
problem description
===================
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""


class Solution(object):
    # solution 1
    def isValid(self, s):
        # if not s:
        #     return False
        if len(s) % 2 == 1:
            return False
        forward_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        backward_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        tmp = []
        for c in s:
            if c in forward_map:
                tmp.append(c)
            elif c in backward_map:
                if not tmp:
                    return False
                if not tmp.pop() == backward_map[c]:
                    return False
            else:
                return False
        if tmp:
            return False
        else:
            return True


if __name__ == '__main__':

    tests = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}"
    ]
    for t in tests:
        print(t, Solution().isValid(t))

"""tips

"""
