class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)

        hashmap = {}
        left = 0

        max_length = 0

        for right, c in enumerate(s):
            if c in hashmap and hashmap[c] >= left:
                left = hashmap[c] + 1
            hashmap[c] = right
            max_length = max(max_length, right - left + 1)

        return max_length
            
