class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            if len(matrix) == 1:
                mid = 0
                break
            mid = (l + r) // 2
            c1 = matrix[mid][len(matrix[mid])-1]
            c2 = matrix[mid][0]
            if c1 == target:
                return True
            elif c2 == target:
                return True
            elif target > c1:
                l = mid + 1
            elif target < c2:
                r = mid - 1
            else:
                break
        l = 0
        r = len(matrix[mid]) - 1
        while l <= r:
            m = (l + r) // 2
            c = matrix[mid][m]
            if c == target:
                return True
            elif target > c:
                l = m + 1
            else:
                r = m - 1
        return False
