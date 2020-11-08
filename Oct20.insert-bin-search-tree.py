# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
        else:
            curr = root
            while True:
                if curr.val < val:
                    if curr.right is None:
                        curr.right = TreeNode(val)
                        break
                    curr = curr.right
                else:
                    if curr.left is None:
                        curr.left = TreeNode(val)
                        break
                    curr = curr.left
        
        return root
