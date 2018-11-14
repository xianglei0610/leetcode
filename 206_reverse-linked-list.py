#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/14 14:10
@desc:
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        newList = None
        while cur:
            tmp = cur.next
            cur.next = newList
            newList=cur
            cur = tmp
        return newList

