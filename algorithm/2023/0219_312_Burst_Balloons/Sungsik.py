class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # nums에 앞뒤로 1 추가
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        # 해당 문제를 2D dp table로 둔다면
        # dp[i][j]는 nums의 i번째부터 j번째까지에서의 최댓값으로 볼 수 있다.
        # 또한 이는 터뜨린 마지막 풍선을 k라 했을 때
        # k기준으로 왼쪽, 오른쪽의 최대 coin과 k를 터뜨렸을떄의 coin을 합한 것으로 쪼갤 수 있다.
        for diagonal in range(2, n):
            for row in range(n-diagonal):
                col = row + diagonal
                max_coin = 0
                # i의 범위가 row~col이 아닌 이유는 앞뒤로 1짜리 풍선을 추가해줬기 때문
                # 1짜리 풍선을 터뜨리지 않기 위해 row+1~col-1 범위로 하였다.
                for i in range(row+1, col):
                    tmp_coin = nums[row] * nums[i] * nums[col] + dp[row][i] + dp[i][col]
                    if tmp_coin > max_coin:
                        max_coin = tmp_coin
                dp[row][col] = max_coin
        
        return dp[0][n-1]
                    
