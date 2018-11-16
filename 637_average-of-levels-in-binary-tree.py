#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None
        ans = []
        
        que = [root]
        
        while que:
            n = len(que)
            sum = 0
            for i in range(n):
                r = que.pop(0)
                sum += r.val
                if r.left:
                    que.append(r.left)
                if r.right:
                    que.append(r.right)
            ans.append(float(sum)/n)        
                
        return ans
        