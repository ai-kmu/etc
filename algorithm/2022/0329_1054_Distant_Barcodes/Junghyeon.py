import heapq
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        '''
        Greedy 방법으로 매 순간 개수가 가장 많은 수와 두번째로 많은 수를 result에 넣고 각각 개수를 하나씩 뺀다음 배열 재정렬
        -> O(N^2*logN)으로 풀이시 시간초과가 발생하므로 위의 방법으로 풀이 x
        mean heap을 이용해서 매 반복마다 정렬 없이도 해결가능
        '''
        result = list()
        heap = list()
        
        # Counter를 이용해 각각 숫자마다 개수를 구한다.
        num_cnt = Counter(barcodes)
        
        # mean heap으로 처리하기 위해 -count를 append
        # num = 숫자, count = 숫자의 개수
        for num, count in num_cnt.items():
            heapq.heappush(heap, [-count, num])
        
        # 2개씩 묶어서 꺼내기때문에 입력값의 길이가 홀수일때 따로 처리를 해줘야한다.
        while len(heap) > 1:
            cnt1, num1 = heapq.heappop(heap)
            cnt2, num2 = heapq.heappop(heap)

            result.append(num1)
            result.append(num2)
            
            # -count로 넣었기 때문에 더하는 식으로 업데이트
            cnt1 += 1
            cnt2 += 1
            
            # cnt = 0 -> 해당 숫자를 더이상 사용x, heappush를 진행하지 않는다. 
            if cnt1 < 0:
                heapq.heappush(heap, [cnt1, num1])
            if cnt2 < 0:
                heapq.heappush(heap, [cnt2, num2])
        
        # 입력값의 길이가 홀수일때의 처리
        if len(heap):
            result.append(heap[0][1])
            
        return result
