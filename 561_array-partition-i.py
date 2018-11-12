#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/7 18:37
@desc:
'''


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print nums
        s = 0
        for i in range(0, len(nums), 2):
            print i
            s += nums[i]
        return s

nums  = [1, 2,3,2]
print Solution().arrayPairSum(nums)