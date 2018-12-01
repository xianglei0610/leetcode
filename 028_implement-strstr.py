#coding=utf-8

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        
        return haystack.find(needle)
    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack) - len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
        
haystack = "baaaa"
needle = "aaa"  
print Solution().strStr(haystack, needle)      
        