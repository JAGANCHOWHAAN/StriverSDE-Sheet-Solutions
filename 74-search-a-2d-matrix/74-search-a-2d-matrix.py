class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][0] or i == len(matrix)-1:
                if target in matrix[i-1]:
                    return True
                else:
                    if target in matrix[i]:
                        return True
                    return False