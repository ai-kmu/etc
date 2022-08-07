class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 이미 들른 곳을 기록하기 위한 행렬 선언
        visited = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        def dfs(i,j):
            # 현재 위치에서의 값
            cur = matrix[i][j]
            
            # 현 위치에서 path 길이 초기화
            l = 1
            
            # 이미 전에 들른 곳이면 바로 그 위치에서의 최대 길이 값 리턴
            if visited[i][j] > 0:
                return visited[i][j]
            
            # 현 위치에서 위, 아래, 왼쪽, 오른쪽 dfs 탐색하여 현 위치에서 최대 path 길이 출력
            # 문제 조건에 맞게 이동하면서 path 길이 증가
            if i+1 < len(matrix) and cur < matrix[i+1][j]:
                l = max(l, 1 + dfs(i+1, j))
            
            if i-1 >= 0 and cur < matrix[i-1][j]:
                l = max(l, 1 + dfs(i-1, j))
                
            if j+1 < len(matrix[0]) and cur < matrix[i][j+1]:
                l = max(l, 1 + dfs(i, j+1))
                
            if j-1 >= 0 and cur < matrix[i][j-1]:
                l = max(l, 1 + dfs(i, j-1))
                
            # 현 위치에서 최대 path 길이 기록
            visited[i][j] = l
            
            return l
        
        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i,j))
                
        return res
