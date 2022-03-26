from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        ans = [0] * len(barcodes) # 정답 리스트 요소를 모두 0으로 초기화. 길이는 barcodes와 동일
        bar_count = Counter(barcodes) # 숫자별로 몇개가 있는지 dict형태로 저장
        i = 0 # ans의 인덱스

        # 숫자가 많은 것을 0번째 인덱스 부터 2칸씩 정답 리스트에 저장
        # 그 다음 많은 숫자는 계속 이어서 저장하다가 만약 최대 길이를 초과하면
        # 1번째 인덱스부터 다시 2칸씩 저장
        for x,y in bar_count.most_common():
            for k in range(y):
                if i>=len(barcodes): # ans 인덱스 i가 barcodes 길이 이상이면 1로 초기화
                    i = 1
                ans[i] = x
                i += 2   
        return ans
