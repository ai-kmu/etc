class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = deque([root])
        while q:
            node = q.popleft()
            if node == None: continue
            node.left, node.right = node.right, node.left
            q.extend([node.left, node.right])
        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None: return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
