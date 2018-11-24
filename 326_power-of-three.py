class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            if n%3 ==0:
                n /= 3
            else:
                break
        return True if n ==1 else False   