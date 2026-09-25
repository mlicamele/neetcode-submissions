class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [-1]*len(nums)
        res[0] = 0
        for i in range(len(nums)):
            j = res[i] + 1
            for jump in range(1, nums[i]+1):
                if i + jump < len(nums) and (res[i+jump] > j or res[i+jump] == -1):
                    res[i+jump] = j
        return res[-1]

        # BETTER O(N) SOLUTION
        # n = len(nums)
        # dp = [1000000] * n
        # dp[-1] = 0

        # for i in range(n - 2, -1, -1):
        #     end = min(n, i + nums[i] + 1)
        #     for j in range(i + 1, end):
        #         dp[i] = min(dp[i], 1 + dp[j])
        # return dp[0]

