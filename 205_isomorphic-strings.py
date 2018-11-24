#coding=utf-8

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        
        d  = {}
        for i in range(len(s)):
            k = s[i]
            v = t[i]
            if k in d.keys():
                if v != d.get(k):
                    return False
            else:
                if v in d.values():
                    return False
                d[k] = v
        return True
        #return len(set(zip(s,t))) == len(set(s)) == len(set(t))   