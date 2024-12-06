from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        answer = set()
        d = deque()
        d.append(root)
        while d:
            r = d.pop()
            if r.left is not None:
                d.append(r.right)
                d.append(r.left)
                answer.add(r.left.val)
                answer.add(r.right.val)
        
        answer = sorted(list(answer))
        return answer[1] if len(answer) >= 2 else -1
