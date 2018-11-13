#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/12 11:32
@desc:
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex<33:
            for i in range(rowIndex+1):
                pass