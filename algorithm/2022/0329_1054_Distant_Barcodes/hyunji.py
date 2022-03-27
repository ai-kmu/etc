'''
1. 각 barcode 별로 개수를 세어준 뒤, 이를 k(barcode), v(barcode 개수) 로 딕셔너리화 해준다
2. 그리고 딕셔너리를 v(barcode 개수) 로 내림차순 정렬해준다.
3. 그리고 v 크기만큼 loop를 돌면서 가장 큰 v 를 가진 k 부터 차례로 res 배열의 짝수 index를 채워준다.
    ex. [1, 0, 1, 0, 1, 0, 1, 0]
4. 이런 식으로 정답 배열을 채워 나가다가, i >= n 이 되는 경우, i = 1 로 지정해주고
5. 정답 배열의 홀수 index를 채워나가면 된다. 
    ex. [1, 2, 1, 2, 1, 0, 1, 0]
    ex. [1, 2, 1, 2, 1, 3, 1, 3]
'''

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        res = [0] * n
        dict = {}
        
        # dictionary를 사용해서 바코드 별 개수 세어줌
        for x in barcodes:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        
        # value 의 값(barcode 개수)을 기준으로 내림차순 정렬
        sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
        
        i = 0
        for k, v in sorted_dict:
            # barcode 개수 만큼 loop 
            for x in range(v):
                res[i] = k
                i += 2
                if i >= n:
                    i = 1
        return res
        
