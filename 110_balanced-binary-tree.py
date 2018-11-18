#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left = self.getMaxdepth(root.left)
        right = self.getMaxdepth(root.right)
        if abs(left-right) >1:
            return True
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getMaxdepth(self,root):
        if not root:
            return 0
        return max(self.getMaxdepth(root.left),self.getMaxdepth(root.right))+1