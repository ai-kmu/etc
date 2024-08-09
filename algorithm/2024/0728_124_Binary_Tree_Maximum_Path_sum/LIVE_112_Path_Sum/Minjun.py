

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        self.result = []

        def dfs(node, cur_sum, flag):
            if node is None:
                return
            if node.left is None and node.right is None:
                if cur_sum + node.val == targetSum:
                    self.result.append(True)
                    return
            else:
                dfs(node.left, cur_sum + node.val, flag)
                dfs(node.right, cur_sum + node.val, flag)
        dfs(root, 0, False)
        if True in self.result:
            return True
        else:
            return False
