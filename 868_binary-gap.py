#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 10:57
@desc:
'''


class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)[2:]
        s = []
        left = 0
        for index, v in enumerate(b):
            if v == '1':
                s.append(index - left)
                left = index
        return max(s)

print Solution().binaryGap(8)
