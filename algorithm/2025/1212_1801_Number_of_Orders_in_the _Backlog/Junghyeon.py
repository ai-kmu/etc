class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_order = []
        buy_order = []
        mod_num = 10 ** 9 + 7
        for order in orders:
            price, amount, order_type = order[0], order[1], order[2]
            if order_type == 0:
                heapq.heappush(buy_order, [-price, amount])      
            else:
                heapq.heappush(sell_order, [price, amount])
            
            while buy_order and sell_order and -buy_order[0][0] >= sell_order[0][0]:
                buy = heapq.heappop(buy_order)
                sell = heapq.heappop(sell_order)
                if sell[1] > buy[1]:
                    heapq.heappush(sell_order, [sell[0], sell[1] - buy[1]])
                elif buy[1] > sell[1]:
                    heapq.heappush(buy_order, [buy[0], buy[1] - sell[1]])
                        
        buy_amount = sell_amount = 0
        for buy in buy_order:
            buy_amount += buy[1]
        for sell in sell_order:
            sell_amount += sell[1]
        return (buy_amount + sell_amount) % mod_num
        
                
            
                
                
