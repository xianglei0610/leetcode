#coding=utf-8

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = S.split(' ')
        res = []
        for i ,v in enumerate(l):
            if v[0].lower() not in  ['a', 'e', 'i', 'o', 'u']:
                s = v[0]
                v = v[1:]+s
            v += 'ma'
            v += 'a'*(i+1)
            res.append(v)
        return ' '.join(res)
S="I speak Goat Latin"
print Solution().toGoatLatin(S)