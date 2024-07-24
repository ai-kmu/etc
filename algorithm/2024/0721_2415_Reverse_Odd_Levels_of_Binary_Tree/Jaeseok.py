# complexity : O(N)
from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # level, n : 현재 트리의 레벨과 현재 레벨의 몇번째 노드인지 세는 변수
        level, n = 0, 0
        # q : root부터 차례대로 bfs 순회
        q = deque()
        q.append(root)
        # tmp : level이 even일 때 node의 left와 right의 value를 append, odd일 때 pop
        tmp = deque()
        while q:
            node = q.popleft()
            # level이 even일 경우
            if level % 2 == 0 and node.left is not None:
                tmp.append(node.left.val)
                tmp.append(node.right.val)
            # level이 odd일 경우
            elif tmp:
                node.val = tmp.pop()
            # 마지막 레벨 전까지는 node의 left와 right를 계속 q에 추가
            if node.left is not None:
                q.append(node.left)
                q.append(node.right)
            n += 1
            # perfect binary tree이므로 n이 2의 level 승이 될때마다 다음 level로 이동
            if n == (2 ** level):
                n = 0
                level += 1
                
        return root
        
