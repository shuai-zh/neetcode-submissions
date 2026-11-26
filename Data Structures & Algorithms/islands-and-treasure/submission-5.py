class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        lr = len(grid)
        lc = len(grid[0])
        INF = 2147483647

        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        step = 0
        while queue:
            size = len(queue)
            
            
            while size > 0:
                i,j = queue.pop(0)
                
                for dr, dc in directions:
                    row,col = i+dr, j+dc
                    
                    if (row in range(lr)) and (col in range(lc)):
                        if grid[row][col] == INF:
                            
                            grid[row][col] = step + 1
                            queue.append((row,col))
                            
                        
                size -= 1
            step += 1






