#coding=utf-8

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = 'qwertyuiop'
        second ='asdfghjkl'
        third = 'zxcvbnm'
        d = []
        for i in [first, second, third]:
            for word in words:
                line = set(word.lower())
                print line
                if line.issubset(i):
                    d.append(word)
        return d



words = ["Hello", "Alaska", "Dad", "Peace"]
print Solution().findWords(words)

