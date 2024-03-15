# 김민성이 O(N^2)으로 풀다가 저 따라했어요

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 홀수 인덱스
        odd_idx = [i for i, v in enumerate(nums) if v % 2 == 1]
        ans = 0
        # trivial case
        if len(odd_idx) < k:
            return 0
        for i, v in enumerate(odd_idx):
            # Exit
            if i + k > len(odd_idx):
                break

            # left
            # 처음이면 처음 홀수 인덱스까지
            # 이전 홀수 인덱스 다음부터 지금 홀수 인덱스까지
            if i == 0:
                left = v + 1
            else:
                left = v - odd_idx[i-1]
            
            # right
            # 마지막 홀수 인덱스면, nums의 끝까지.
            # 다음 홀수 인덱스 전까지
            if i + k == len(odd_idx):
                right = len(nums) - odd_idx[-1]
            else:
                right = odd_idx[i+k] - odd_idx[i+k-1]

            # 좌 우 곱하면 경우의 수 완성
            ans += left * right
        return ans
