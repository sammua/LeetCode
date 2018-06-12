#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-06-11
===================
[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/) | Easy
===================
problem description
===================
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def my_print(self):
        print self.val,
        if self.next:
            self.next.my_print()


class Solution(object):
    # solution 1
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        dummy = head
        while l1 or l2:
            if not l1:
                dummy.next = l2
                break
            if not l2:
                dummy.next = l1
                break
            if l1.val <= l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        return head.next


if __name__ == '__main__':
    a_3 = ListNode(4)
    a_2 = ListNode(2)
    a_1 = ListNode(1)
    a_2.next = a_3
    a_1.next = a_2
    b_3 = ListNode(4)
    b_2 = ListNode(3)
    b_1 = ListNode(1)
    b_2.next = b_3
    b_1.next = b_2

    result = Solution().mergeTwoLists(a_1, b_1)
    result.my_print()

"""tips
recursion methods:
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python
"""
