#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-05-24
===================
[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/) | Easy
===================
problem description
===================
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    # solution 1
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for _str in strs:
                if _str[i] != c:
                    return shortest[:i]
        return shortest


if __name__ == '__main__':

    tests = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"]
    ]
    for t in tests:
        print(t, Solution().longestCommonPrefix(t))

"""tips

"""
