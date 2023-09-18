from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        q = deque()
        # BFS로 풀이
        q.append((root.val, root.val, root.left, root.right))
        while q:
            # 최댓값, 현재 노드의 값, 노드의 왼쪽과 오른쪽을 큐에서 꺼냄
            max_, val, left, right = q.popleft()
            # 만약 현재 노드의 값이 지금까지의 최댓값보다 크다면 good node이므로 answer에 1을 더해줌
            if val >= max_:
                answer += 1
                max_ = val
            # left 노드가 비어있지 않다면 최댓값, 왼쪽 노드의 값, 노드의 왼쪽과 오른쪽을 큐에 추가
            if left is not None:
                q.append((max_, left.val, left.left, left.right))
            # right 노드가 비어있지 않다면 최댓값, 오른쪽 노드의 값, 노드의 왼쪽과 오른쪽을 큐에 추가
            if right is not None:
                q.append((max_, right.val, right.left, right.right))
        return answer
