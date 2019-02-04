# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def subTrees(s, e):
            res = []
            if s > e:
                res.append(None)
                return res

            for i in range(s, e + 1):
                leftSubtrees = subTrees(s, i - 1)
                rightSubtrees = subTrees(i + 1, e)

                for lt in leftSubtrees:
                    for rt in rightSubtrees:
                        root = TreeNode(i)
                        root.left = lt
                        root.right = rt
                        res.append(root)
            return res

        return subTrees(1, n) if n > 0 else []