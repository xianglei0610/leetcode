#coding=utf8

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(bin(num))[2:]
        print s
        b = ''
        for i in s:
            if i == '1':
                b += '0'
            else:
                b += '1'
        return int(b, 2)


print Solution().findComplement(5)