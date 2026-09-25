class Solution:
    def convert(self, s: str, numRows: int) -> str:
        h = numRows
        z = h - 2
        st = True
        i = 0
        res = []
        for r in range(h):
            res.append([])
        while i < len(s):
            c = 0
            if st:
                while c < h:
                    if i + c >= len(s):
                        break
                    res[c].append(s[i+c])
                    c += 1
                i += c
                st = False
            else:
                c = 0
                while c < z:
                    if i + c >= len(s):
                        break
                    res[h - 2 - c].append(s[i+c])
                    c += 1
                i += c
                st = True
        result = ""
        for r in res:
            for e in r:
                result += e
        return result

