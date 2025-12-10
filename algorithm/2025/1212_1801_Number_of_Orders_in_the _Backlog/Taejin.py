# 49번에서 틀립니다.. 풀이 안해주셔도 됩니다..

from collections import defaultdict, deque

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        backlog = [defaultdict(int), defaultdict(int)] # buy, sell list

        for p, a, o in orders: # price, amount, order type 순회
            backlog[o][p] += a

        # buy, sell 정렬
        buy = sorted([[k, v] for k, v in backlog[0].items()])
        sell = sorted([[k, v] for k, v in backlog[1].items()])

        buy_idx, sell_idx = 0, 0
        remains = 0

        # 판매 조건 맞으면 제거, 아니면 remains에 더하기
        while buy_idx < len(buy) and sell_idx < len(sell):
            if buy[buy_idx][0] >= sell[sell_idx][0]:
                if buy[buy_idx][1] >= sell[sell_idx][1]:
                    buy[buy_idx][1] -= sell[sell_idx][1]
                    sell_idx += 1
                else:
                    sell[sell_idx][1] -= buy[buy_idx][1]
                    buy_idx += 1

            else:
                remains += buy[buy_idx][1]
                buy_idx += 1

        remains += sum([a for _, a in buy[buy_idx:]] + [a for _, a in sell[sell_idx:]])
        return int(remains % (1e9 + 7))



        
