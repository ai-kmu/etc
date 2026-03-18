# 나와 인접한 행 중 나 포함 좌우 3개 열만 탐색해서 계산하고, 이를 전부 계산하면 됨. 
# 완전 탐색의 경우 3^n-1승임
# 점화식 세워서 dp로 가즈아
# 내 위에 행 3개 열에 대해서 최소값 더해가기
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix) for i in range(len(matrix))]
        # 첫행 나로 초기화
        for i in range(len(matrix)):
            dp[0][i] = matrix[0][i]
        # 두번째 행부터 바로 윗 행에서 나포함 좌우 탐색해서 최소값 더함
        for row in range(1, len(matrix)):
            for col in range(len(matrix)):
                tmp = dp[row-1][col]
                if col > 0:
                    if tmp > dp[row-1][col-1]:
                        tmp = min(dp[row-1][col-1], tmp)
                if col < len(matrix)-1:
                    if tmp > dp[row-1][col+1]:
                        tmp = min(dp[row-1][col+1], tmp)
                dp[row][col] = tmp + matrix[row][col]
        return min(dp[-1])
