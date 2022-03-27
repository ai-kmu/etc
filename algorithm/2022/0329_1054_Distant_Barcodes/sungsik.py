from collections import Counter
import itertools


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # barcodes를 counter로 각각 개수를 센 후 개수의 내림차순으로 정렬
        barcode_count = [[x, y] for x, y in Counter(barcodes).most_common()]
        
        # 가장 많이 나온 barcode를 찾음
        # 해답이 있음을 보장하기 때문에 max_count는 <= (n + 1) // 2 이 보장됨
        max_count = barcode_count[0][1]
        
        # 가장 많이 나온 barcode를 세운 다음에
        # 사이사이에 barcode를 끼워 넣는 방식을 사용함
        answer = [[barcode_count[0][0]] for _ in range(max_count)]

        # cursor는 현재 사용중인 barcode를 의미
        # 0번째 barcode는 이미 전부 사용했기 때문에 1부터 시작
        cursor = 1
        for i in range(0, len(barcodes)-max_count):
            # 현재 barcode를 끼워넣음
            answer[i % max_count].append(barcode_count[cursor][0])
            
            # 현재 barcode를 다 사용했을 경우
            # 다음 barcode로 이동
            barcode_count[cursor][1] -= 1
            if barcode_count[cursor][1] <= 0:
                cursor += 1
        
        # 모든 list를 concat해서 return
        return list(itertools.chain(*answer))
