from collections import deque


# BFS를 통해 가장 가까운 0의 depth를 저장
class Solution:
    def updateMatrix(self, mat):
        row = len(mat)
        col = len(mat[0])

        que = deque()

        # 0인 matrix의 index 값을 depth와 함께 que에 저장
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    que.append((i, j, 0))
                else:
                    mat[i][j] = float('inf')

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS
        # que에서 값들을 꺼내며 가장 가까운 0의 depth를 저장
        while que:
            i, j, distance = que.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < row and 0 <= nj < col:
                    if mat[ni][nj] > distance + 1:
                        mat[ni][nj] = distance + 1
                        que.append((ni, nj, distance + 1))
                        
        return mat
