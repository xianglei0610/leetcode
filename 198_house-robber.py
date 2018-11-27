#coding=utf-8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last =0
        now = 0
        for i in nums:
            last, now = now, max(last+i,now)
        return now
    
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        else:
            dp = [0]*len(nums)
            dp[0]=nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(num[i]+dp[i-2],dp[i-1])
        return dp[-1]