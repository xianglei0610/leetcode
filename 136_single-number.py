#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 11:23
@desc:
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2-sum(nums)

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for num in nums[1:]:
            res = res ^ num
        return res