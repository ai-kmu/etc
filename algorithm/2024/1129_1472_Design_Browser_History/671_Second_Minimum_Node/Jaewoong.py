# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        unique_values = set()
        
        def dfs(node):
            if not node:
                return
            unique_values.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        unique_values = sorted(unique_values)
        
        if len(unique_values) > 1:
            return unique_values[1]
        else:
            return -1 
