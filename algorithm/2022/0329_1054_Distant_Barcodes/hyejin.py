from collections import defaultdict
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # warehouse에 barcode의 열이 있음
        # 두개의 근접한 barcode가 동일하지 않도록
        # 답은 무조건 존재
        
        answer = []
        
        # 빈도수 계산 / 1.defaultdict로 빈도수 계산 / 2.Counter로 빈도수 계산(더 빠름)
        # num_dict = defaultdict(int) 
        # for b in barcodes:
        #     num_dict[b] 
        num_dict = Counter(barcodes)
        
        heap = []
        # 빈도 수의 최대 힙 구축
        for k, v in num_dict.items():
            heapq.heappush(heap, (-v, k))
            
        # 빈도 수가 많은 것부터 뽑아서 answer에 append
        # 앞의 원소와 겹치지만 않으면 됌, 겹칠 경우, 두번째꺼를 집어넣음
        while heap:
            top = heapq.heappop(heap)
            # answer가 비었거나, top과 answer[-1]이 같지 않다면 추가 가능
            if len(answer) == 0 or answer[-1] != top[1]: 
                answer.append(top[1])
                if -top[0] > 1:
                    heapq.heappush(heap, (top[0] + 1, top[1]))
            else: # 아니라면 두번째걸 뽑아서 넣기
                second = heapq.heappop(heap)
                answer.append(second[1])
                if -second[0] > 1:
                    heapq.heappush(heap, (second[0] + 1, second[1]))
                heapq.heappush(heap, top)

        return answer
