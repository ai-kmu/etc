class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)
        # 구간마다 얼마나 점수차이가 발생하는지 저장하기 위한 2차원 배열
        dp = [[0]*n for i in range(n)]
        
        # 루프를 돌며 start와 end범위를 바꿔가며 사이의 플레이어 사이의 점수차이 계산
        for i in range(n):
            for start in range(n - i):
                # end의 범위를 바꿔주며 탐색
                end = start + i
                # 처음 열을 nums로 채워줌
                if start == end: 
                    dp[start][end] = nums[start]
                # 현재 범위에서 나올 수 있는 가장 큰 점수차이를 dp 배열에 업데이트해줌
                else:
                    dp[start][end] = max(nums[end] - dp[start][end - 1], nums[start] - dp[start + 1][end])
        
        # 점수가 양수면 플레이어1의 승리이기 때문에 0이상일 경우 true를 반환
        return dp[0][-1] >= 0
