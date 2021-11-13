class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # 방문한 횟수 체크
        visited_cnt = [[-1 for _ in range(n)] for _ in range(m)]
        
        # dfs로 현재 위치에서 갈 수 있는 최대한 가기
        def dfs(row, col, mat, visited_cnt):
            if visited_cnt[row][col] != -1:
                return visited_cnt[row][col]
            else:
                temp_cnt = [0]
                # 4방향에 대해서 모두 dfs 수행
                for i, j in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    next_r, next_c = row+i, col+j
                    if 0 <= next_r < m and 0 <= next_c < n and mat[row][col] < mat[next_r][next_c]:
                        temp_cnt.append(dfs(next_r, next_c, mat, visited_cnt))
                visited_cnt[row][col] = 1+ max(temp_cnt)
            
            # 현재 위치에서의 가장 긴 path return
            return visited_cnt[row][col]
                
        
        answer = 0
        # 모든 r, c에 대하여 수행
        for r in range(m):
            for c in range(n):
                answer = max(answer, dfs(r, c, matrix, visited_cnt))
                
                
        return answer
