class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            # 현재 도시 방문 표시
            visited[city] = True
            
            # 모든 도시를 확인하면서
            for neighbor in range(n):
                # 현재 도시와 이웃 도시가 연결되어 있고, 아직 방문하지 않았다면 DFS 호출
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        n = len(isConnected)  # 도시 수
        visited = [False] * n  # 도시 방문 여부 저장
        provinces = 0  # 결과로 반환할 province 수

        for city in range(n):
            # 방문하지 않은 도시를 시작점으로 DFS 수행
            if not visited[city]:
                dfs(city)
                provinces += 1  # DFS가 끝날 때마다 하나의 province가 끝난 것
        
        return provinces
