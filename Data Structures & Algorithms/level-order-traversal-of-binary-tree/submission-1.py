# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = []
        res = []
        curLevel = -1
        q.append((root, 0))
        while q:
            node, l = q.pop(0)
            if l > curLevel:
                curLevel += 1
                res.append([])
            res[l].append(node.val)
            if node.left != None:
                q.append((node.left, l + 1))
            if node.right != None:
                q.append((node.right, l + 1))
        return res