#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: mabin
date  : 2018-06-05
===================
[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/) | Medium
===================
problem description
===================
Given a linked list, remove the n-th node from the end of list and return its
head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes
1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        before = after = new_head
        for _ in range(n+1):
            before = before.next
        while before:
            before = before.next
            after = after.next
        after.next = after.next.next
        return new_head.next

    # solution 2
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def getIndex(node):
            if not node:
                return 0
            print "current_index={}".format(node.val)
            print "current_node:",
            node.my_print()
            print
            index = getIndex(node.next) + 1
            if index > n:
                print "index: {}, [change]".format(index)
                node.next.val = node.val
                print "changed:",
                node.my_print()
                print
            else:
                print "index: {}, [remain]".format(index)

            return index

        getIndex(head)
        return head.next

    # solution 3
    def removeNthFromEnd3(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            else:
                print "current head", head.val
            i, head.next = remove(head.next)
            print "current i={}, head={}".format(i, head.val)
            return i + 1, (head, head.next)[i + 1 == n]

        return remove(head)[1]


if __name__ == '__main__':
    n5 = ListNode(5)
    n4 = ListNode(4)
    n3 = ListNode(3)
    n2 = ListNode(2)
    n1 = ListNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    result = Solution().removeNthFromEnd3(n1, 3)
    result.my_print()
"""
    tests = [
    ]
    for t in tests:
        print(t, Solution().removeNthFromEnd(t))
"""

"""tips
discuss:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions

solution 1
需要增加一个头结点, 然后用两个指针, p1, p2, p1 先移动n个节点, 之后p1, p2一起
移动, p1 移动到结尾的时候, p2 的位置就是要删除的位置的前一位置
solution 2
改变节点的值, 将n个节点之前的节点的值依次后移, 然后返回 head.next
current_index=1
current_node: 1 2 3 4 5
current_index=2
current_node: 2 3 4 5
current_index=3
current_node: 3 4 5
current_index=4
current_node: 4 5
current_index=5
current_node: 5
index: 1, [remain]
index: 2, [remain]
index: 3, [remain]
index: 4, [change]
changed: 2 2 4 5
index: 5, [change]
changed: 1 1 2 4 5

"""
