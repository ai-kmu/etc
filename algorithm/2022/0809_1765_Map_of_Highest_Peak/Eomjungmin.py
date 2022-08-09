from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        
        # bfs 구현을 위한 deque 변수 선언
        queue = deque()
        
        # 정답 출력 행렬
        ans = [[0 for i in range(n)] for j in range(m)]
        
        # 방문 여부 기록하는 행렬
        visited = [[-1 for i in range(n)] for j in range(m)]
        
        '''        
        먼저 queue에 물이 있는 곳의 위치와 높이를 저장
        그리고 먼저 방문했다고 기록함
        '''
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i,j,0))
                    visited[i][j] = 1
        
        '''
        bfs 방법으로 풀어야함
        
        1) 먼저 물이 있는 곳들을 먼저 방문하여
        주변 상하좌우 먼저 높이를 1로 기록
        
        2) 물이 있는 곳들의 주변을 다 방문했으면
        나머지 방문하지 않은 곳들의 경우 문제의 규칙에 따라
        bfs를 이용해 높이를 올려서 저장
        
        '''
        while queue:
            x, y, v = queue.popleft()
            if p[0]+1 < len(isWater):
                if visited[x+1][y] == -1:
                    visited[x+1][y] = 1
                    ans[x+1][y] = v + 1
                    queue.append((x+1, y, ans[x+1][y]))
                    
            if p[0]-1 >= 0:
                if visited[x-1][y] == -1:
                    visited[x-1][y] = 1
                    ans[x-1][y] = v + 1
                    queue.append((x-1, y, ans[x-1][y]))
                    
            if p[1]+1 < len(isWater[0]):
                if visited[x][y+1] == -1:
                    visited[x][y+1] = 1
                    ans[x][y+1] = v + 1
                    queue.append((x, y+1, ans[x][y+1]))
                    
            if p[1]-1 >= 0:
                if visited[x][y-1] == -1:
                    visited[x][y-1] = 1
                    ans[x][y-1] = v + 1
                    queue.append((x, y-1, ans[x][y-1]))
        return ans
