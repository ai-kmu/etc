from collections import defaultdict as ddict

MOD = 1e9 + 7

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # 합해야할 인덱스가 각각 몇 개인지 저장 - 구간 차이 계산 후 누적 합
        # 1. 구간 차
        counts = [0 for _ in range(len(nums) + 1)]
        for s, e in requests:
            counts[s] += 1
            counts[e + 1] -= 1
        # 2. 누적 합
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

        # 내림차순 정렬
        counts.sort(reverse=True)  # 몇 개 씩 더해야 하는지
        nums.sort(reverse=True)  # 뭘 더해야 하는지

        # 큰 걸 가장 많이 더하는 게 정답
        result = 0
        for num, cnt in zip(nums, counts):
            result += (num * cnt)
            if result >= MOD:
                result = int(result % MOD)
        
        return result
