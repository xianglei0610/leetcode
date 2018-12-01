# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        if not root:
            return ans
        tmp = {}
        def curNode(r):
            if r.val in tmp.keys():
                tmp[r.val] += 1
            else:
                tmp[r.val] = 1 
            if r.left:
                curNode(r.left)
            if r.right:
                curNode(r.right)
            
        
        curNode(root)
        
        max_val=max(tmp.values())
        
        for k,v in tmp.items():
            if v == max_val:
                ans.append(k)
        return ans
        