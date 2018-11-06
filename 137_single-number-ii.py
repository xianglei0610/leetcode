#coding=utf8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*sum(list(set(nums)))-sum(nums))/2

nums = [2,5,5,5]
print Solution().singleNumber(nums)