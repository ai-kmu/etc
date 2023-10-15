# Test6번에서 막히는 코드 구현;
# 해설보고 수정 했어요 리뷰 안해주셔도 됩니다
from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # 리스트의 길이
        N = len(nums)
        
        # 리스트 정렬
        nums.sort()
        
        # 각 숫자의 빈도를 계산
        freq = Counter(nums)
        
        # 각 숫자를 순회하면서 가능한 묶음을 확인
        for num in nums:
            if freq[num] != 0:
                # 현재 숫자의 빈도
                count = freq[num]
                
                # 현재 숫자부터 k개만큼의 숫자를 확인하며 빈도를 줄임
                for current_num in range(num, num + k):
                    freq[current_num] -= count
                    
                    # 빈도가 음수인 경우, 묶음을 만들 수 없으므로 False 반환
                    if freq[current_num] < 0:
                        return False
        
        # 모든 묶음을 만들 수 있는 경우 True 반환
        return True
