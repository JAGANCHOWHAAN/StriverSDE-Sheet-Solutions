class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat=[]
        for row in matrix:
            for num in row:
                flat.append(num)
        for i in range(len(flat)):
            if flat[i]==target:
                return True
        return False
                