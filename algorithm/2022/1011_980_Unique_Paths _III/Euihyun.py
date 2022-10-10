# dfs 해보려고 했는데 실패
# 추가로 공부하고 업데이트 했습니다. 코드리뷰 안해주셔도 됩니다!
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        x = 0
        y = 0
        empty = 1
        
        # 시작점 찾고 
        # 0 이면 갈수있는 곳들 체크
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    x = i
                    y = j
                elif grid[i][j] == 0:
                    empty += 1
        
        def dfs(x, y, empty):
            nonlocal ans
            # 범위를 초과하거나 장애물이 있으면 return
            if  x >= m or x < 0  or y >= n or y < 0 or grid[x][y] == -1: 
                return
            
            # 도착지첨 들어 오면 정답 추가
            if grid[x][y] == 2 :
                if empty == 0:
                    ans += 1
                return
            
            # 이미 갔던 곳은 -1로 바꿔줌
            grid[x][y] = -1
            
            # 네 방향 조회
            dfs(x+1, y, empty-1)
            dfs(x-1, y, empty-1)
            dfs(x, y+1, empty-1)
            dfs(x, y-1, empty-1)

            # 다시 이동가능하게 바꿔줌 
            grid[x][y] = 0
        
        dfs(x,y, empty)
        
        return ans

                    
