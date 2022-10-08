class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        # target_num은 시작점부터이므로 1부터 시작
        target_num = 1
        
        # 총 지나야하는 칸 수와 시작 점을 구해줌
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    y = i
                    x = j
                    
                if grid[i][j] == 0:
                    target_num += 1
        
        # 현재 지나온 칸의 수와 정답
        count_path = 0
        ans = 0
        
        # DFS 수행
        # 이 때 nonlocal을 통해 count_path와 ans 변수를 수정할 수 있도록 함
        def DFS(y, x):  
            nonlocal count_path
            nonlocal ans

            # 만약 현재 1이라면 count_path에 1 추가
            if grid[y][x] == 1:
                count_path += 1
                
                # 현재 방문처리가 되었다면 4방향으로 탐색
                for i in range(4):
                    dy, dx = direction[i]
                    ny = y + dy
                    nx = x + dx
                    
                    # 만약 현재 0이라면 1로 방문처리한 후 DFS수행
                    # DFS를 종료한 후에는 현재 칸을 다시 0으로 돌려주고 count_path 1 빼줌
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == 0:
                        grid[ny][nx] = 1
                        DFS(ny, nx)
                        count_path -= 1
                        grid[ny][nx] = 0
                    
                    # 현재 칸이 2이고 count_path가 target_num과 같으면 정답에 1 더해줌
                    elif 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == 2 and count_path == target_num:
                        ans += 1
        
        # 시작점을 넣고 DFS 수행
        DFS(y, x)
        return ans
