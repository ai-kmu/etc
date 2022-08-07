from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # BFS 문제
        # DFS를 사용하게 될 경우 주변과의 차이가 최대 1이 보장되지 않는다.
        m, n = len(isWater), len(isWater[0])
        
        visited = [[False] * n for _ in range(m)]
        height = [[0] * n for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = deque()
        
        # 시작점 찾기
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j, 0))
                    visited[i][j] = True
        
        while queue:
            i, j, h = queue.popleft()
            height[i][j] = h
            
            # 4방향으로 이동하며 높이를 1씩 추가하며 queue에 삽입
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n and not visited[new_i][new_j]:
                    visited[new_i][new_j] = True
                    queue.append((new_i, new_j, h+1))
        
        return height
        
                        
