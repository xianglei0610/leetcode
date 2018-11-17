#coding=utf-8
from test._mock_backport import right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        res = ''
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if t.left or t.right:
            res += '(%s)' % left
        if t.right:
            res +='(%s)' % right
        return str(t.val) + res
            