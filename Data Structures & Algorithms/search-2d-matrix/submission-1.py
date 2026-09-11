class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        top = 0
        bottom = n - 1

        while top <= bottom:
            middle = (top+bottom)//2
            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break

        m = len(matrix[middle])
        start = 0
        end = m - 1
        while start <= end:
            middle2 = (start+end)//2
            if target == matrix[middle][middle2]:
                return True
            elif target < matrix[middle][middle2]:
                end = middle2 - 1
            else:
                start = middle2 + 1

        return False
