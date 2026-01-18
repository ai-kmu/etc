# 솔루션참고
from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        # 그래프 생성 (인접 리스트)
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        
        visited = set()
        answer = float('inf')  # 최소 간선 값을 저장할 변수

        def dfs(city):
            nonlocal answer
            visited.add(city)

            # 현재 도시에서 연결된 모든 도로 확인
            for next_city, dist in graph[city]:
                # 도로 거리 중 최소값 갱신
                answer = min(answer, dist)

                # 아직 방문하지 않았다면 계속 탐색
                if next_city not in visited:
                    dfs(next_city)

        # 도시 1부터 DFS 시작
        dfs(1)

        return answer
