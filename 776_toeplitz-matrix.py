#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/9 16:26
@desc:
'''


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        a = matrix[0]
        for i in range(1, len(matrix)):
            if a [:-1] == matrix[i][1:]:
                a = matrix[i]
            else:
                return False
        return True



matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

print Solution().isToeplitzMatrix(matrix)