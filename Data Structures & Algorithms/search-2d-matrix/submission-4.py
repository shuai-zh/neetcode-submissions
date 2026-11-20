class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix) - 1

        while u <= d:
            mid = (u+d)//2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                u = mid +1
            else:
                d = mid - 1
        
        row = (u+d)//2

        l = 0
        r = len(matrix[0]) -1

        while l <= r:
            mid = (l+r)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid +1
            else:
                r = mid - 1
        return False
