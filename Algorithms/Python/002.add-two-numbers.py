#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2016-12-11
===================
[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium
===================
problem description
===================
You are given two linked lists representing two non-negative numbers. The
digits are stored in reverse order and each of their nodes contain
a single digit.
 Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


class Solution(object):
    # solution 1
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3, tag = ListNode(0), 0
        head = l3

        while tag or l1 or l2:
            node = ListNode(tag)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            tag = node.val / 10
            node.val = node.val % 10
            head.next = node
            head = head.next
        return l3.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(Solution().addTwoNumbers(l1, l2))

"""tips

"""
