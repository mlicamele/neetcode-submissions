"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        h = {}
        res = Node(node.val, [])
        h[res.val] = res
        self.dfs(res, node, h)
        return res
    def dfs(self, res: Optional['Node'], node: Optional['Node'], h):
        for n in node.neighbors:
            if n.val not in h:
                nn = Node(n.val, [])
                h[n.val] = nn
                self.dfs(nn, n, h)
            res.neighbors.append(h.get(n.val))
        return

