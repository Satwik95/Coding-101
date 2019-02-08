class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def in_grid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        def neighbours(node):
            p, q = node
            dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            return [(x, y) for x, y in [(p + i, q + j) for i, j in dir] if in_grid(x, y)]

        def dfs(node):
            self.visited.append(node)
            for v in neighbours(node):
                i, j = v
                print(grid[i][j])
                if grid[i][j]== "1" and v not in self.visited:
                    dfs(v)

        components = 1
        self.visited = []
        dfs((0,0))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node = (i, j)
                if grid[i][j] == "1" and node not in self.visited:
                    components += 1
                    dfs(node)

        return components


print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))