from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visit = [-1 for i in range(len(graph))]              # 색깔 칠하기
        visited = []                                         # 방문한 노드 저장
        way = deque()                                        # BFS 방법을 위한 deque
        
        for idx, start in enumerate(graph):                  # 모든 곳을 방문
            if len(start) == 0 or idx in visited:            # 연결되어 있지 않거나 이미 방문한 곳은 넘어감
                continue
            visited.append(idx)                              # 방문한 노드에 저장
            way = deque(start)                               # 방문할 노드 저장
                                            
            visit[idx] = 0                                   # 이번 노드를 0으로 색깔 칠하기
            for des in start:                                # 연결된 노드들은 1로 색깔 칠하기
                visit[des] = 1
        
            while way:                                       # BFS를 이용하여 연결된 노드들 색깔 칠하기
                start = way.popleft()
                for des in graph[start]:
                    if visit[des] == -1:
                        if visit[start] == 1:
                            visit[des] = 0
                        else:
                            visit[des] = 1
                    else:
                        if visit[start] == visit[des]:       # 만약 인접한 노드 중에 같은 색깔이 있다면 종료
                            return False
                    if des not in visited and des not in way:
                        way.append(des)
                visited.append(start)
        
        return True
