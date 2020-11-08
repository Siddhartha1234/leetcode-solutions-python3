# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def parse(self, root, hgt):
        if root is None:
            return

        if root.left is None and root.right is None:
            self.mind = min(self.mind, hgt)

        self.parse(root.left, hgt + 1)
        self.parse(root.right, hgt + 1)

    def minDepth(self, root: TreeNode) -> int:
        self.mind = 2**50
        self.parse(root, 1)
        return 0 if self.mind == 2**50 else self.mind
