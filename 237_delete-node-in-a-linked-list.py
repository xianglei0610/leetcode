#coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    # def printNode(self, node):
    #     res = []
    #
    #     while node:
    #         if node:
    #             res.append(node.val)
    #             node = node.next
    #     print res


# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# Solution().printNode(node1)
# Solution().deleteNode(node1)
# Solution().printNode(node1)
