#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/13 10:27
@desc:
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
        return j

nums = ['a',1,2,3,4,'a']
val='a'
print Solution().removeElement(nums,val)
