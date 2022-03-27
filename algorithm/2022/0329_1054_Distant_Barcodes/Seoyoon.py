class Solution:
    def rearrangeBarcodes(self, barcodes):
        from collections import Counter
        # 디폴트가 min이니까 최빈 요소가 맨 위로 가도록 뒤집음
        counts = Counter(barcodes).most_common()[::-1]
        freq = [v for v,k in counts for _ in range(k)]
        # print(freq)
        
        ## 제일 빈도 높은 원소들을 먼저 0,2,4 ... 인덱스에 넣고 그다음 높은 순서대로 홀수 인덱스에 채우는 식
        # 짝수인덱스일때 첫번째 최빈요소 pop 해서 바꿈
        for i in range(0, len(barcodes), 2): 
            barcodes[i] = freq.pop()
        
        # 홀수인덱스일때 그다음 최빈요소 pop 해서 바꿈
        # 이게 pop되면 자동으로 그다음 최빈요소가 남으니까 차례대로 들어갈 수 있음
        for i in range(1, len(barcodes), 2): 
            barcodes[i] = freq.pop()
        return barcodes
