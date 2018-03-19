#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2016-12-11
===================
[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium
===================
problem description
===================
Given a string, find the length of the longest substring without repeating
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
# solution 1 (forword direction)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #:type s: str
        #:rtype: int
        target_start, current_start = 0, 0
        target_end = 1
        target_len, current_len = 1, 1
        current_str = ""
        for i, c in enumerate(s):
            if c in current_str:
                current_len = i - current_start
                if target_len < current_len:
                    target_start = current_start
                    target_end = i
                    target_len = target_end - target_start
                current_str = c
                current_start = i
            else:
                current_str += c
        current_len = len(s) - current_start
        if target_len < current_len:
            target_start = current_start
            target_end = len(s)
        return [target_start, target_end, s[target_start:target_end]]
"""


# solution 2
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        #:type s: str
        #:rtype: int
        """
        longest = 0
        current_str = ""
        for i, c in enumerate(s):
            if c in current_str:
                longest = max(longest, len(current_str))
                current_str = current_str[current_str.index(c)+1:] + c
            else:
                current_str += c
        return max(longest, len(current_str)), current_str


if __name__ == '__main__':
    s = "abcabcbb"
    s = "bbbbb"
    s = "abcdeao"
    s = "abcabcbb"
    s = "jbpnbwwd"
    s = "c"
    s = "abba"
    s = "bpfbhmipx"
    print(Solution().lengthOfLongestSubstring(s))

"""tips

"""
