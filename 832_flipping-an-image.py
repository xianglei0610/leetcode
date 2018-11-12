#coding=utf-8

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = []
        for a in A:
            k = []
            for j in a[::-1]:
                if j:
                    j = 0
                else:
                    j = 1
                k.append(j)
            m.append(k)
        return m

# A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

# print Solution().flipAndInvertImage(A)