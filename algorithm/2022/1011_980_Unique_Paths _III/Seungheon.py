import copy

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:    
        
        len_row = len(grid)
        len_col = len(grid[0])
        
        # start_point와 path_count(장애물 수)구하기
        start_point = [] 
        path_count = 1
        for row in range(len_row):
            for col in range(len_col):
                if grid[row][col] == 1:
                    start_point = [row, col]
                    grid[row][col] = 0
                if grid[row][col] == -1:
                    path_count += 1
        
        # DFS, Backtracking
        
        answer = 0
        
        def explore(cur_i = start_point[0], cur_j = start_point[1], path_count = path_count):
            nonlocal answer
            
            # 방문 & 벽 처리
            if grid[cur_i][cur_j] == -1:
                return

            # answer 조건
            # 조건 : 최종위치에 도달했을때 path_count(이동횟수 + 장애물수) 가 grid의 크기와 같으면 answer += 1
            if grid[cur_i][cur_j] == 2:
                if path_count == len_row * len_col:
                    answer += 1 
                return
            
            grid[cur_i][cur_j] = -1
            
            for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nxt_i, nxt_j = cur_i+dy, cur_j+dx
                if nxt_i < 0 or nxt_j < 0 or nxt_i >= len_row or nxt_j >= len_col: 
                    continue
                tmp = grid[nxt_i][nxt_j]
                explore(cur_i+dy, cur_j+dx, path_count+1)
                grid[cur_i+dy][cur_j+dx] = tmp
                
                # try except로 하려했으나 잘 안됨
                # -> 재귀함수와 try except를 같이쓰면 꼬이는것 같긴한데 어디서 꼬이는지 잘 모르겠음
                # try:
                #     tmp = grid[cur_i+dy][cur_j+dx]
                # except:
                #     continue
                # 
                # explore(cur_i+dy, cur_j+dx, path_count+1)
                # grid[cur_i+dy][cur_j+dx] = tmp
                
        explore()
        
        return answer
