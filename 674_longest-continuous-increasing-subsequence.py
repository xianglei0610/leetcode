#coding=utf-8

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        N = len(nums)
        d=[0]
        count=1
        for i in range(N-1):
            if nums[i]>=nums[i+1]:
                d.append(count)
                count = 0
            count+=1
            #print nums[i],count,d
        d.append(count)
        return max(d)
nums=[1,3,5,4,7]
print Solution().findLengthOfLCIS(nums) 