from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        answer = 0
        row , col = len(matrix),len(matrix[0])
        # 마지막 열의 수를 한 행의 합으로 바꾼다. sub matrix의 합을 이용
        for r in range(row):
            for c in range(1,col):
                matrix[r][c] += matrix[r][c-1]
        
        for i in range(col):
            for j in range(i,col):
                dic = defaultdict( int )
                dic[0] += 1
                sum = 0 
                
                for k in range(row):
                    sum += matrix[k][j] - (0 if i == 0 else matrix[k][i-1])
                    if sum - target in dic:
                        answer += dic[sum - target]
                    dic[sum] += 1
        return answer
