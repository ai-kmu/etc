# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        # print(root.val)
        # print(root.right)
                
        def dfs(node, path):
            if not node.left and not node.right:
                total_path = path + str(node.val)             
                paths.append(total_path)
                return
            
            if node.left:
                dfs(node.left, path + str(node.val) + "->")

            if node.right:
                dfs(node.right, path + str(node.val) + "->")

        paths = []

        dfs(root, "")

        return paths
