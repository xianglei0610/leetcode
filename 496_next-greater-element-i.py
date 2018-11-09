#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 9:36
@desc:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。

'''

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []

        for i in findNums:
            print nums.index(i)+1,len(nums)
            if nums.index(i)+1>=len(nums):
                a.append(-1)
            else:
                flag = False
                for j in range(nums.index(i)+1, len(nums)):
                    if nums[j]>i:
                        flag = True
                        break
                if flag:
                    a.append(nums[j])
                else:
                    a.append(-1)
        return a
nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
print Solution().nextGreaterElement(nums1, nums2)