# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def check(self, s, t):
        if s is None or t is None:
            return s is None and t is None
        if s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return not s and not t
        
        if self.check(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)