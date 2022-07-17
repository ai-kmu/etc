from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # bfs
        queue = deque([(root, 0)])
        # height마다 마지막 node 저장
        # node의 최대 개수는 100 => height의 최댓값도 100
        answer = [None] * 100
        
        while queue:
            node, height = queue.popleft()
            # bfs를 사용하므로 각 height마다 오른쪽에 있는 node가 덮어쓰게 됨
            answer[height] = node.val
            if node.left:
                queue.append((node.left, height+1))
            if node.right:
                queue.append((node.right, height+1))
            
        return filter(lambda x: x != None, answer)
            
