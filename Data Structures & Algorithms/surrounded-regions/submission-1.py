class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rl = len(board)
        cl = len(board[0])
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        s = set()
        def dfs(i,j):
            if i < 0 or i >= rl or j < 0 or j >= cl or board[i][j] != "O" or (i,j) in s:
                return
            
            s.add((i,j))
            for dr,dc in directions:
                row,col = i+dr, j+ dc
                dfs(row,col)

                
            

        for i in range(rl):
            for j in [0, cl-1]:
                if board[i][j] == "O":
                    dfs(i,j)
        for i in [0, rl-1]:
            for j in range(cl):
                if board[i][j] == "O":
                    dfs(i,j)
        print(s)
        
        def dfs2(i,j):
            if i < 0 or i >= rl or j < 0 or j >= cl or board[i][j] != "O" or (i,j) in s:
                return
            
            board[i][j] = "X"
            
            for dr,dc in directions:
                row,col = i+dr, j+ dc
                dfs2(row,col)
        
        for i in range(1,rl-1):
            for j in range(1,cl-1):
                if board[i][j] == "O" and (i,j) not in s:
                    
                    board[i][j] = "X"
