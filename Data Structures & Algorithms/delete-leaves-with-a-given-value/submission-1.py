# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.rec(root, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root
    def rec(self, root: Optional[TreeNode], target: int):
        if root.left != None:
            self.rec(root.left, target)
        if root.right != None:
            self.rec(root.right, target)
        if root.left != None and root.left.left is None and root.left.right is None and root.left.val == target:
            root.left = None
        if root.right != None and root.right.left is None and root.right.right is None and root.right.val == target:
            root.right = None
        return root

