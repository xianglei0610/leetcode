#coding=utf-8

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i=0
        for j in range(len(typed)):
            if i<len(name) and name[i] == typed[j]:
                i += 1
#             elif j == 0 or typed[j]==typed[j-1]:
            elif typed[j]!=typed[j-1]:
                return False
        return i == len(name)
name = "alex"
typed = "aaleex"  
print Solution().isLongPressedName(name, typed)                      