class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row , col = len(board), len(board[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r == row or c == col or board[r][c] != "O":
                return 

            board[r][c] = "T" 
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr , dc in directions:
                dfs(r + dr, c + dc)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r in [0,row - 1] or c in [0, col - 1]):
                    dfs(r,c)


        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"   