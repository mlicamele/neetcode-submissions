class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            le = numbers[l]
            re = numbers[r]
            s = le + re
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        # O(n) time
            # While loop goes through at most n elements in numbers
        # O(1) space
            # Only constant space used
