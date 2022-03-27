class Solution(object):
    def rearrangeBarcodes(self, barcodes):
    # 필요한 변수 정의
        cnt = {}             # cnt: barcode의 수별로 정렬
        n = len(barcodes)    # 
        result = [None] * n     # result: barcode 저장할 list(결과)

        # 숫자 바코드별 개수 저장 dictionary
        for barcode in barcodes:
            if barcode in cnt:
                cnt[barcode] += 1
            else:
                cnt[barcode] = 1

        # 숫자 바코드 개수별로 정렬
        cnt = sorted(cnt.items(), key = lambda item: item[1], reverse = True)
        
        # barcode가 많은 순서대로 입력
        pos = 0
        for i in range(len(cnt)):
            for j in range(cnt[i][1]):
            
                # 처음에는 짝수번째 위치에 입력
                result[pos] = cnt[i][0]
                pos += 2
                
                # 입력이 다 찰 경우 홀수번째 나머지 
                if pos >= n:
                    pos = 1
        return result
