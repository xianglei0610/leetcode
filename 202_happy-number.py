#coding=utf-8

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        temp = []
        def get_add(n):
            ret = 0
            while n!=0:
                g= n%10
                ret += g **2
                n = int(n/10)
            return ret
        
        
        while True:
            n = get_add(n)
            print n,temp
            if n ==1:
                return True
            elif n in temp:
                return False
            else:
                temp.append(n)
print Solution().isHappy(19)  