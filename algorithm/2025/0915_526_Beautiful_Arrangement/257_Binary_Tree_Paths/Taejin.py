# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ret = []
    
    def binaryTreePaths(self, root: Optional[TreeNode], path="") -> List[str]:
        if root.left is None and root.right is None:
            self.ret.append(f"{path}{root.val}")

        else:
            if root.left:
                self.binaryTreePaths(root.left, f"{path}{root.val}->")

            if root.right:
                self.binaryTreePaths(root.right, f"{path}{root.val}->")

        return self.ret

        
