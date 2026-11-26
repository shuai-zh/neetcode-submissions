class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        res = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while queue:
            s = len(queue)
            found = False
            while s > 0:
                rot = queue.pop(0)

                i, j = rot[0], rot[1]

                for dr, dc in directions:
                    row, col = i+dr, j+dc
                    if (row in range(len(grid))) and (col in range(len(grid[0]))) and grid[row][col] == 1:
                        queue.append((row,col))
                        grid[row][col] = 2
                        found = True
                s -= 1
            if found:
                res += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res
            
            