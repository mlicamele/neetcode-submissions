class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        h = {}
        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            if a in h:
                h[a].append(b)
            else:
                h[a] = [b]
        res = []
        for query in queries:
            a, b = query
            q = [a]
            visited = [False] * numCourses
            pre = False
            while q:
                node = q.pop(-1)
                visited[node] = True
                if node == b:
                    pre = True
                    break
                if node not in h:
                    continue
                for n in h[node]:
                    if not visited[n]:
                        q.append(n)
            res.append(pre)
        return res
                