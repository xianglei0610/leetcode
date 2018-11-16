#coding=UTF8

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        for i in ops:
            print res
            if i=='+':
                res.append(sum(res[-2:]))
                             
            
            elif i == "C":
                if res:
                    del res[-1]
            elif i == "D":
                res.append(res[-1]*2)  
            else:
                res.append(int(i))
        return sum(res)
                
        
ops = ["5","2","C","D","+"]

print Solution().calPoints(ops)