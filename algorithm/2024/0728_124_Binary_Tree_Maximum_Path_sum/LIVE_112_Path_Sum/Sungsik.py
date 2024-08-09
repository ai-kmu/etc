# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def dfs(node, val):
            if node.left is None and node.right is None:
                return val == targetSum
            
            answer = False
            if node.left is not None:
                answer |= dfs(node.left, val + node.left.val)
            if node.right is not None:
                answer |= dfs(node.right, val + node.right.val)
            return answer
        
        return dfs(root, root.val)
