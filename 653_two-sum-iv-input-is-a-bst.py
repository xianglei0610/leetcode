#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        
        que = [root]
        a = set()
        while que:
            m = que.pop()
            if k-m.val in a:
                return True
            a.add(m.val)
            if m.left:
                que.append(m.left)
            if m.right:
                que.append(m.right)
        return False
            
            
        
        
        
        