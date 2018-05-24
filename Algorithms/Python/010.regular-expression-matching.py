#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-03-19
===================
[10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/description/) | Hard
===================
problem description
===================
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""


class Solution(object):
    # solution 1
    def isMatch(self, s, p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    # solution 2
    def isMatch2(self, s, p):
        """动态规划的方式是
        s[i:] p[j:] 是否 match

        """
        # 自顶向下的方式, 从 s[0:],p[0:]到s[len(s):],p[len(p)]这个过程状态的存储
        memo = {}  # 存储中间状态

        def dp(i, j):
            if (i, j) not in memo:  # 如果没有该状态
                if j == len(p):  # 规定边界,p没有东西
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

if __name__ == '__main__':

    tests = [
        ("aa", "a"),
        ("aaa", "aa"),
        ("aa", "aa"),
        ("aa", "a*"),
        ("aa", ".*"),
        ("ab", ".*"),
        ("aab", "c*a*b"),
        ("aababbbc", "a*b.*c"),
    ]
    for t in tests:
        print(t, Solution().isMatch(t[0], t[1]))

"""tips
1, 递归方法
从前面开始匹配, 如果前面满足, 那就看剩下的是否满足
要特殊考虑 "*", 0 个 或者 多个 要分开考虑

- 首先, 考虑递归结点, pattern 为空的时候, 返回当前 text 的状态.
- 正常情况, 需要确定开头是否是一致的, pattern 需要满足 p[0] == s[0] or p[0] == ".", 记录当前匹配的状态.
需要考虑 "*" 这种特殊状态, 因为 "*" 表示 0 , 或者 多个
这两种情况要分开考虑. 匹配0个的时候, 用 s, 与 p[2:] 来匹配;
匹配多个的时候(此时已经和s[0] 匹配了, 只需考虑 p 和 s[1:] 就可以了), 用 s[1:] 与 p 来匹配.

2, 动态规划方法
返回 s[i:], p[j:] 的匹配情况的状态列表
自顶向下是 s[0:], p[0:] 到 s[len(s):], p[len(p):] 的一个过程

"""
