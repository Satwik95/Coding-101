# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def _isSymmetric(self, nd1, nd2):
        if not nd1 and not nd2:
            return True
        if not nd1 or not nd2:
            return False
        if nd1.val!=nd2.val:
            return False
        return nd1.val==nd2.val and self._isSymmetric(nd1.left, nd2.right) and self._isSymmetric(nd1.right, nd2.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self._isSymmetric(root.left, root.right)