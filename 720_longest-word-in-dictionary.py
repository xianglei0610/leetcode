#coding=utf-8

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        longestWord = ''

        a = set([''])
        for i in words:
            if i[:-1] in a:
                a.add(i)
                if len(i) > len(longestWord):
                    longestWord = i
        return longestWord
                