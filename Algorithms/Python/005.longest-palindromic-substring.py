#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Filename: 005.longest-palindromic-substring
@Date    : 2016/12/15 17:18
@Author  : bingo
@Software: PyCharm
"""


"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        target_str, current_str = "", ""
        for i, e in enumerate(s):
            if len(current_str)


if __name__ == '__main__':

    print(Solution().)


"""tips

"""