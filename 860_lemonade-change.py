#coding=utf-8

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        a = {5:0,10:0}
        
        for i in bills:
            if i==5:
                a[5] += 1
            elif i==10:
                if a[5]==0:
                    return False
                a[5] -=1
                a[10] += 1
            elif i==20:
                if a[10]!=0:
                    if a[5]==0:
                        return False
                    else:
                        a[5] -= 1
                        a[10] -= 1
                else:
                    if a[5]<3:
                        return False
                    else:
                        a[5] -=3
        return True