class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 앞 뒤로 리스트에 1을 추가해줌
        # dp table 선언
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        # i는 어디서부터 어디까지 값들을 비교할 것인지 정해주는 값
        for i in range(len(nums)):
            # left와 right을 설정해서 코인의 점수를 더해감
            for left in range(len(nums)-i):
                right = left + i
                
                res = 0
                for j in range(left+1, right):
                    coins = nums[left] * nums[j] * nums[right]
                    # 이제까지 계산된 점수와 res값을 비교하며 가장 큰 값으로 res 업데이트
                    res = max(res, coins + dp[left][j] + dp[j][right])
                # 해당 값을 dp 테이블에 업데이트
                dp[left][right] = res
                
        return dp[0][len(nums)-1]
