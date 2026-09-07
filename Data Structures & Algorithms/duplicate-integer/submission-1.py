class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            if h.get(i, False):
                return True
            else:
                h[i] = True
        return False

        # O(n) time and space