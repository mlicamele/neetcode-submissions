class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a = [0]*26
        abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        cum = []
        for w in words:
            a = [0]*26
            for c in w:
                a[ord(c) - ord("a")] += 1
            cum.append(a)
        res = []
        print(cum[0])
        for c in range(len(cum[0])):
            m = None
            for r in range(len(cum)):
                if m is None or cum[r][c] < m:
                    m = cum[r][c]
            res.append(m)
        result = []
        for i, n in zip(res, abc):
            for j in range(i):
                result.append(n)
        return result