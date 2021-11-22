class Solution(object):
    def change(self, amount, coins):

        dp = [0] * (amount + 1) ## 동적할당법
                                ## dp의 인덱스는 amount이다.
                                ## dp의 value는 가능한 경우의 수이다.
        dp[0] = 1 ## 0원을 만들 수 있는 경우의 수는 1이다.
        
        for coin in coins: ## 전체 코인을 순회하며 경우의 수를 판단하기. 
            for x in range(coin, amount + 1):
                ## 현재 코인보다 큰 amount만 경우의 수에 추가할 수 있다.
                dp[x] += dp[x - coin]
                ## x에서 coin만큼 빠진 값은 현재 coin으로 x의 위치에 경우의 수로 추가할 수 있는 것을 의미한다.
                ## 따라서 dp[x] += dp[x - coin]을 하면 전체 x의 경우의 수를 계산할 수 있다.
        return dp[amount]
