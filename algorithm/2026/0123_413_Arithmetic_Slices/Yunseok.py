## 풀이 안해주셔도 됩니다...
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 3개 미만이면 등차수열(최소 3개)을 만들 수 없음
        if len(nums) < 3:
            return 0
        
        total_slices = 0  # 전체 등차수열의 개수 (정답)
        current_streak = 0  # 현재 위치에서 끝나는 등차수열의 추가 개수
        
        # 인덱스 2부터 끝까지 순회 (앞의 두 개(i-1, i-2)와 비교해야 하므로)
        for i in range(2, len(nums)):
            # 등차 조건 확인: (현재 - 이전) == (이전 - 전전)
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                # 등차수열이 이어지면, 현재 위치에서 끝나는 등차수열 개수가 1 증가
                current_streak += 1
                # 누적 합계에 더함
                total_slices += current_streak
            else:
                # 등차수열이 끊기면 초기화
                current_streak = 0
                
        return total_slices
