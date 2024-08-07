# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        nodes = deque([root])
        queue = deque([root])
        max_path = -float('inf')
        
        # BFS로 모든 노드들 추가
        while queue:
            node = queue.popleft()
            left = node.left
            right = node.right
            if left is not None:
                nodes.append(left)
                queue.append(left)
            if right is not None:
                nodes.append(right)
                queue.append(right)
        
        # Bottom-up으로 순회
        while nodes:
            node = nodes.pop()
            left = node.left
            right = node.right
            
            left_path = node.left.path if left is not None else 0
            right_path = node.right.path if right is not None else 0
            
            # node의 path는 왼쪽과 오른쪽 중 하나만을 취한다
            node.path = max(node.val, node.val + left_path, node.val + right_path)
            
            # max_path는 왼쪽과 오른쪽을 모두 취할수 있다
            max_path = max(max_path, node.val + max(left_path, 0) + max(right_path, 0))
            
        return max_path
