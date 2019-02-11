# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.prev = None
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root):
            if root:
                if not inorder(root.left): return False
                if self.prev and self.prev.val>=root.val: return False
                self.prev = root
                return inorder(root.right)
            return True
        return inorder(root)