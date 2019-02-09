# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # thanks to girikuncoro for his solution
        # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-           
        # lines-of-python-solution-(reverse-preorder-traversal)
        
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root