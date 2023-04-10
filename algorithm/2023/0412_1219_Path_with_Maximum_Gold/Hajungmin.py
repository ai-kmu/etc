# 테스트 케이스 하나는 통과하는데 다른 하나를 통과 못함

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # DFS를 수행할 방향 설정
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        # visited를 생성해줄 임시 배열인 check 선언
        check = [['False' for i in range(n)] for j in range(m)]
        # 시작 좌표들을 저장할 start_points 선언
        start_points = []
        
        # grid를 돌며 0이면 check에 True로 넣어주고
        # 0이 아니면 start_points에 좌표를 넣어줌
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    check[i][j] = 'True'        
                else:
                    start_points.append([i, j])
        
        # 각 start_points에서 DFS를 시작할 경우 최대 점수를 저장할 score 선언
        score = [0 for _ in range(len(start_points))]

        def DFS(row, col, visited, curr_score):
            # 가장 높은 점수를 저장할 best_score 선언
            nonlocal best_score
            
            # 현재 좌표를 방문처리 한 후 
            # curr_score에 점수 더해주기
            visited[row][col] = 'True'
            curr_score += grid[row][col]
            
            # 만약 best_score가 curr_score보다 작으면 업데이트
            if best_score < curr_score:
                best_score = curr_score
            
            # 4가지 방향으로 탐색
            for d in range(4):
                new_row = row + dx[d]
                new_col = col + dy[d]

                # 새로운 좌표가 grid의 범위를 넘어가지 않는 경우
                # 이미 방문한 좌표가 아닌 경우
                # 새로운 좌표에 저장된 값이 0이 아닌 경우 DFS 수행
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] != 0 and visited[new_row][new_col] == 'False':
                    DFS(new_row, new_col, visited, curr_score)
                    # DFS를 수행한 후 다시 visited에서 False처리
                    # curr_score에서 값을 빼줌
                    visited[new_row][new_col] = 'False'
                    curr_score -= grid[new_row][new_col]

        # start_points를 돌며 해당 좌표로부터 DFS수행
        for idx in range(len(start_points)):
            s_row, s_col = start_points[idx]
            visited = copy.deepcopy(check)
            best_score = 0
            DFS(s_row, s_col, visited, 0)
            score[idx] = best_score

        # 저장된 값들 중 가장 큰 값 출력
        return max(score)
