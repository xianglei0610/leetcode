#coding=utf-8

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res =[]
        if not S:
            return res
        count = 1
        for i in range(1,len(S)):
            if S[i-1]==S[i]:
                count += 1
                if i!=len(S)-1:
                    continue
                else:
                    if count>=3:
                        res.append([i-count+1,i])
            if S[i-1] !=S[i]:
                if count>=3:
                    res.append([i-count,i-1])
                    count =1
                else:
                    count =1
        return res
            
    
S = "abcdddeeeeaabbbcd"
S = 'aaa'
print Solution().largeGroupPositions(S)       