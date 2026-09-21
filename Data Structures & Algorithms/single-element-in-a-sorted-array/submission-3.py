class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        p = 0
        while p < len(nums):
            if p == len(nums) - 1:
                return nums[p]
            if nums[p] == nums[p+1]:
                p += 2
                continue
            else:
                return nums[p]