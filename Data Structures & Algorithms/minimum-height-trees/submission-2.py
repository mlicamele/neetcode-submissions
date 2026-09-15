class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [i for i in range(n)]
        h = {}
        for edge in edges:
            a, b = edge
            if a in h:
                h[a].append(b)
            else:
                h[a] = [b]
            if b in h:
                h[b].append(a)
            else:
                h[b] = [a]
        paths = {}
        for k in h:
            q = [([k], 0)]
            visited = [False]*n
            visited[k] = True
            while q:
                path, c = q.pop(0)
                for node in h[path[-1]]:
                    if not visited[node]:
                        path.append(node)
                        if c + 1 in paths:
                            paths[c+1].append(path.copy())
                        else:
                            paths[c+1] = [path.copy()]
                        q.append((path.copy(), c + 1))
                        path.pop()
                        visited[node] = True
        m = max(paths.keys())
        ps = paths[m]
        result = []
        for p in ps:
            if len(p) % 2 == 0:
                c1 = p[m//2]
                if c1 not in result:
                    result.append(c1)
                c2 = p[m//2 + 1]
                if c2 not in result:
                    result.append(c2)
            else:
                c = p[m//2]
                if c not in result:
                    result.append(c)
        return result
        
        

