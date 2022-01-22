# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        
        #  순회를 했을때 정렬이 되도록, 중위순회를 사용하였다.
        
        def traversal(root):
            
            if root is None:
                pass
            
            else:
                traversal(root.left)
                result.append(root.val)
                traversal(root.right)
            
        traversal(root)
        return result[k-1]
