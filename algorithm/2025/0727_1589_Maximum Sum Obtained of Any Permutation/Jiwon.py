# 풀이 참고
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # i번째 인덱스가 몇 번 계산에 포함되는지 확인
        freq = [0 for _ in range(n)] 
        for start, end in requests:
            freq[start] += 1  # 시작 위치 표시: +1
            if end + 1 < n:
                freq[end + 1] -= 1  # 끝 위치 표시: -1
        
        # 실제 포함 횟수 계산
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        # 계산에 많이 포함되는 위치에 큰 숫자 배치
        nums.sort()
        freq.sort()
        
        ans = 0
        for i in range(n):
            ans = (ans + nums[i] * freq[i]) % MOD
        
        return ans
