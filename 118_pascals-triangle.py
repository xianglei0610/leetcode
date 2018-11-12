#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/8 15:44
@desc:
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = [[1]]
        for i in range(1,numRows):
            b=[1,1]
            print a[-1]
            for j in range(len(a[-1])-1):
                b.insert(j+1,a[-1][j]+a[-1][j+1])
            a.append(b)
        return a

    def generate1(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = []
        for i in range(numRows):
            b = [1]*(i+1)
            a.append(b)
            for j in range(1, i):
                a[i][j] = a[i-1][j-1]+a[i-1][j]
        return a


print Solution().generate1(5)