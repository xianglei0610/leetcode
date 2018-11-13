#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/13 10:18
@desc:
'''


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ch = 0
        for i in s+t:
            ch = ch^ord(i)
        return chr(ch)

s= 'abc'
t = 'abcd'

print Solution().findTheDifference(s, t)