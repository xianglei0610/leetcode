#coding=utf-8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ((len(nums)+1)*len(nums))/2 -sum(nums)