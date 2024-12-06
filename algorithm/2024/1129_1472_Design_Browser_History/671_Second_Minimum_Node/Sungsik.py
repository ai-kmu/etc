# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root.left is None:
            return -1
        
        candidates = []
        nodes = deque([root])
        
        while nodes:
            node = nodes.popleft()
            
            if node.left is not None:
                if node.val != node.left.val:
                    candidates.append(node.left.val)
                else:
                    nodes.append(node.left)
            
                if node.val != node.right.val:
                    candidates.append(node.right.val)
                else:
                    nodes.append(node.right)
        
        if not candidates:
            return -1
        
        answer = min(candidates)
        
        return answer if answer != root.val else -1
        
