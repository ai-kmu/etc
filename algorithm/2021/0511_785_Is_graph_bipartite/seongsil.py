#BFS

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [-1] * n # 이 노드들은 Untouched 된것임을 표시
        
        for i in range(n):
            if col[i] != -1:
                continue
            q = deque()
            q.append((0,0)) # 첫번째 노드 color는 0

            while q:
                node, color = q.popleft()
                if col[node] == -1: # untouched 였으면 touched로 바꿔줌
                    col[node] = color
                    for g in graph[node]:
                        q.append((g, color^1)) #0이면 1, 1이면 0으로 반환
                
                if col[node] != color:
                    return False
            
            return True
