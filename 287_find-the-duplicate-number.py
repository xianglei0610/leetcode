#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 17:21
@desc:
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        for i in nums:
            if data.get(i, 0):
                data[i] += 1
            else:
                data[i] = 1
            if data.get(i, 0) == 2:
                return i


nums = [1,3,4,2,2]
print Solution().findDuplicate(nums)