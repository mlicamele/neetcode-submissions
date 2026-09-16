class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        h = {}
        edges = {}
        for e, v in zip(equations, values):
            a, b = e
            if a in edges:
                edges[a].append(b)
            else:
                edges[a] = [b]
            if b in edges:
                edges[b].append(a)
            else:
                edges[b] = [a]
            h[(a, b)] = v
        res = []
        for q in queries:
            a, b = q
            if a not in edges or b not in edges:
                res.append(-1)
                continue
            q = [(a, 1)]
            m = -1
            visited = {}
            while q:
                elem, c = q.pop()
                if elem == b:
                    m = c
                    break
                for n in edges[elem]:
                    if n in visited:
                        continue
                    if (elem, n) in h:
                        q.append((n, c * h[(elem, n)]))
                        visited[n] = True
                    elif (n, elem) in h:
                        q.append((n, c / h[(n, elem)]))
                        visited[n] = True
                    else:
                        continue
            res.append(m)
        return res