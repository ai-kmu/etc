# 풀이 실패
# dictionary에 꽃 개수 저장 및 person 구하기
# dictionary 생성 과정에서 memory 초과
# 이진탐색 시도 중 ㅜ ㅜ
from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        flower = defaultdict(int)
        
        for i, j in flowers:
            for f in range(i,j+1):
                flower[f] += 1
        
        return [flower[p] for p in persons]
