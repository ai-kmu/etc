# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 왼쪽 탐색부터 그다음 오른쪽 반복 in-order
        stack = deque([])
        inorder_arr = []
        curr = root
        while curr is not None or stack:
            # 왼쪽 계속 넣어주고
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            # curr를 맨 left에서부터 시작
            curr = stack.pop()
            # 값 넣어주기
            inorder_arr.append(curr.val)
            # 본인의 right subtree 탐색
            curr = curr.right
        
        return inorder_arr[k-1]
        
