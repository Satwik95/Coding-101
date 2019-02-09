class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def in_grid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        def neighbours(node):
            print(node)
            p, q = node
            dir = ((-1,0),(0,1),(1,0),(0,-1))
            return [(x, y) for x, y in [(p+i,q+j) for i, j in dir] if in_grid(x, y)]
            
        def dfs(node):
            self.visited.append(node)
            for v in neighbours(node):
                if grid[v[0]][v[1]]==1:
                    dfs(v)
                
        components = 0
        self.visited = []
        dfs((0,0))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node = (i,j)
                if grid[i][j]=="1 and node not in self.visited:
                    components += 1
                    dfs(node)
        print(self.visited)
        return components


print(Solution().numIslands())