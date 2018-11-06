#coding=utf8

class Sulution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
print Sulution().hammingDistance(4, 1)