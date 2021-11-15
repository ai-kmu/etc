class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
            # dfs 알고리즘으로 한 요소에서 최대로 갈 수 있는 path의 최대 길이를 계산
            # 최소한 한 지점에서의 path길이는 1부터 시작하므로 dfs 함수에서 
            # 길이(l)를 1로 시작한다.
            # 그리고 한 요소에서 주변 4개 방향요소를 보면서 문제의 조건에 부합하면
            # 길이를 늘려서 max를 이용해 최대로 갈 수 있는 path길이를 계산
            @cache
            def dfs(i,j):
                current = matrix[i][j]
                l = 1
                if j < len(matrix[0])-1 and current < matrix[i][j+1]:
                    l = max(l, 1+dfs(i,j+1))                 
                    
                if j >= 1 and current < matrix[i][j-1]:
                    l = max(l, 1+dfs(i,j-1))                  
                    
                if i < len(matrix)-1 and current < matrix[i+1][j]:
                    l = max(l, 1+dfs(i+1,j))               
            
                if i >= 1 and current < matrix[i-1][j]:
                    l = max(l, 1+dfs(i-1,j))     
                
                return l
                    
            result = max(dfs(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])))
                    
            return result
