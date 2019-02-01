# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def pathSum(self, root, sum):
        def dfs(root, sum, visited):
            if not root:
                return 0
            visited = visited + [root.val]
            paths, res = 0, 0
            #print(root.val, visited)
            for num in visited[::-1]:
                res += num
                if res == sum:
                    paths += 1
            return paths + dfs(root.left, sum, visited) + dfs(root.right, sum, visited)
            
        return dfs(root, sum, [])