#coding=utf-8

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattens_l =pattern
        str_l =str.split(' ')
        print pattens_l,str_l
        if len(pattens_l) != len(str_l):
            return False
        return len(set(pattens_l))==len(set(str_l)) == len(set(zip(pattens_l,str_l)))