# Time Limit Exceeded 
# 524 / 535 testcases passed
# nums를 반복한 리스트 생성
# nums : [1,1,1,2,3] -> [1,1,1,2,3,1,1,1,2,3,1,1,1,2,3, ...]
# slicing window(length)를 1부터 늘려가면서 리스트의 합이 target과 같을때 slicing window(length)를 리턴
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        t = target // sum(nums) + 2
        # nums 리스트 복제
        nums *= t
        
        for length in range(len(nums)):
            for idx in range(1, len(nums)+1):
                if sum(nums[idx:idx+length]) == target:
                    return length

        return -1
