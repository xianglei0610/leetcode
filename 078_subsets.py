#coding=utf-8

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = self.subsets(nums[1:])
        return result + [[nums[0]]+s for s in result ]



# nums = [2,3,1]
# print Solution().subsets(nums)