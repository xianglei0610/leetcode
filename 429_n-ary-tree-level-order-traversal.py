#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/14 14:09
@desc:
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[]]
        quene = [(root, 0)]
        print quene
        while quene:
            s, level = quene.pop(0)
            if level >= len(res):
                res.append([])

            res[level].append(s.val)
            for i in s.children:
                quene.append(((i, level + 1)))
        return res