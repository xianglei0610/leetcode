#coding=utf-8

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        ans=0
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0)+1
        print d
        for num in nums:
            if num+1 in d:
                ans = max(ans, d[num]+d[num+1])
                print ans
        return ans
nums = [1,3,2,2,5,2,3,7]
print Solution().findLHS(nums) 