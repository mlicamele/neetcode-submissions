class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        for c in s:
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1
        for c in t:
            if c not in h or h[c] <= 0:
                return False
            h[c] -= 1
        for c in s:
            if h[c] != 0:
                return False
        return True

        # O(2(n + m)) = O(n + m) time
        # O(1) space (constant number of possible characters that could be keys in hashmap)