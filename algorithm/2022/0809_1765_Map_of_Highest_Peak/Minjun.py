from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        hmap = [[-1 for i in range(len(isWater[0]))] for j in range(len(isWater))]
        visit = []

        # 방문하지 않았고, 인덱스 범위를 벗어나지 않는다면,
        # 현재 높이보다 +1 해주고, 해당 위치를 queue에 넣는다.
        def bfs(i,j):
            if hmap[i-1][j] == -1 and i > 0:
                hmap[i-1][j] = hmap[i][j] +1
                queue.append([i-1,j])
            if i < len(isWater) - 1 and hmap[i+1][j] == -1 :
                hmap[i+1][j] = hmap[i][j] +1
                queue.append([i+1,j])
            if hmap[i][j-1] == -1 and j > 0:
                hmap[i][j-1] = hmap[i][j] +1
                queue.append([i,j-1])
            if j < len(isWater[0]) - 1 and hmap[i][j+1] == -1 :
                hmap[i][j+1] = hmap[i][j] +1
                queue.append([i,j+1])
        
        # water 위치를 queue에 다 넣는다.
        for i, k in enumerate(isWater):
            for j in range(len(k)):
                if isWater[i][j] == 1:
                    hmap[i][j] = 0
                    queue.append([i,j])
        
        # queue 빌때까지 해준다.
        while queue:
            a = queue.popleft()
            bfs(a[0],a[1])
            
        return hmap
