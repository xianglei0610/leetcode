#coding=utf-8


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(c) for c in zip(*A)]