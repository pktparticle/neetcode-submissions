class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        largestInRow = [matrix[i][cols-1] for i in range(rows)]
        row = -1
        for i in range(rows):
            if largestInRow[i]==target:
                return True
            elif largestInRow[i]>target:
                row = i
                break
        if row == -1:
            return False
        searchDomain = matrix[row]
        left, right = 0, cols-1
        while left <= right:
            mid = (left+right)//2
            if searchDomain[mid] == target:
                return True
            elif searchDomain[mid]<target:
                left+=1
            else:
                right-=1
        return False