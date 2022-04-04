from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count_fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    count_fresh+=1
        if count_fresh==0:
            return 0
        t = [[1,0],[0,1],[-1,0],[0,-1]]
        count=0
        # print(count_fresh)
        while(len(q)!=0):
            count+=1
            j=len(q)
            # print(q)
            while(j>0):

                a=q.popleft()
                for i in t:
                    x,y =  a[0]+i[0],a[1]+i[1]
                    if x>=len(grid) or x<0 or y>=len(grid[0]) or y<0 or grid[x][y]==0 or grid[x][y]==2:
                        continue

                    count_fresh-=1
                    if count_fresh==0:
                        return count
                    grid[x][y]=2
                    q.append([x,y])
                j-=1
        if count_fresh!=0:
            return -1
        return count-1
                
                    
        
        
        
    