class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        for i in range(len(s)):
            k = s[i]
            if k not in h:
                h[k] = 1
            else:
                h[k] += 1
        for i in range(len(t)):
            k = t[i]
            if k not in h:
                return False
            else:
                h[k] -= 1
        for k in h:
            if h[k] != 0:
                return False
        return True
        