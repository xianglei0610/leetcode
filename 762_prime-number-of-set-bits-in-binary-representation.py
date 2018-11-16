#coding=utf-8

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count =0
        for i in range(L,R+1):
            m = bin(i).count('1')
            if m==1 or m==0:
                continue
            if m==2 or m==3:
                count +=1
                continue
            for i in range(2, m/2+1):
                if m%i==0:
                    flag = 0
                    break
                else:
                    flag =1
            if flag:
                count +=1
        return count
                
            
    
print Solution().countPrimeSetBits(10, 18)