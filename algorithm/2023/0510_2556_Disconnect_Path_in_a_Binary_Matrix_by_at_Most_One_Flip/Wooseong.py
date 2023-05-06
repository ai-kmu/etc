class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        # dfs로 가능한 경로 찾아내서
        # 2개 이상이면 false, 1개 이하면 true 반환

        # m, n 찾기
        m, n = len(grid), len(grid[0])
        
        # 예외 케이스
        if (m, n) in ((1, 1), (1, 2), (2, 1)):
            return False
        
        # 짧은 곳을 먼저 탐색하는 게 효율적임
        go_down = m < n

        # dfs
        def dfs(r, c):
            # 끝 점 도달 == 경로 찾음!
            if r == m - 1 and c == n - 1:
                return True
            
            # 범위 벗어남 or 0 발견 == 경로 없음!
            if r >= m or c >= n or not grid[r][c]:
                return False
            
            # visited
            grid[r][c] = 0
            
            if (r, c) != (0, 0):
                # 모든 경로를 찾을 필요가 없음
                # 출발점이 아니라면 찾는 즉시 return True 하면 됨
                # 출발점에서 오른쪽, 아래 모두 경로가 없으면 return False
                # 따라서 or 연산
                if go_down:
                    return dfs(r + 1, c) or dfs(r, c + 1)
                else:
                    return dfs(r, c + 1) or dfs(r + 1, c)

            # 출발점이라면 => 최종 return 값
            # 오른쪽으로 갔을 때랑 왼쪽으로 갔을 때 중에
            # 둘 다 경로가 있는 경우를 제외하고 나머지 True
            if go_down:
                if dfs(r + 1, c):
                    return not dfs(r, c + 1)
                else:
                    return True
            else:
                if dfs(r, c + 1):
                    return not dfs(r + 1, c)
                else:
                    return True
        
        # (0, 0)에서 시작
        return dfs(0, 0)
