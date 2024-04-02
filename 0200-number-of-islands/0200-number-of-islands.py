class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        row , col = len(grid), len(grid[0])
        visited = set()
        

        def dfs(r,c):
            if r not in range(row) or c not in range(col) or grid[r][c] == "0" or (r,c) in visited:
                return 0

            visited.add((r,c))
            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(row):
            for c in range(col):
                    
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
        return islands
       


        