class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        res = 0
        while queue:
            s = len(queue)
            found = False
            while s > 0:
                rot = queue.pop(0)

                i, j = rot[0], rot[1]

                if i-1 >= 0 and grid[i-1][j] == 1:
                    queue.append((i-1,j))
                    grid[i-1][j] = 2
                    found = True
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    queue.append((i+1,j))
                    grid[i+1][j] = 2
                    found = True
                
                if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                    queue.append((i,j+1))
                    grid[i][j+1] = 2
                    found = True
                if j-1 >=0 and grid[i][j-1] == 1:
                    queue.append((i,j-1))
                    grid[i][j-1] = 2
                    found = True
                s -= 1
            if found:
                res += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res
            
            