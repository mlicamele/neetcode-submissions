class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        if not edges:
            return 0
        import heapq
        h = {}
        w = {}
        for i, e in enumerate(edges):
            a, b = e
            if a not in h:
                h[a] = [b]
            else:
                h[a].append(b)
            if b not in h:
                h[b] = [a]
            else:
                h[b].append(a)
            w[(a,b)] = succProb[i]
        visited = [False]*n
        hq = [(-1, start_node)]
        while hq:
            p, node = heapq.heappop(hq)
            visited[node] = True
            if node == end_node:
                return -1*p
            for n in h[node]:
                if visited[n]:
                    continue
                if (n, node) in w:
                    heapq.heappush(hq, (p*w[(n, node)], n))
                else:
                    heapq.heappush(hq, (p*w[(node, n)], n))
        return 0

