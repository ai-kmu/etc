class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum):
            if not node:
                return False
            
            sum += node.val

            if not node.left and not node.right:
                return sum == targetSum
            
            return dfs(node.left, sum) or dfs(node.right, sum)

        return dfs(root, 0)

        
