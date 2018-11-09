#coding=utf-8

'''
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

IV 4
IX 9
XL 40
XC 90
CD 400
CM 900

I             1
V             5
X             10
L             50
C             100
D             500
M             1000

'''




class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1, "V":5 ,"X":10, "L":50, "C":100, "D": 500, "M":1000}
        m = 0
        for i in range(len(s)):

            if i == len(s)-1:
                m = m + d[s[i]]
            else:
                if d[s[i]] < d[s[i+1]]:
                    m = m - d[s[i]]
                else:
                    m = m + d[s[i]]
        return m
s = "MCMXCIV"
print Solution().romanToInt(s)