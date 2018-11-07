#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/7 18:59
@desc:
'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(S)):
            left, right = S[i-len(S)::-1].find(C),  S[i:].find(C)
            if left == -1:
                left = 10000
            if right == -1:
                right = 10000
            res.append(min(left, right))
        return res
print Solution().shortestToChar('abcdefg','a')