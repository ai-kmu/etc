# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(sub, ans):
            if not sub:
                return

            ans += str(sub.val)

            if sub.left == None and sub.right == None:
                result.append(ans)
                return
        
            ans += "->"
            dfs(sub.left, ans)
            dfs(sub.right, ans)
        dfs(root, "")

        return result
