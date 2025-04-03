from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        answer = 0
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue
            answer += 1
            visited[i] = True
            # BFS로 연결된 node를 방문
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for j in range(n):
                    if node != j and isConnected[node][j] and not visited[j]:
                        visited[j] = True
                        queue.append(j)
        return answer
