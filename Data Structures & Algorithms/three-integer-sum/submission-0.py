class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:        
        nums.sort()
        res = []
        for i in range(len(nums)):
            ni = nums[i]
            if i > 0 and ni == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                nj = nums[j] 
                nk = nums[k]
                
                s = ni + nj + nk
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append([ni, nj, nk])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res

        # O(n^2) time
            # O(n) for loop
            # O(n) while loop inside for loop
            # Constant-time operations done inside both
        # O(n) space
            # res holds at most n entires
        # Notes:
            # Could not figure out the most inner while loop for advancement after finding an entry to add, had close/similar ideas like j += 1 and k -= 1 or a while loop checking nums[j] == nums[j + 1], but that was the bottleneck for this problem