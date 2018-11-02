#coding=utf-8
import re


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        d = []
        for i in emails:
            a, b = i.split('@')
            a = i.replace('.', '')
            s = a.split('+')[0] +'@'+ b
            d.append(s)
        return len(set(d))


