class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range((len(grid[0]))):
                if grid[i][j]==2:
                    self.dfs(i,j,grid,2)
        res = 0
        for i in range(len(grid)):
            for j in range((len(grid[0]))):
                if grid[i][j]==1:
                    return -1
                res = max(res,grid[i][j])
        if res<2:
            return 0
        return res-2


    def dfs(self,row, col, grid,minutes):
        if row==len(grid) or row<0 or col<0 or col==len(grid[0]) or grid[row][col]==0 or 1<grid[row][col]<minutes:
            return
        grid[row][col]=minutes
        self.dfs(row-1,col,grid,minutes+1)
        self.dfs(row+1,col,grid,minutes+1)
        self.dfs(row,col-1,grid,minutes+1)
        self.dfs(row,col+1,grid,minutes+1)