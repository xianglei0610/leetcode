#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/14 11:10
@desc:
'''
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
            return None
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val == val:
            return root
        else:
            return None