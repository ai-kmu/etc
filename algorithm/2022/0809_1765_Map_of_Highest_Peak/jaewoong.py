#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        
        res = [[0 for _ in range(n)] for _ in range(m)] #높이를 기록하는 res 배열을 0으로 초기화
        q = collections.deque([]) #BFS의 deque 형태 활용을 위해 deque를 줌
        
        visited = set()
        #큐에 물의 위치들과 높이(0)을 넣어줍니다.
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append([[i, j], 0])
                    visited.add((i, j))
        #상하좌우 이동을 위한 벡터
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        #큐를 하나씩 빼보면서 인접한 영역에 방문하지 않았으면 방문합니다.
        while q:
            curr, value = q.popleft()
            x, y = curr
            for i, j in zip(dx, dy): #상하좌우 이동을 하면서
                nx = x + i
                ny = y + j
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited: #방문하지 않은것에 대해 방문
                        visited.add((nx, ny))
                        q.append([[nx, ny], value+1])
                        res[nx][ny] = value + 1
        
        return res

