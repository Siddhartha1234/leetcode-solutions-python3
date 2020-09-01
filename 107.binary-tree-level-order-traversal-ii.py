" definition for a binary tree node."


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def parseTree(self, node, lvl):
        if node is None:
            return
        if lvl in self.level:
            self.level[lvl].append(node.val)
        else:
            self.level[lvl] = [node.val]
        if node.left is not None:
            self.parseTree(node.left, lvl + 1)
        if node.right is not None:
            self.parseTree(node.right, lvl + 1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.level = {}
        self.parseTree(root, 0)
        return [self.level[key] for key in reversed(sorted(self.level.keys()))]
