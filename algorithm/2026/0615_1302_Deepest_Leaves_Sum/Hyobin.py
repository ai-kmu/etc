# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest_sum = 0
        cnt = 0
        
        def dfs(node, depth):
            nonlocal deepest_sum, cnt

            if not node:
                return

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

            if cnt < depth:
                cnt = depth
                deepest_sum = 0

            if cnt == depth:
                deepest_sum += node.val
        
        dfs(root, 0)
        
        return deepest_sum
