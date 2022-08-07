class Solution(object):
    def longestIncreasingPath(self, matrix): 
        
        # 전체 경로 기록
        path_record = [[0 for _ in matrix[0]] for _ in matrix]
        
        # 방향 설정
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        answer = 0
        
        def explore(i, j, prv_num, path_count = 1):
            nonlocal answer
            nonlocal path_record
            
            # 탐색
            for dy, dx in directions:
                
                # 범위를 벗어나면 return
                if i+dy < 0 or j+dx < 0 or i+dy >= len(matrix) or j+dx >= len(matrix[0]):
                    answer = max(path_count, answer)
                    continue

                # 더 긴 경로가 있다면 return
                if path_record[i+dy][j+dx] >= path_count:
                    answer = max(path_count, answer)
                    continue

                # 현재값이 이전 값보다 작거나 같으면 return(이전값보다 커야함)
                if matrix[i+dy][j+dx] <= prv_num:
                    answer = max(path_count, answer)
                    continue           

                # 경로 기록
                path_record[i+dy][j+dx] = path_count
                
                explore(i+dy, j+dx, matrix[i][j], path_count+1)
                
            return 
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if path_record[i][j] == 0:
                    explore(i, j, -1)
                
        return answer
