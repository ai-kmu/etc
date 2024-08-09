from collections import deque


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        q = deque()
        q.append((root, root.val))
        while q:
            node, val = q.popleft()
            if val == targetSum and node.left is None and node.right is None:
                return True
            if node.left is not None:
                q.append((node.left, val + node.left.val))
            if node.right is not None:
                q.append((node.right, val + node.right.val))
        
        return False
        
