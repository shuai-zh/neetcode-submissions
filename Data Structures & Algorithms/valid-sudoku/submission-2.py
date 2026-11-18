class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validRow(board: List[List[str]]):
            for i in range(len(board)):
                
                dup = set()
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in dup or (int(board[i][j]) < 1 or int(board[i][j])>9):
                        return False
                    dup.add(board[i][j])
            return True
        
        def validColumn(board: List[List[str]]):
            for j in range(len(board[0])):
                
                dup = set()
                for i in range(len(board)):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in dup or (int(board[i][j]) < 1 or int(board[i][j])>9):
                        return False
                    dup.add(board[i][j])
            return True
        
        def validSub(board: List[List[str]]):
            i = 0
            j = 0

            while i < len(board):
                dup = set()
                for m in range(i,i+3):
                    for n in range(j, j + 3):
                        if board[n][m] == ".":
                            continue
                        if board[n][m] in dup or (int(board[n][m]) < 1 or int(board[n][m])>9):
                            return False
                        dup.add(board[n][m])
                        print(i,j,dup)
                i += 3
                if i == 6:
                    j += 3
            return True

        return validRow(board) and validColumn(board) and validSub(board)
               

                    
                    