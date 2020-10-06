class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        numWays = [float('inf')] * (amount + 1)
        
        numWays[0] = 0
        
        for coin in coins:
            for value in range(coin, amount + 1):
                numWays[value] = min(numWays[value], 1 + numWays[value - coin])
                
        return numWays[amount] if numWays[amount] != float('inf') else -1
