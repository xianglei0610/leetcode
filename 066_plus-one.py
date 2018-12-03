#coding=utf-8

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in range(len(digits)):
            sum = sum*10 +digits[i]
        print sum
        sum  += 1
        return [int(i) for i in str(sum)]

digits = [1,2,3]

print Solution().plusOne(digits)      