#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/13 10:50
@desc:
'''


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(N+1):
            s =str(i)
            num =0
            for char in s:
                if char in '347':
                    num -=1
                    break
                elif char in '018':
                    num +=1
            if len(s)!=num and num!=-1:
                count = count +1
        return count
