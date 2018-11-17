#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        if not q or not q:
            return False
        if p and q and p.val == q.val:
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
            return l and r
        else:
            return False
            
            