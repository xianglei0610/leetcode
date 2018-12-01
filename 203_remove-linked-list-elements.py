#coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
     
        while pre.next:
            if pre.next.val==val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next