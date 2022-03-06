class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # DP
        '''
        어떤 좌표를 기준으로 그 좌표를 둘러싼 좌,상단의 좌표가 정사각형을 이루는 경우에는
        해당 좌표를 포함한 정사각형을 그릴 수 있다.
        이 경우, 해당 좌표를 포함한 정사각형이 최대 정사각형이다.
        '''
        # 점화식: dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1
        
        
        rows = len(matrix)  
        cols = len(matrix[0]) 
        
        # dp 생성 (rows행 cols열 크기 0 배열)
        dp = [[0]*cols for i in range(rows)]  
        
        # 최대 길이
        max_cnt = 0  
        
        for row in range(rows):
            for col in range(cols):
                # dp값 할당
                dp[row][col] = int(matrix[row][col])  
                
                # dp에 값이 할당됐다면(1), 최대 길이 1
                if dp[row][col]:  
                    max_cnt = 1 
        
        for i in range(1,rows):
            for j in range(1,cols):
                # dp 값이 0 아니라면 (정사각형 이루고 있다면) 좌,상단 비교한다
                if dp[i][j] != 0:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    
                    max_cnt = max(max_cnt, dp[i][j])
        
        # 정사각형 넓이 = 길이 제곱  
        return max_cnt ** 2

'''
원래 풀려던 방식
mxn 행렬에서 가질 수 있는 최대 정사각형 크기부터
정사각형 필터를 만들어서 탐지하고, 크기를 줄여가면서
찾는 순간 max값이므로 종료.
구현 실패,,
'''

# 기존 코드    
'''

        m,n >= 1 -> 1   m,n -> m,n**2
        m,n >= 2 -> 4   m,n**2
        m,n >= 3 -> 9   m,n**2
        ==> m,n 일 때 가능한 최대 정사각형은 min(m,n)**2
        
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        a = min(m,n)
    
   
    def findMax(self, a):
    
        
        a 정사각형 가능한 최대 값 -> a**2
        a-1 -> a-1**2
        a-2 -> a-2**2
        a-a+1 -> 1
            
        for i in range a:
            matrix[m-i][n-i]
'''
