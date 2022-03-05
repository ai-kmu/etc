class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[int(ele) for ele in sub] for sub in matrix]  # matrix의 str을 int로 바꾼다.
        
        maxlen = 0  # 최대값 넣을 maxlen
 
        for i in range(len(dp)):  # 만약 1열에 1이 있다면 maxlen = 1
            if dp[i][0] == 1:
                maxlen = 1    
                
        for j in range(len(dp[0])):  # 만약 1행에 1이 있다면 maxlen = 1
            if dp[0][j] == 1:
                maxlen = 1
                
        for i in range(1,len(matrix)):  # 행의 길이 (0인덱스제외), [1,1,1,1]
            for j in range(1,len(matrix[0])):  # 열의 길이 (0인덱스제외), [1,0,1,0,0]
                if dp[i][j]== 1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1  #왼쪽대각선위,위,왼쪽 숫자중 가장 min 한 값에 +1
                    
                    if maxlen < dp[i][j]:  # maxlen 갱신식
                        maxlen = dp[i][j]
        
        
        return maxlen * maxlen  # output
        
        
        
        
        
