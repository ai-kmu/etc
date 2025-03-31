class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # dfs 함수 - 함수 내부에 정의해서 로컬 변수 같이 쓰기
        def dfs(curr):
            # 현재 노드 방문 처리
            visited[curr] = True
            for ngbr in range(n):
                # 연결되어 있고 방문한 노드가 아니라면 dfs 재귀
                if isConnected[curr][ngbr] and not visited[ngbr]:
                    dfs(ngbr)

        # 필요한 변수 초기화
        n = len(isConnected)
        visited = [False for _ in range(n)]
        answer = 0

        # 전체 노드 탐색하면서
        for i in range(n):
            # 방문처리가 되지 않았으면 걜 중심으로 하는 province가 있는 거니까 + 1
            if not visited[i]:
                answer += 1
                dfs(i)
        
        return answer
