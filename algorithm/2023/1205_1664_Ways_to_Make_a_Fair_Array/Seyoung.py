# 이번주에는 솔루션을 참고했습니다.  리뷰는 괜찮습니다.

from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # 오른쪽 (r)과 왼쪽 (l)의 홀수 인덱스와 짝수 인덱스에 대한 합을 저장하는 변수 초기화
        odd_sum_r, even_sum_r = 0, 0
        odd_sum_l, even_sum_l = 0, 0
        
        # 각 인덱스에 대한 누적 합을 저장하는 배열
        sum_arr = []
        ans = 0

        # 배열의 오른쪽 부분에 대한 누적 합 계산
        for i in range(len(nums)-1, -1, -1):
            # 현재 인덱스에 대한 합을 sum_arr에 역순으로 저장
            sum_arr.append([odd_sum_r, even_sum_r, odd_sum_l, even_sum_l])
            
            # 현재 인덱스에 따라 odd_sum_r과 even_sum_r을 업데이트
            if i % 2:
                odd_sum_r += nums[i]
            else:
                even_sum_r += nums[i]

        # sum_arr를 정상적인 순서로 변경하기 위해 뒤집음
        sum_arr = sum_arr[::-1]

        # 배열의 왼쪽 부분에 대한 누적 합 계산
        for i in range(len(nums)):
            # 현재 인덱스에 따라 odd_sum_l과 even_sum_l을 업데이트
            sum_arr[i][2], sum_arr[i][3] = odd_sum_l, even_sum_l
            if i % 2:
                odd_sum_l += nums[i]
            else:
                even_sum_l += nums[i]

        # 배열이 공정한지 확인하고 유효한 경우를 카운트
        for i in range(len(nums) - 1, -1, -1):
            # 인덱스 i의 요소를 제거하여 배열이 공정한지 확인
            if sum_arr[i][2] + sum_arr[i][1] == sum_arr[i][3] + sum_arr[i][0]:
                ans += 1

        # 공정한 배열의 총 개수를 반환
        return ans
