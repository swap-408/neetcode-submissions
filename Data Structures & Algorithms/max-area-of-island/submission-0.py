class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c,grid):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==0: return 0
            dir = [[-1,0],[1,0],[0,-1],[0,1]]
            grid[r][c]=0
            ar = 1
            for dr,dc in dir:
                ar += dfs(r+dr,c+dc,grid)
            return ar
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area,dfs(r,c,grid))
        
        
        return area
