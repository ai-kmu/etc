# 풀이 실패해서 정답 보고 공부했습니다...
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        if not grid:
            return False

        # 방문한 곳은 재방문하지 않기 위함
        visited = set()
        
        def dfs(position, visited, prev, count):
            i,j = position
            char = grid[i][j]
            visited.add((i,j))
            for r,c in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                # 범위를 벗어나지 않고, 방문한 곳은 아니어야 하고, 같은 단어여야함
                if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == char and (r,c) != prev:
                    # 조건에 맞는 위치를 찾으면 사이클을 찾은것
                    if (r,c) in visited and count >= 4:
                        return True
                    elif (r,c) not in visited:
                        val = dfs((r,c), visited, (i,j), count+1)
                        if val is True:
                            return val
         
        # dfs 적용
        for i in range(len(grid)):
            for j in range(len(grid[0])):
			    # 방문한 곳은 재방문 하지 않음
                if (i,j) not in visited:
                    val = dfs((i,j), visited, None, 1)
                    if val is True:
                        return val
        
        return False
