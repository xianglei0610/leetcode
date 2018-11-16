#coding=utf-8

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split(' ')
        b = B.split(' ')
        c =a +b 
        d =set(c)
        m = []
        for i in d:
            if c.count(i)>1:
                continue
            m.append(i)
        return m

A = "this apple is sweet"
B = "this apple is sour"
print Solution().uncommonFromSentences(A, B)