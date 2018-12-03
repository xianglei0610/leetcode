#coding=utf=8

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i<j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].upper()!=s[j].upper():
                    return False
                else:
                    i += 1
                    j -= 1
            if not s[i].isalnum():
                i +=1
            if not s[j].isalnum():
                j -=1
        return True
s = "A man, a plan, a canal: Panama"
print Solution().isPalindrome(s)
                