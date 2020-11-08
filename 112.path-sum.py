# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def parse(self, node, cs):
        cs += node.val
        leaf = True
        if node.left is not None:
            self.parse(node.left, cs)
            leaf = False
        if node.right is not None:
            self.parse(node.right, cs)
            leaf = False

        if leaf and cs == self.sum:
            self.found = True
            return

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        self.sum = sum
        self.found = False
        self.parse(root, 0)
        return self.found
