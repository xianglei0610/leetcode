#coding=utf-8

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        old = []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                old.append(i)
        B = []
        for i in range(len(even)):
            B.append(even[i])
            B.append(old[i])
        return B
A = [4,2,3,7]
Solution().sortArrayByParityII(A)


