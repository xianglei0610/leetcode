#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/7 18:32
@desc:
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        s = s.split(' ')
        for i in s:
            a.append(i[::-1])
        return ' '.join(a)
a = "Let's take LeetCode contest"
print Solution().reverseWords(a)