#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/14 10:21
@desc:
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root:
            root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root