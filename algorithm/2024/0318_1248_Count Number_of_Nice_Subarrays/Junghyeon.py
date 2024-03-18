# 홀수가 등장하는 인덱스를 기록한 후, 그 사이의 거리를 곱하여 경우의 수를 계산
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        idx = [-1]
        res = 0
        for i in range(len(nums)):
            # 홀수인 경우를 기록
            if nums[i] % 2 == 1:
                idx.append(i)

        idx.append(len(nums))
        
        # 두 홀수 인덱스 사이의 거리를 구하고 다음 k개 홀수 사이의 거리를 곱하여 결과에 더합
        for i in range(1, len(idx) - k):
            res += (idx[i] - idx[i-1]) * (idx[i+k] - idx[i+k-1])

        return res
