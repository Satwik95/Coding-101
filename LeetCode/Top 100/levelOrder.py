# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import defaultdict
        parent = defaultdict(list)
        parent[root.value].append(None)
        frontier = []
        frontier.append(root)
        res = []
        res.append([root.val])
        while frontier:
            next = []
            for u in frontier:
                if u.left and u.left not in parent:
                    parent[u.left.value] = u
                    next.append(u.left)
                if u.right and u.right not in parent:
                    parent[u.right.value] = u
                    next.append(u.right)
            frontier = next
            res.append([x.val for x in next if next != []])
        return res


print(Solution().levelOrder([[3, 9, 20, None, None, 15, 7]]))
