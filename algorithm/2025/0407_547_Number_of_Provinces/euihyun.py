class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()  

        def dfs(cityI):
            # cityI는 이제 방문했으면 visited에 추가
            cityIConnections = isConnected[cityI]  
            visited.add(cityI)  
            # cityI와 연결된 모든 도시(cityJ)를 확인
            for cityJ in range(N):
                # 아직 방문하지 않았고, 연결되어 있으며, 자기 자신이 아닌 경우 탐색
                if (cityJ not in visited) and (cityIConnections[cityJ] == 1) and (cityI != cityJ):
                    dfs(cityJ)  
            return  

        numProvinces = 0  
        for cityI in range(N):
            # 아직 방문하지 않은 도시부터 dfs
            if cityI not in visited:
                dfs(cityI) 
                numProvinces += 1  
        return numProvinces  
