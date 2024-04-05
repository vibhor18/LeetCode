class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = collections.deque()
        

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        minute = 0
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue and fresh_oranges > 0:
            for i in range(len(queue)):
                ROW, COL = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = ROW + dr, COL + dc
                    if new_row >= 0 and new_row < row and new_col >= 0 and new_col < col and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh_oranges -= 1
                        queue.append((new_row, new_col))
            minute += 1
        
        return minute if fresh_oranges == 0 else -1
