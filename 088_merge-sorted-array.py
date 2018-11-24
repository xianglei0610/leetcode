#coding=utf-8

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l  =len(nums1)
        while l>m:
            nums1.pop()
            l -= 1
        print nums1
        nums1.extend(nums2[:n])
        nums1.sort()
            
            


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3  
print Solution().merge(nums1, m, nums2, n)   