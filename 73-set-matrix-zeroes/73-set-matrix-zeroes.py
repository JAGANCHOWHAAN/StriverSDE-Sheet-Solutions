class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        rowzero=False
        for r in range(row):
            for c in range(col):
                if(matrix[r][c]==0):
                    matrix[0][c]=0
                    if(r>0):
                        matrix[r][0]=0
                    else:
                        rowzero=True
        for r in range(1,row):
            for c in range(1,col):
                if(matrix[0][c]==0 or matrix[r][0]==0):
                    matrix[r][c]=0
        if(matrix[0][0]==0):
            for r in range(row):
                matrix[r][0]=0
        if rowzero:
            for c in range(col):
                if matrix[0][c]==0:
                    for r in range(1,row):
                        matrix[r][c]=0
                else:
                    matrix[0][c]=0
                    
