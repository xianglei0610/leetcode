#coding=utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0   
        for i in range(len(nums)):
            if nums[i]!=nums[index]:
                index += 1
                nums[index] = nums[i]  
        return index +1
print Solution().removeDuplicates([1,2,3,4,4,5,6])