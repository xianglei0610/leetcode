#coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def __init__(self):
        self.sum = 0
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        self.convertBST(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convertBST(root.left)
        return root
    
Tree=TreeNode(2)
Tree.left=TreeNode(1)
Tree.right=TreeNode(3)
s=Solution()
print(s.convertBST(Tree))

print(Tree.val,Tree.left.val,Tree.right.val)
