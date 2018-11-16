#coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        l = []
        def dfs(root, path, res):
            if not root.left and not root.right:
                res.append(path+str(root.val))
                return 
            if root.left:
                dfs(root.left, path+str(root.val)+'->',res)
            if root.right:
                dfs(root.right, path+str(root.val)+'->',res)
        
        dfs(root,'', l)
        return l