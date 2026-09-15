class Solution:
    h = {}
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.r(nums[:-1], {}), self.r(nums[1:], {}))
    
    def r(self, nums, h):
        n = len(nums)
        if n <= 2:
            return max(nums) if nums else 0
        if n in h:
            return h[n]
        h[n] = max(nums[0] + self.r(nums[2:], h), self.r(nums[1:], h))
        return h[n]