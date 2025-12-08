# 솔루션 참고해서 풀이 안 해주셔도 됩니다.
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        ans = 0
        buy, sell = [], []  # buy: 최대 힙(가격을 음수로 저장), sell: 최소 힙
        
        for p, q, t in orders: 
            ans += q  # 일단 모든 주문량을 더해 둠 (후에 매칭되면 빼줌)

            if t:  # 판매 주문(sell)
                # 현재 판매가격(p) 이상으로 사겠다는 buy 주문과 매칭
                while q and buy and -buy[0][0] >= p:
                    pb, qb = heappop(buy)  # 가장 높은 가격의 buy 주문
                    ans -= 2 * min(q, qb)  # 매칭된 만큼 양쪽 주문량 제거
                    
                    if q < qb:  
                        # 남은 buy 주문량이 있다면 다시 힙에 넣기
                        heappush(buy, (pb, qb - q))
                        q = 0
                    else:
                        # 판매 주문이 더 많다면 계속 매칭 이어가기
                        q -= qb

                if q:  # 매칭하고도 남은 sell 주문은 backlog에 저장
                    heappush(sell, (p, q))

            else:  # 구매 주문(buy)
                # 현재 구매가격(p) 이하로 팔겠다는 sell 주문과 매칭
                while q and sell and sell[0][0] <= p:
                    ps, qs = heappop(sell)  # 가장 낮은 가격의 sell 주문
                    ans -= 2 * min(q, qs)  # 매칭된 만큼 양쪽 주문량 제거
                    
                    if q < qs:
                        # 남은 sell 주문량 재삽입
                        heappush(sell, (ps, qs - q))
                        q = 0
                    else:
                        q -= qs

                if q:  # 매칭 후 남은 buy 주문은 backlog로
                    heappush(buy, (-p, q))  # 최대 힙을 위해 가격을 음수로 저장
            
        return ans % 1_000_000_007  # 최종 backlog 수량 모듈러 연산 후 반환
