#coding=utf-8


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        f = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = []
        for word in words:
            s = ''
            for i in word:
                s += f[ord(i)-97]
            d.append(s)
        return len(set(d))

words = ["gin", "zen", "gig", "msg"]
print Solution().uniqueMorseRepresentations(words)

