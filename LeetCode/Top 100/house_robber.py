# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rob(self, root):
        
        if root is None:
            return 0
        
        self.dp = {}
        def helper(root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None:
                return 0
            if root in self.dp:
                return self.dp[root]
            # including the root
            included = 0
            included += root.val
            if root.left and root.left.left:
                included += helper(root.left.left)
            if root.left and root.left.right:
                included += helper(root.left.right)
            if root.right and root.right.left:
                included += helper(root.right.left)
            if root.right and root.right.right:
                included += helper(root.right.right)

            #not including the root
            excluded  = 0
            excluded += helper(root.left) + helper(root.right)
            self.dp[root] =  included if included>excluded else excluded
            return self.dp[root]
        
        helper(root)
        return self.dp[root]