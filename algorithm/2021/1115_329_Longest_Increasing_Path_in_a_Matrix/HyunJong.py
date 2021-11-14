class Solution(object):
    def longestIncreasingPath(self, matrix):

        xlen = len(matrix)
        ylen = len(matrix[0])
        zero_matrix =[] ## 길이저장용 matrix
        result = 0 

        for i in range(xlen): ## matrix와 같은 크기, 요소값은 0인 행렬 생성
            x_list =[]
            for j in range(ylen):
                x_list.append(0)
            zero_matrix.append(x_list)
            
            
        def dfs(x, y): ## dfs
            move = [(0, 1), (1, 0), (0, -1), (-1, 0)] ## 4방향 지정
            if zero_matrix[x][y] !=0: ## 한번 방문했으면 그 위치에서 커지는 방향의 길이가 저장되어 있다 
                return zero_matrix[x][y]  ## 그 값을 return하면 된다.
            for mv in move: ## 4방향으로 움직이기
                x_ = x + mv[0] 
                y_ = y + mv[1]
                if 0<= x_ and x_ < xlen and 0<=y_ and y_ < ylen and matrix[x_][y_] > matrix[x][y]:
                    ## 조건, 움직일 방향이 matrix범위안에 존재, 움직인 방향이 기존 값보다 커야된다.
                
                    zero_matrix[x][y] = max(zero_matrix[x][y], dfs(x_, y_))
                    ## 업데이트되는 path 길이 중에서 가장 큰값만 저장
                
            zero_matrix[x][y] += 1     
            return zero_matrix[x][y]   
            
            
        for x in range(xlen): ## 모든 matrix 모든요소 dfs 탐색
            for y in range(ylen):
                result = max(result, dfs(x, y))
                
        return result
