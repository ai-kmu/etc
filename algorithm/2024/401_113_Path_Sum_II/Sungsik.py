# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        answer = []
        
        queue = deque([(root, root.val, [root.val])])
        
        # tree를 순회하면서 leaf이며 targetSum과 같을 경우 answer에 append
        while queue:
            node, path_sum, path = queue.popleft()
            
            if node.left is None and node.right is None:
                if path_sum == targetSum:
                    answer.append(path)
                continue
            
            if node.left is not None:
                queue.append((node.left, path_sum + node.left.val, path + [node.left.val]))
                
            if node.right is not None:
                queue.append((node.right, path_sum + node.right.val, path + [node.right.val]))
        
        return answer
                
