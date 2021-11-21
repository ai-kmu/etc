# 전형적인 coin 의 합계 문제
# dp를 이용하여 n원을 만들 수 잇는 가지수를 센다.
# n원을 만들수 있으면 n+c원을 만들 수 있는 가지수도 알 수 있다(여기서 c는 사용하지 않은 코인)

class Solution:
    def change(self, amount, coins):
        
        
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1 # 0원을 만들 수 있는것은 한가지라고  하고시작
        for coin in coins: 
            for i in range(coin, amount + 1): 
                dp[i] += dp[i-coin] * (coin <= i)

        return dp[amount]
