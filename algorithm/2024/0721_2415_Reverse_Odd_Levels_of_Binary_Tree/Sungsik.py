# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # odd level의 node의 val을 바꾸는 함수
        def swap(nodes):
            n = len(nodes)
            for i in range(n // 2):
                nodes[i].val, nodes[n-i-1].val = nodes[n-i-1].val, nodes[i].val
        
        if root.left is None:
            return root
        queue = deque([(1, root.left), (1, root.right)])
        tmp_level = 0
        nodes = []
        
        while queue:
            level, node = queue.popleft()
            if node.left is not None:
                queue.append((level + 1, node.left))
                queue.append((level + 1, node.right))
            
            if tmp_level != level:
                # even level에 진입할 경우 이전 odd level의 node들을 swap
                if tmp_level % 2 == 1:
                    swap(nodes)
                    nodes = []
                tmp_level = level
            
            # odd level일 경우 nodes에 node를 저장
            if level % 2 == 1:
                nodes.append(node)
        
        if tmp_level % 2 == 1:
            swap(nodes)

        return root
            
