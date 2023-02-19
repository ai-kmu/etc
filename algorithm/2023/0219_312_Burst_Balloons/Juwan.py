from collections import deque

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # 인덱스를 벗어난 곳을 1로 취급하기 때문에
        # 처음 시작에서 양 옆에 1을 넣어줌
        nums.insert(0, 1)
        nums.append(1)

        l = len(nums)

        # dp 테이블 생성
        dp = [[0] * l for _ in range(l)]
        
        
        # dp 테이블에서 dp[i][j]의 값은 nums[i+1 : j] 사이에서
        # 구할 수 있는 최대값임
        # k는 터트릴 풍선을 의미
        # dp[i][k]는 (i : k)내에서 구할 수 있는 최대값
        # dp[k][j] 또한 마찬가지.

        for i in range(l-2,-1,-1): 
            for j in range(i, l):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[j]*nums[k])
        return dp[0][l-1]
