# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        temp = root.left
        root.left = root.right
        root.right = temp
        return root