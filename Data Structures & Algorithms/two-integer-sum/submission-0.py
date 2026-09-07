class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            v = nums[i]
            k = target - v
            if k in h:
                l = [i, h[k]]
                l.sort()
                return l
            elif v not in h:
                h[v] = i
        return False