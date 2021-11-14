class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        longest = float('-inf') # 가장 긴 값. 선언할 수 있는 가장 작은 수를 먼저 선언해놓는다.
        
        memo = dict() # memoization 사용하여
        
        for i in range(len(matrix)): # matrix 전체를 dfs로 탐색한다.
            for j in range(len(matrix[0])):
                longest = max(longest, self.dfs(matrix, i, j, memo))
                
        return longest
    
    def dfs(self, matrix, row, col, memo):
        if (row, col) in memo: # 만약 memo해둔 것이 있다면 바로 리턴이 가능함.
            return memo[(row, col)]

        path_len = 0 # 만약 memo에 없는 상황이라면,
        for r, c in [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]: # 해당 i, j값으로부터 상하좌우를 탐색
            if r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0]): # matrix의 범위를 벗어나지 않는 선에서
                if matrix[r][c] > matrix[row][col]: # 상하좌우 각각 탐색했을 때, 현재 i,j에 위치한 값보다 크면
                    path_len = max(path_len, self.dfs(matrix, r, c, memo)) # recursive로 탐색한 값과 현재의 경로 길이를 비교하여 더 큰값을 뽑아냄
                    
            
        memo[(row, col)] = path_len+1 # 경로의 길이를 메모에 저장해두고
        return path_len+1 # 최대 길이 리턴.
