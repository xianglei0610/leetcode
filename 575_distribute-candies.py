#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 10:35
@desc:
'''


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) // 2)