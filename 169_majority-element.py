#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 17:46
@desc:
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = set(nums)
        n = len(nums) / 2
        for i in s:
            if nums.count(i) > n:
                return i


nums = [2, 2, 1, 1, 1, 2, 2]
print Solution().majorityElement(nums)