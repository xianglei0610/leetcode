#coding=utf-8
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        d = []
        for i in range(left, right+1):
            if i % 10 == 0 or '0' in str(i):
                continue
            j = str(i)
            flag = True
            for k in j:
                print i,k
                if i % int(k) != 0:
                    flag = False
            if flag:
                d.append(i)
        return d


print Solution().selfDividingNumbers(66, 708)