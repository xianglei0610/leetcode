#coding=utf-8

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 1
        right = len(A)-2
        while left < right:
            mid = (left+right)//2
            if A[mid]> A[mid+1]:
                right = mid
            if A[mid] < A[mid+1]:
                left = mid+1
        return left
Solution().peakIndexInMountainArray([1,2,3,4,5,1])



