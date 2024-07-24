# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        
        while q:
            if level % 2 == 0:  # evenLevel
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                        q.append(node.right)
                
            else:  # oddLevel
                oddLevel = []
                for _ in range(len(q)):
                    node = q.popleft()
                    oddLevel.append(node)
                    if node.left:
                        q.append(node.left)
                        q.append(node.right)
                        
                # reverse
                n = len(oddLevel)
                for i in range(n // 2):
                    oddLevel[i].val, oddLevel[n - 1 - i].val = oddLevel[n - 1 - i].val, oddLevel[i].val
                    
            level += 1
                
        return root
