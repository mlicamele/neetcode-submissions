class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h = {}
        for i, o in enumerate(order):
            h[o] = i
        a = []
        for c in s:
            a.append((h.get(c, 0), c))
        a.sort()
        r = ""
        for i, c in a:
            r += c
        return r