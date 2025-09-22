# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node:TreeNode, current_path:str) :
            if node is None :
                return

            if not current_path:
                current_path = str(node.val)
            else:
                current_path = current_path + "->" + str(node.val)

            if node.left is None and node.right is None :
                ans.append(current_path)
                return

            if node.left :
                dfs(node.left, current_path)

            if node.right :
                dfs(node.right, current_path)

        dfs(root, "")

        return ans
