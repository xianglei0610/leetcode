#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/14 16:57
@desc:
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            right = dfs(root.right)
            left = dfs(root.left)

            self.ans = max(self.ans, right + left)
            return max(left, right) + 1

        dfs(root)
        return self.ans
