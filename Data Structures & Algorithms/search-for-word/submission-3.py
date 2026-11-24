class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def find(r,c,k):
            if len(word) == k:
                
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[k] or visited[r][c]:
                return False
            visited[r][c] = True
            r1 = find(r+1,c,k+1)
            r2 = find(r,c+1,k+1)
            r3 = find(r-1,c,k+1)
            r4 = find(r,c-1,k+1)
            visited[r][c] = False
            return r1 or r2 or r3 or r4

        for i in range(rows):
            for j in range(cols):
                if find(i,j,0):
                    return True    
        return False