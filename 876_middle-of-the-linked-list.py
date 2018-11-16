#coding=UTF8
from pip._vendor.requests.api import head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = quick = head
        
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            
        return slow
            