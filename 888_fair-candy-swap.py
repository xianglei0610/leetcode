#coding=utf-8

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        sum_a = sum(A)
        sum_b = sum(B)
        s_b = set(B)
        avr = (sum_a+sum_b)/2
        for i in A:
            b = avr-(sum_a-i)
            
            if b>= 1 and b in s_b:
                return [i,b]
            
              
            