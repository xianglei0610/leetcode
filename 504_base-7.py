#coding=utf-8

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        if not num:
            return 0
        n = abs(num)
        while n:
            res += str(n%7)
            n = n/7
        return res if num>0 else '-'+res