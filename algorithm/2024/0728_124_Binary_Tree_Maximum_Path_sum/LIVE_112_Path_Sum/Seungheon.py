class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False

        answer = False

        def dfs(node=root, node_sum=0):
            nonlocal answer

            node_sum += node.val
            if node.left is not None:
                dfs(node.left,  node_sum)
            if node.right is not None:
                dfs(node.right, node_sum)

            if not node.right and not node.left:
                if targetSum == node_sum:
                    answer = True

            return

        dfs()

        return answer
