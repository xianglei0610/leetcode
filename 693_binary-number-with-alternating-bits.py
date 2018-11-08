#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/8 14:52
@desc:
'''


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n < 3:
            return True
        if n == 3:
            return False
        s = bin(n)[2:]
        for i in range(1, len(s)-1):
            if s[i] ==s[i-1] or s[i]==s[i+1]:
                return False
        return True

    def hasAlternatingBits1(self, n):

        a = bin(n)
        if '00' in a or '11' in a:
            return False
        return True


n = 7
n = 11
print Solution().hasAlternatingBits(n)