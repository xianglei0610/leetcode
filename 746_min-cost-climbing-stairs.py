#coding=utf-8

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res = [0]*(len(cost)+1)
        print res
        for i in range(2,len(cost)+1):
            res[i] = min(res[i-1]+cost[i-1],res[i-2]+cost[i-2])
        print res
        return res[-1]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] 
print Solution().minCostClimbingStairs(cost)
        