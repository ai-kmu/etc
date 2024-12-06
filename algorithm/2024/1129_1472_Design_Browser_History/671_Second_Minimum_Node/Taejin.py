# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        val_set = set()

        while queue:
            node = queue.popleft()

            if node is not None:
                val_set.add(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return -1 if len(val_set) < 2 else sorted(list(val_set))[1]
