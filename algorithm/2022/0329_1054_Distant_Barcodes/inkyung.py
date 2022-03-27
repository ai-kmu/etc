from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt_bar = Counter(barcodes)
        cnt_bar = {k: v for k, v in sorted(cnt_bar.items(), key=lambda x: x[1], reverse=True)}
        answer = [0] * len(barcodes)
        
        idx = 0
        for k, v in cnt_bar.items():
            for i in range(v):
                answer[idx] = k
                # 0을 포함한 짝수 자리에 모든 값이 채워지고 나면 홀수 자리에 채우기 시작
                idx = idx + 2 if idx + 2 < len(barcodes) else 1
        return answer
