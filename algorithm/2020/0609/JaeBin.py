# 23. leetCode - Invert Binary Tree

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, root):
        self.root = root

    def invertTree(self, root : TreeNode) -> TreeNode:
        if root == None:
            return root

        tree = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tree

        return root

