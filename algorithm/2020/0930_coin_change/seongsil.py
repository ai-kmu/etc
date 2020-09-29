# Dynamic Programming

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tempNumofCoins = [0] + [-1] * (amount)

        for i in range(amount + 1):
            if tempNumofCoins[i] != -1:
                for coin in coins:
                    if i + coin <= amount:
                        if tempNumofCoins[i+coin] == -1:
                            tempNumofCoins[i+coin] = tempNumofCoins[i] + 1
                        else:
                            tempNumofCoins[i+coin] = min(tempNumofCoins[i+coin], tempNumofCoins[i] + 1)
                            
        return tempNumofCoins[amount] 
        
