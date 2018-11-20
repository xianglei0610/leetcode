#coding=utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i  in s:
            if i in d:
                d[i] = d[i]+1
            else:
                d[i] = 1
        res = 0
        for j in d:
            res += d[j]-d[j]%2
        return res+1 if res<len(s) else res
            