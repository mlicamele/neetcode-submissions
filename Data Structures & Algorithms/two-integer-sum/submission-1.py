class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        for i in range(len(nums)):
            c = target - nums[i]
            if c in h and h[c] != i:
                return [i, h[c]]
        return []

        # O(2n) = O(n) time
        # O(n) space