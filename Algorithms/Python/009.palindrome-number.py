#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-03-19
===================
[9. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/) | Easy
===================
problem description
===================
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction
of using extra space.

You could also try reversing an integer. However, if you have solved the
problem "Reverse Integer", you know that the reversed integer might overflow.
How would you handle such case?

There is a more generic way of solving this problem.
"""


class Solution(object):
    # solution 1
    def isPalindrome(self, x):
        if x < 0:
            return False
        origin, reverse = x, 0
        while origin:
            reverse = reverse * 10 + origin % 10
            origin /= 10
        return reverse == x


if __name__ == '__main__':
    tests = [
        12321,
        -123,
        12345
    ]
    for a in tests:
        print(a, Solution().isPalindrome(a))
    pass


"""tips

"""
