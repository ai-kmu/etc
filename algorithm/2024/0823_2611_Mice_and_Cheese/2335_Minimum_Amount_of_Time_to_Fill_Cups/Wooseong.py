import heapq as hq

class Solution:
    '''
    그때그때 제일 많은 애 넣으면 됨
    142 -> 131 021 010 000
    544 -> 443 333 223 212 111 001 001
    422 -> 312 211 101 000
    '''
    def fillCups(self, amount: List[int]) -> int:
        # amount가 세 개라서 가능한 풀이 ....
        amount = [-a for a in amount]
        hq.heapify(amount)
        answer = 0
        while True:
            top1 = hq.heappop(amount)
            top2 = hq.heappop(amount)
            last = hq.heappop(amount)
            if top1 < 0 and top2 < 0:
                # 두 개 채우기
                hq.heappush(amount, top1 + 1)
                hq.heappush(amount, top2 + 1)
                hq.heappush(amount, last)
                answer += 1
            elif top1 < 0 and top2 == 0:
                # 하나 채우기
                hq.heappush(amount, top1 + 1)
                hq.heappush(amount, top2)
                hq.heappush(amount, last)
                answer += 1
            elif top1 == 0 and top2 == 0:
                break
            
        
        return answer
