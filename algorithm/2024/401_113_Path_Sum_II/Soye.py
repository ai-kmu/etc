class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []

        # currentNode, currentSum, targetSum, path
        self.dfs(root, root.val, targetSum, [root.val])

        return self.ans


    def dfs(self, node, currentSum, targetSum, path):
        if not node.left and not node.right and currentSum != targetSum:
            return

        if not node.left and not node.right and currentSum == targetSum:
            self.ans.append(path)
            return
        
        if node.left:
            self.dfs(node.left, currentSum + node.left.val, targetSum, path + [node.left.val])
        if node.right:
            self.dfs(node.right, currentSum + node.right.val, targetSum, path + [node.right.val])
