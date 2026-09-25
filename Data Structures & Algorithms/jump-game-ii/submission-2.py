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
