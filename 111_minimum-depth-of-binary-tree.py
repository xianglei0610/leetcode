#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l and r:
            return min(l,r)+1
        if not l:
            return r+1
        if not r:
            return l+1