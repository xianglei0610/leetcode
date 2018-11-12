#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/8 14:11
@desc:
'''


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        sum = 0
        count = 1
        for i in S:
            sum = sum + widths[ord(i)-ord('a')]
            if sum > 100:
                count += 1
                sum = widths[ord(i)-ord('a')]
        return count, sum

print Solution().numberOfLines(
        widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        S="bbbcccdddaaa")
