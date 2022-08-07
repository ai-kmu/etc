from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        
        # 시작점 넣을 큐와 방문한 곳 체크할 set
        q = deque([])
        visited = set()
        
        # 시작점인 물들 넣고 level을 0으로 초기화
        for r in range(row):
            for c in range(col):
                if isWater[r][c]:
                    visited.add((r, c))
                    q.append((r, c))
                    isWater[r][c] = 0
        
        # BFS 정의
        def BFS(r, c, level):
            # 범위 안 벗어나고 방문 안 했으면
            if 0 <= r < row and 0 <= c < col and (r, c) not in visited:
                # 인접한 곳보다 level 1 올리고 visited랑 q에 넣음
                isWater[r][c] = level + 1
                visited.add((r, c))
                q.append((r, c))
        
        # q가 빌 때까지 계속
        while q:
            # BFS에서도 q를 업데이트 하기 때문에
            # 초기 q의 길이 계산해서 for문을 돌려야 한다
            repeat = len(q)
            for _ in range(repeat):
                r, c = q.popleft()
                level = isWater[r][c]
                BFS(r - 1, c, level)
                BFS(r + 1, c, level)
                BFS(r, c - 1, level)
                BFS(r, c + 1, level)
        
        return isWater
