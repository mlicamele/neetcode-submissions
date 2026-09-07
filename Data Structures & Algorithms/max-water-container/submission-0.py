class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = -1
        while l < r:
            lh = height[l]
            rh = height[r]
            area = (r - l) * min(lh, rh)
            max_area = max(max_area, area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area

        # O(n) time
            # While loop doing O(1) work for at most n iterations
        # O(1) space
            # Only constant-space variables used
        # Notes:
            # Took some time/errors to think of advancement if/else block, but eventually figured it out