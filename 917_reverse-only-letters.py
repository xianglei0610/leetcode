#coding=utf-8
from msilib.schema import ReserveCost

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = []
        for index ,v in enumerate(S):
            if v.isalpha():
                l.append(v)
        res = ''
        for index,v in enumerate(S):
            if v.isalpha():
                res += l.pop()
            else:
                res += v
        return res

S = "a-bC-dEf-ghIj"
print Solution().reverseOnlyLetters(S)
                
        