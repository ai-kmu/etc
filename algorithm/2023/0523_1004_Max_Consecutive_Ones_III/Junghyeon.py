'''
sliding window 방식을 이용
'''
class Solution:
    def longestOnes(self, nums, k):
        result = 0  
        zero_count = 0  
        l = 0

        for r in range(len(nums)):
            # 0인경우 zero_count 증가
            if nums[r] == 0:
                zero_count += 1

            # l을 이동시키면서 최대 개수 계산
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            # 최댓값 업데이트
            result = max(result, r - l + 1)

        return result
