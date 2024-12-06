# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.counter = dict()
        self.dfs(root)
        self.counter = list(self.counter.keys())
        self.counter.sort()
        return self.counter[1] if len(self.counter) > 1 else -1

    def dfs(self, root):
        self.counter[root.val] = True
        if root.left is not None:
            self.dfs(root.left)
        if root.right is not None:
            self.dfs(root.right)
