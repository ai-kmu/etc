from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        ans = []
        
        # 주어진 matrix를 순회하면서 0인 위치를 ans 리스트에 저장하고, 나머지는 '#'으로 표시
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans.append((i, j))
                else:
                    mat[i][j] = "#"

        # BFS를 사용하여 0인 위치에서부터의 거리를 계산하여 행렬 갱신
        for row, col in ans:
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                new_row = row + dx
                new_col = col + dy
                # 탐색할 위치가 행렬을 벗어나지 않고 1인 위치에 해당하고 방문한 적이 없으면
                if 0 <= new_row < n and 0 <= new_col < m and mat[new_row][new_col] == "#":
                    # 이전 거리에서 1을 더하여 현재 위치의 거리 갱신
                    mat[new_row][new_col] = mat[row][col] + 1
                    ans.append((new_row, new_col))

        # 최종 갱신된 행렬 반환
        return mat
