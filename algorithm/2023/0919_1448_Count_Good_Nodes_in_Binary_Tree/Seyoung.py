# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            res = int(root.val >= max_val)
            if root.left:
                res += dfs(root.left, max(max_val, root.val))
            if root.right:
                res += dfs(root.right, max(max_val, root.val))
            return res
        
        return dfs(root, -10000)
