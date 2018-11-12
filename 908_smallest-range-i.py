#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/8 10:25
@desc:
'''


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        s = A[-1]-A[0]-2*K
        if s<0:
            s = 0
        return s
A= [0,10]
print Solution().smallestRangeI(A,2)