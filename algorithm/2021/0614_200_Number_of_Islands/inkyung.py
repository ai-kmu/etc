class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w = len(grid[0])
        h = len(grid)
        
        cols = [0, 0, 1, -1]
        rows = [1, -1, 0, 0]
        
        def isRange(row, col):
            if col >= w or col < 0: return False
            if row >= h or row < 0: return False
            return True
        
        def bfs(cur_row, cur_col):
            # 현재 육지를 que에 넣어줌
            que = [(cur_row, cur_col)]
            
            while que:
                # 현재 위치를 꺼내주고
                row, col = que.pop(0)
                # 방문한 곳이니 0으로 표시
                grid[row][col] = "0"
                # 8방향을 탐색
                for i in range(4):
                    new_row = row + rows[i]
                    new_col = col + cols[i]
                    
                    # 전체 배열안에 있으면서 육지이면
                    if isRange(new_row, new_col) == True and grid[new_row][new_col] == "1":
                            # 육지이면 0으로 바꿔주고 que에 넣어줌
                            grid[new_row][new_col] = "0"
                            que.append((new_row, new_col))
        
        answer = 0
            
        for i in range(h):
            for j in range(w):
                # 먼저 육지인 곳을 찾고
                if grid[i][j] == "1":
                    bfs(i, j)
                    # 육지를 다 돌았으면 1을 추가
                    answer += 1
        return answer
        
        
:wq!
