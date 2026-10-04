class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToBeZero = set()
        colsToBeZero = set()
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowsToBeZero.add(row)
                    colsToBeZero.add(col)
        for row in rowsToBeZero:
            matrix[row] = [0]*cols
        
        for col in colsToBeZero:
            for row in range(rows):
                matrix[row][col] = 0