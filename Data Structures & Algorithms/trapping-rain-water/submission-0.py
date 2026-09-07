class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l_max = -1
        r_max = -1
        l = 0
        r = len(height) - 1
        while l < r:
            lh = height[l]
            rh = height[r]
            l_max = max(l_max, lh)
            r_max = max(r_max, rh)
            if l_max < r_max:
                total += l_max - lh
                l += 1
            else:
                total += r_max - rh
                r -= 1
        return total

        # O(n) time
            # O(n) while loop because iterates over at most n elements and does constant-time operations
        # O(1) space
            # Only uses constant-space variables
        # Notes:
            # Need review, basically copied solution, but understood once saw