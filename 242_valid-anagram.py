#coding=utf-8

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = sorted(list(s))
        t1 = sorted(list(t))
        return s1 == t1