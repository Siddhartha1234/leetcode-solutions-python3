# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def parse(self, left, right):
        if left is None and right is None:
            return True
        
        if left is not None and right is None:
            return False
        
        if left is None and right is not None:
            return False
        
        return left.val == right.val and self.parse(left.left, right.right) and self.parse(left.right, right.left)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.parse(root.left, root.right)
