class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def bt(sub, nums, res):
            if len(nums) == 0:
                res.append(sub.copy())
                return
            bt(sub, nums[1:], res)
            sub.append(nums[0])
            bt(sub, nums[1:], res)
            sub.pop()
        
        res = []
        sub = []
        bt(sub, nums, res)
        return res
