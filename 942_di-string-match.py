#coding=utf-8
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ni = 0
        nd = len(S)
        res=[]
        for i in S:
            if i=='I':
                res.append(ni)
                ni+=1
            else:
                res.append(nd)
                nd-=1
        res.append(ni)
        return res 
print Solution().diStringMatch(S="IDI")