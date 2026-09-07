class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            val = nums[i]
            key = hash(val)
            if key in dic:
                if val in dic[key]:
                    return True
                else:
                    l = dic[key]
                    l.append(val)
                    dic[key] = l
            else:
                dic[key] = [val]
        return False
            