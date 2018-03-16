#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-03-12
===================
[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/description/) | Medium
===================
problem description
===================
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""


# solution 1
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        seq = range(len(s))
        step_1 = 2 * numRows - 2
        out = s[0::step_1]
        for i in range(1, numRows-1):  # 除了首行末行的每一层
            step_2 = 2 * (numRows - i - 1)
            pos_list = seq[i::step_1]
            for pos in pos_list:
                out += s[pos]
                if pos + step_2 <= seq[-1]:
                    out += s[pos + step_2]
        out += s[numRows-1::step_1]
        return out


if __name__ == '__main__':

    s = "PAYPALISHIRING"
    # s = "ABC"
    # s = "ABCD"
    print(Solution().convert(s, 3))
    pass


"""tips
s = "0123456789abcdefg"
numRows = 5
得到的是:
    0   8   g
    1  79  f
    2 6 a e
    35  bd
    4   c
分两个步长,
一个是水平竖直点的步长是 2n-2, 如 (0, 8, g), (1, 9), (2, a)
一个是和深度相关的步长 2(n-i-1), 如 (1, 7), (9, f), (2, 6), (a, e), (3, 5)

"""
