# dp로 품
# dfs로 완전 모든 행렬의 longest increasing path를 구함
# 이 때 현재 칸의 longest increasing path 값을 dp에 저장해 놓음

import numpy as np

class Solution:
    def dfs(self, x, y):
        if self.dp[y][x] > 0:
            return self.dp[y][x]
        else:
            self.dp[y][x] = 1
            # 4방향 모두 탐색
            up = self.dfs(x, y - 1) if (y-1 >=0 and self.matrix[y-1][x] > self.matrix[y][x]) else 0
            down = self.dfs(x, y + 1) if (y+1 < self.y_len and self.matrix[y+1][x] > self.matrix[y][x]) else 0
            left = self.dfs(x - 1, y) if (x-1 >=0 and self.matrix[y][x - 1] > self.matrix[y][x]) else 0
            right = self.dfs(x + 1, y) if (x+1 < self.x_len and self.matrix[y][x+1] > self.matrix[y][x]) else 0
            
            # 4방향중 가장 높은 값을 현재 칸에 추가시켜줌
            self.dp[y][x] += max(up, down, left, right)
            return self.dp[y][x]
        
    def longestIncreasingPath(self, matrix):
        self.dp = np.zeros_like(matrix)
        self.matrix = matrix
        self.y_len, self.x_len = self.dp.shape
        
        # dfs로 모든 칸을 탐색
        for i in range(self.y_len):
            for j in range(self.x_len):
                self.dfs(j, i)
        
        return np.max(self.dp)
        
