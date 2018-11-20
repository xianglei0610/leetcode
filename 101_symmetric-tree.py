# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def isSameTree(p, q):
            if not q and not p:
                return True
            if q and p and q.val ==p.val:
                l = isSameTree(p.left, q.right)
                r = isSameTree(p.right, q.left)
                return l and r
            else:
                return False
                
        return isSameTree(root.left, root.right)