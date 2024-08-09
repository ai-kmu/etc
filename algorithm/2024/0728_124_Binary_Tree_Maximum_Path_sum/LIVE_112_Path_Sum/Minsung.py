# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: 
            return False
        self.target = targetSum
        self.ans = False
        self.dfs(root, 0)
        return self.ans

    def dfs(self, cur_node, cur_sum):
        is_leaf = True
        if cur_node.left is not None:
            self.dfs(cur_node.left, cur_sum+cur_node.val)
            is_leaf = False
        if cur_node.right is not None:
            self.dfs(cur_node.right, cur_sum+cur_node.val)
            is_leaf = False
        if is_leaf and cur_sum+cur_node.val == self.target:
            self.ans = True
