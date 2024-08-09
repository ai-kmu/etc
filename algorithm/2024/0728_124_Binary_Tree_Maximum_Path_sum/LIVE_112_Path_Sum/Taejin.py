# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:   
        def dfs(node, targetSum):
            if node is None:
                return False
            
            elif node.left is None and node.right is None:
                if targetSum == node.val:
                    return True

                else:
                    return False
                    
            return dfs(node.left, targetSum - node.val) or dfs(node.right, targetSum - node.val)

        return dfs(root, targetSum)

            
        
