# test case만 통과
# DFS를 사용해서 가능한 경로를 모두 구한 다음 경로의 수가 2이상이면 False 반환하는 방법 사용
# 1 1 1 0 0
# 1 1 1 0 0
# 0 0 1 1 0
# 0 0 1 1 1
# => 이런 경우 정답을 못맞힘...

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        dx = [0, 1]
        dy = [1, 0]
        cnt = 0
        m = len(grid)
        n = len(grid[0])

        def DFS(x, y):
            nonlocal cnt

            if cnt > 1:
                return False

            elif x == m-1 and y == n-1:
                cnt += 1
            
            else:
                for i in range(2):
                    nx = x + dy[i]
                    ny = y + dx[i]
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == grid[0][0]:
                            grid[nx][ny] = 0
                            DFS(nx, ny)
                            grid[nx][ny] = 1

        DFS(0, 0)
        return False if cnt > 1 else True
