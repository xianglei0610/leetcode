#coding=utf-8

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.preorder(root1) == self.preorder(root2)
        
    def preorder(self, root):
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [root.val]
        res.extend(self.preorder(root.left))
        res.extend(self.preorder(root.right))
        return res