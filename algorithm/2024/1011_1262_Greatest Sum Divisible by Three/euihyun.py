# 풀다가 답 봤어요 리뷰 안해주셔도 됩니다

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp 배열 초기화 나머지가 0, 1, 2일 때의 최대 합
        dp = [[0 for i in range(len(nums) + 1)] for j in range(3)]

        for i in range(1, len(nums) + 1):
            # j는 나머지 0, 1, 2를 의미
            for j in range(3):
                # 이전까지의 dp 값을 그대로 유지하는 경우 
                dp[j][i] = max(dp[j][i-1], dp[j][i])
                
                # 현재 숫자(nums[i-1])를 더한 경우의 합 
                curSum = nums[i-1] + dp[j][i-1]
                
                # 새로운 합(curSum)을 3으로 나눈 나머지 값
                idx = curSum % 3
                
                # 새로운 나머지 idx에 해당하는 dp 값을 갱신
                dp[idx][i] = max(dp[idx][i-1], curSum, dp[idx][i])


        return dp[0][-1]
