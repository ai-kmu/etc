class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        [0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0]
        [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
        """
        DPlist = [0 for i in range(amount + 1)]
        
        n = len(coins)
        for i in range(1, amount + 1):
            temp = float("inf")
            for j in range(0, n):
                if coins[j] <= i:    # coin[j]가 i보다 크면 그대로 유지 = 그윗줄 그대로 가져옴
                    temp = min(temp, DPlist[i - coins[j]])
            DPlist[i] = 1 + temp  # 마지막에 리턴해야 하는 값은 DPlist[amount - coins[-1]] + 1
            print(temp, DPlist)
        return -1 if DPlist[amount] == float("inf") else DPlist[amount]
