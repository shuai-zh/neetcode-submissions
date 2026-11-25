class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.cur = 0
        def dfs(i,j):
            if i< 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            self.cur += 1

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    
                    self.cur = 0
                    dfs(i,j)
                    
                    self.res = max(self.res, self.cur)
        
        return self.res