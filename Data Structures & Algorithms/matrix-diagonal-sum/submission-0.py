class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for r in range(len(mat)):
            s += mat[r][r]
            if len(mat) - 1 - r != r:
                s += mat[len(mat) - 1 - r][r]
        return s