class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c == 0:
                    continue
                v = 201
                if r - 1 >= 0:
                    v = dp[r-1][c]
                if c - 1 >= 0 and dp[r][c-1] < v:
                    v = dp[r][c-1]
                dp[r][c] = v + grid[r][c]
        return dp[-1][-1]
            
            