#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/14 10:08
@desc:
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        cur = TreeNode(None)

        def d(cur, nums):
            if not nums:
                return
            i = nums.index(max(nums))
            cur.val = max(nums)
            if nums[:i]:
                cur.left = TreeNode(None)
                d(cur.left, nums[:i])
            if nums[i + 1:]:
                cur.right = TreeNode(None)
                d(cur.right, nums[i + 1:])
        d(cur, nums)
        return cur

nums = [3, 2, 1, 6, 0, 5]
print Solution().constructMaximumBinaryTree(nums)