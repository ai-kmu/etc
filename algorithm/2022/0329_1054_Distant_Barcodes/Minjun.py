'''
제일 많은 것부터 인덱스에 집어넣고
사이사이에 계속 껴넣으면 같은 바코드가 인접할 일이 없다.
껴넣다가 배열 끝에 도달하면 초기화해서 
다시 껴넣으면 된다.
'''
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # 카운터 함수로 딕셔너리 생성
        cnt = Counter(barcodes)
        
        # 바코드 재배열용 리스트 생성 (barcodes 길이만큼)
        answer = [0] * len(barcodes)
        
        # 인덱스 지표 초기화
        i = 0
        
        # 가장 많이 나온 순부터 반복
        for key,value in cnt.most_common():
            
            # 바코드 수만큼 반복
            for _ in range(value):
                
                # 리스트 끝에 도달하면 지표 초기화
                if i >= len(barcodes):
                    i = 1
                
                answer[i] = key
                
                # 2칸씩 띄어서 저장
                i += 2
        
        return answer            
        
