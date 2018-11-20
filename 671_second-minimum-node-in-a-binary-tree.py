#coding =utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return -1
        s =set()
        que = [root]
        while que:
            m = que.pop()
            s.add(m.val)
            if m.left:
                que.append(m.left)
            if m.right:
                que.append(m.right)
        if len(s)<2:
            return -1
        else:
            s.remove(min(s))
            return min(s)