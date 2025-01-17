# TimeLimited..................
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        하루에 할 수 있는 action 3개(buy, sell, cooldown), prices 길이 5000 -> bruteforce 시 3^5000를 고려해야 함
        - time limit 걸릴 거임
        - 다른 최적화 수단이 필요함
            - sell 직후 buy를 못하는 조건이 있긴 하지만, 시간을 유의미하게 줄일 것 같지는 않음
            - greedy? dp? 
            - 현재 day에 가지고있는 profit, stock에 따라 뭐가 더 optimal 한 지에 대한 기준이 필요함
                - profit이 같다면, stock이 낮을 수록 좋은 것 -> 일단 얘만 고려해봐  -> time_limited -> profit_dp
                - stock이 같다면, profit이 높을 수록 좋은 것 -> 얘도 고려해 -> stock_dp
                - 둘 다 다르다면, dp에 저장
        profit_dp[day][prev_action][profit] = stock
        stock_dp[day][prev_action][stock] = profit
        -> action이 무슨 상관이야, 고려하지마
        -> 상관있지, day마다 greedy하지가 않잖아
        self.prices = prices
        self.answer = 0
        self.profit_dp = [dict(sell=dict(), cooldown=dict(), buy=dict()) for _ in range(len(prices))]
        self.stock_dp = [dict(sell=dict(), cooldown=dict(), buy=dict()) for _ in range(len(prices))]
        self.action('cooldown', 0, 1001, 0)
        return self.answer

    def action(self, 
                prev_action : str, 
                cur_profit : int, 
                cur_stock : int,
                cur_day : int
    ):
        if cur_day == len(self.prices):
            self.answer = max(self.answer, cur_profit)
            return

        if cur_stock == 1001:
            try:
                if cur_profit > self.stock_dp[cur_day][prev_action][cur_stock]:
                    self.stock_dp[cur_day][prev_action][cur_stock] = cur_profit
                else: return
            except:
                self.stock_dp[cur_day][prev_action][cur_stock] = cur_profit
            try:
                if cur_stock < self.profit_dp[cur_day][prev_action][cur_profit]:
                    self.profit_dp[cur_day][prev_action][cur_profit] = cur_stock
                else: return
            except:
                self.profit_dp[cur_day][prev_action][cur_profit] = cur_stock
        else:
            try:
                if cur_profit > self.stock_dp[cur_day][prev_action][cur_stock]:
                    self.stock_dp[cur_day][prev_action][cur_stock] = cur_profit
                else: return
            except:
                self.stock_dp[cur_day][prev_action][cur_stock] = cur_profit
                    
        if prev_action == 'sell':  # profit만 따져
            self.action('cooldown', cur_profit, cur_stock, cur_day+1)
        elif prev_action == 'cooldown':
            if cur_stock == 1001:  # 보유 중인 stock이 없다면, buy or cooldown 가능
                self.action('buy', cur_profit, self.prices[cur_day], cur_day+1)
                self.action('cooldown', cur_profit, cur_stock, cur_day+1)
            else:  # 보유 중인 stock이 있다면, sell or cooldown 가능
                self.action('sell', cur_profit+self.prices[cur_day]-cur_stock, 1001, cur_day+1)
                self.action('cooldown', cur_profit, cur_stock, cur_day+1)
        elif prev_action == 'buy':  # profit, stock 둘 다 따져
            self.action('sell', cur_profit+self.prices[cur_day]-cur_stock, 1001, cur_day+1)
            self.action('cooldown', cur_profit, cur_stock, cur_day+1)
        else: raise ValueError
'''

# Solution 봤습니다.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0
        b = [-10 ** 9] * n
        s = [0] * n
        for i in range(n):
            s[i] = max(s[i - 1], prices[i] + b[i - 1])
            b[i] = max(b[i - 1], s[i - 2] - prices[i])
        return s[-1]
