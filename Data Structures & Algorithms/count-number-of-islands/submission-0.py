class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(i,j,grid):
            dir = [[-1,0],[1,0],[0,-1],[0,1]]
            if grid[i][j]=="1":
                grid[i][j]="-1"
                for d in dir:
                    i_idx = i+d[0]
                    j_idx = j+d[1]
                    if i_idx>=0 and j_idx>=0:
                        if i_idx<len(grid) and j_idx<len(grid[0]):
                            bfs(i_idx,j_idx,grid)
        
        count =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count += 1
                    bfs(i,j,grid)
        return count