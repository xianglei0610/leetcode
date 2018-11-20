#coding=utf-8

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)<2:
            return 
        
        d = {}
        for i in range(len(numbers)):
            if target-numbers[i] in d.keys():
                return [d.get(target-numbers[i])+1, i+1]
            else:
                d[numbers[i]] = i
        return None 