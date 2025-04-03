class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        numCity = len(isConnected)
        visited = [False] * numCity

        # dfs 사용
        def dfs(city):
            visited[city] = True  # 방문처리
            for i in range(numCity):
                # 연결되어 있는데 방문 안 했으면 dfs로 계속 탐색
                if not visited[i] and isConnected[city][i] == 1:
                    dfs(i)
        
        for i in range(numCity):
            if not visited[i]:
                ans += 1
                dfs(i)

        return ans
        
