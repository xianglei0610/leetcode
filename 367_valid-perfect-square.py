#coding=utf-8
from _ast import Num

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        r = num
        while l<r:
            mid = (l+r)/2
            t = mid**2
            if t==num:
                return True
            elif t>num:
                r-=1
            else:
                l+=1
        return False
            