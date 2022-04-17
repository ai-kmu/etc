class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # DP를 활용한 풀이
        # 
        # [i, j] 범위의 nums에서 해당 턴의 플레이어가 얻을 수 있는 최대 스코어를 S(i, j)이라고 했을 경우
        # 다음 recursive equation이 성립한다.
        # S(i, j) = max(nums[i] + S(i+1, j), nums[j] + S(i, j-1))
        # recursion을 사용하면 sub-problem의 반복 실행이 있기 때문에
        # bottom-up 방식의 DP를 활용해야함
        
        PLAYER_1, PLAYER_2 = 0, 1
        
        n = len(nums)
        if n == 1:
            return True
        # 마지막 턴을 가진 player를 계산
        player = (n + 1) % 2
        
        # 각 player마다 스코어 테이블을 설정
        # dp[i][j] => S(i, j)
        dp1 = [[0] * n for _ in range(n)]
        dp2 = [[0] * n for _ in range(n)]
        
        # base case
        # S(i, i) = 
        #   마지막 턴이 본인일 경우: nums[i]
        #   마지막 턴이 본인이 아닐 경우: 0
        for i in range(n):
            if player == PLAYER_1:
                dp1[i][i] = nums[i]
            else:
                dp2[i][i] = nums[i]

        # player = 1 - player => 턴을 교체한다는 의미
        player = 1 - player
        
        # dp 테이블의 우측 상단 삼각형을 채워나감
        for diagonal in range(1, n):
            for i in range(n-diagonal):
                j = i + diagonal
                # 만약 player1의 턴일 경우
                if player == PLAYER_1:
                    # player1의 경우 recursive equation에 따라 계산
                    dp1[i][j] = max(nums[i]+dp1[i+1][j], nums[j]+dp1[i][j-1])
                    # player2의 경우 얻을 수 있는 최소한의 score만 얻음
                    dp2[i][j] = min(dp2[i+1][j], dp2[i][j-1])
                # player2의 경우도 마찬가지
                else:
                    dp2[i][j] = max(nums[i]+dp2[i+1][j], nums[j]+dp2[i][j-1])
                    dp1[i][j] = min(dp1[i+1][j], dp1[i][j-1])
            # turn 교체
            player = 1 - player
        
        # 각각의 최대 스코어를 비교
        return dp1[0][n-1] >= dp2[0][n-1]
                
