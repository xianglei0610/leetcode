#coding=utf-8

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) !=len(b):
            return max(len(a),len(b))
        elif len(a) == len(b) and a==b:
            return -1
        else:
            return len(a)
