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

### solution 1 N*N
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         length = len(s)
#         longest_begin = 0
#         max_len = 1
#         table = [[False for i in range(length)] for i in range(length)]
#         for i in range(length):
#             table[i][i] = True
#         for i in range(length-1):
#             if s[i] == s[i+1]:
#                 table[i][i+1] = True
#                 longest_begin = i
#                 max_len = 2
#
#         for le in range(3, length+1):
#             for i in range(length-le+1):
#                 j = i + le - 1
#                 if s[i] == s[j] and table[i+1][j-1]:
#                     table[i][j] = True
#                     longest_begin = i
#                     max_len = le
#         # print(longest_begin, longest_begin + max_len - 1)
#         return s[longest_begin:longest_begin + max_len]

## solutino 2
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_center(s, border_1, border_2):
            left = border_1
            right = border_2
            n = len(s)
            while left>=0 and right<=n-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        n = len(s)
        if n == 0:
            return ""
        longest = s[0]
        for i in range(n-1):
            p1 = expand_center(s, i, i)
            if len(p1) >= len(longest):
                longest = p1

            p2 = expand_center(s, i, i+1)
            if len(p2) >= len(longest):
                longest = p2
        return longest




if __name__ == '__main__':
    s = ''
    s = 'babad'
    s = 'abaaba'
    # s = 'abcda'
    s = 'babad'
    print(Solution().longestPalindrome(s))


"""tips

"""