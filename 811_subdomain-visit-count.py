#!/usr/bin/env python
# encoding: utf-8
'''
@author: xianglei
@time: 2018/11/8 14:36
@desc:
'''


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        d = {}
        for i in cpdomains:
            count, domain = i.split(' ')
            if domain in d.keys():
                d[domain] = d[domain] + int(count)
            else:
                d[domain] = int(count)
            dct = domain.count('.')
            while dct >0:
                domain = domain.split('.', 1)[-1]
                if domain in d.keys():
                    d[domain] = d[domain] + int(count)
                else:
                    d[domain] = int(count)
                dct = domain.count('.')
        s = []
        for k,v in d.items():
            s.append(str(v)+' '+k)
        return s




cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

Solution().subdomainVisits(cpdomains)