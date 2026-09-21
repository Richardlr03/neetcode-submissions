class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        total = m*n
        left = 0
        right = total-1

        while left <= right:
            mid = (left + right)//2
            i = mid//n
            j = mid%n
            if matrix[i][j] < target:
                left = mid+1
            elif matrix[i][j] > target:
                right=mid-1
            else:
                return True

        return False
        