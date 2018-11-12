#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 17:31
@desc:
已知三个点为(x1,y1)，(x2,y2)，(x3,y3)

面积为A= 1/2 * [ x1(y2-y3) + x2(y3-y1) + x3(y1-y2) ]
'''
import itertools

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        combinations = itertools.combinations(points, 3)
        print combinations
        _max = 0
        for com in list(combinations):
            point1, point2, point3 = com[0], com[1], com[2]
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3
            s = (1 / 2.0) * abs(x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1)
            _max = max(_max, s)
        return _max


points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print Solution().largestTriangleArea(points)