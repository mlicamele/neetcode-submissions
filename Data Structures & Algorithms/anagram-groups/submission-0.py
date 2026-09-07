class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            k = [0]*26
            for c in s:
                k[ord(c) - ord('a')] += 1
            k = tuple(k)
            if k not in h:
                h[k] = [s]
            else:
                h[k].append(s)
        return list(h.values())

        # O(nm) time
            # O(n) for n s in strs
            # O(m) for m c in s
        # O(nm) space 
            # O(n) for n s in strs stored
            # O(m) for m c in s stored