class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        diff = 1
        while not (xor & diff):
            diff <<= 1
        
        a = 0
        b = 0
        for n in nums:
            if (n & diff):
                a ^= n
            else:
                b ^= n
        
        return [a, b]


