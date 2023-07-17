from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]  # 방문 여부를 저장하는 2차원 배열

        def dfs(row, col, start_row, start_col, count):
            if visited[row][col]:
                return count - visited[row][col] >= 4  # 주기의 길이가 4 이상인지 확인
…            for j in range(n):
                if not visited[i][j] and dfs(i, j, i, j, 1):
                    return True
        return False
