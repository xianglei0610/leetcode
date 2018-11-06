#coding=utf-8

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        'RLDU'
        return moves.count('D') == moves.count('U') and moves.count('R') == moves.count('L')

print Solution().judgeCircle('DURL')