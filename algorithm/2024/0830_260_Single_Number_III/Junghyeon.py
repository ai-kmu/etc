# 딕셔너리로 원소들의 등장 수를 세고, 1인 경우 저장해서 리턴

from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        
        for i in nums:
            d[i] += 1

        result = []

        for i, j in zip(d.values(), d.keys()):
            if i == 1:
                result.append(j)

        return result
