#coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return
        map_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in map_dict:
                return map_dict[target - nums[i]], i
            else:
                map_dict[nums[i]] = i
