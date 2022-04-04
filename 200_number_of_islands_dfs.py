class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(i,j,grid)
        return count
    def dfs(self,row, col, grid):
        if row>=len(grid) or row<0 or col>=len(grid[0]) or col<0 or grid[row][col]=='0' or grid[row][col]=='':
            return
        grid[row][col]=''
        self.dfs(row+1,col,grid)
        self.dfs(row,col+1,grid)
        self.dfs(row-1,col,grid)
        self.dfs(row,col-1,grid)