class Solution:
    def Helper(self,index,amount,coins,dp):
        if index >= len(coins):
            return 0
        if amount == 0:
            return 1
        
        # amount가 차있으면 return
        if dp[index][amount] != -1:
            return dp[index][amount]
        else:
            # amount보다 작거나 같을 때는 만족 가능
            if coins[index] <= amount:
                # subproblem
                ans1 = self.Helper(index,amount-coins[index],coins,dp)
                ans2 = self.Helper(index+1,amount,coins,dp)
                dp[index][amount] = ans1 + ans2
                return ans1 + ans2 
            else: # amount보다 클 때, 다음 index 탐색
                dp[index][amount] = self.Helper(index+1,amount,coins,dp)
                return dp[index][amount]

        
    
    def change(self, amount, coins):
        dp = [[-1 for i in range(amount+ 1)]for j in range(len(coins)+1)]
        return self.Helper(0,amount,coins,dp)
