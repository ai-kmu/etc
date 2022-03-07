class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        h = len(matrix)
        
        w = len(matrix[0])
        
            ''' 
            (feedback)
    
            dp matrix를 0으로 초기화한 이후 => 이중 for문 돌려서 matrix 값을 할당했는데 (이중 for문 한번 + for 문 한번)
            list comprehension이나 map 함수 등을 이용해서 이중 for문 내에서 같이 str type => int type으로 변경하는 방법

            혹은 이중 for문을 이용할거면 다음과 같은 코드로 한번에 변경하는 것이 조금 더 효율적이지 않을까 싶습니다.
            for i in range(h):
                dp.append([])
                for j in range(w):
                    dp[i].append(int(matrix[i][j]))
                    
             ''' 
        
        dp = [[0]*w for _ in range(h)]

        res = 0
        
        for i in range(h):
            for j in range(w):
                dp[i][j] = int(matrix[i][j])
                if dp[i][j]:
                    res = 1
        
        for i in range(1, h):
            for j in range(1, w):
                
            
                if dp[i][j] and dp[i-1][j] and dp[i][j-1] and dp[i-1][j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

                    res = max(res, dp[i][j])

        return res**2

        
