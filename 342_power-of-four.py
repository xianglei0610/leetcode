#coding=utf-8

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        while num %4 ==0:
            num = num/4
        if num ==1:
            return True
        return False
        