#coding=utf-8


class Solution:
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        res = 0
        for i in s:
            res += int(i)

        while res > 9:
            s = str(res)
            res = 0
            for i in s:
                res += int(i)
        return res

    def addDigits(self, num):
        return num and (num%9 or 9)
print Solution().addDigits(123)
print Solution().addDigits(90)