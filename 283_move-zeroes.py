#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 18:45
@desc:
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        for i in nums:
            if i==0:
                nums.remove(0)
        nums.extend([0]*n)
        return nums

nums =[0,1,0,3,12]
print Solution().moveZeroes(nums)