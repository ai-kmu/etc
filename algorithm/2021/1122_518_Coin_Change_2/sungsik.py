class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dynammic programming
        # amount를 num_coin개의 코인을 사용해서 조합을 만든다고 할 경우
        # 1. 크기가 제일 큰 코인을 사용하는 경우 -> combinations[num_coin][am-coins[num_coin-1]]
        # 2. 사용하지 않는 경우 -> combinations[num_coins-1][am]
        n = len(coins)
        combinations = [[0] * (amount+1) for _ in range(n+1)]
        # base case: amount=0일 경우 경우의 수는 1
        for i in range(len(coins)+1):
            combinations[i][0] = 1
        
        # 1개부터 n개의 코인을 사용하는 경우를 차례대로 순회
        for num_coin in range(1, n+1):
            # num_coin개를 사용할 때, 1부터 amount만큼의 양을 계산하는 경우를 차례대로 순회
            for am in range(1, amount+1):
                # 제일 큰 코인을 사용하지 않는 경우로 초기화
                combinations[num_coin][am] = combinations[num_coin-1][am]
                # 제일 큰 코인을 사용해도 0 이상이 남을 경우
                if am-coins[num_coin-1] >= 0:
                    # 제일 큰 코인을 사용하는 경우의 수를 더한다
                    combinations[num_coin][am] += combinations[num_coin][am-coins[num_coin-1]]
        
        return combinations[n][amount]
