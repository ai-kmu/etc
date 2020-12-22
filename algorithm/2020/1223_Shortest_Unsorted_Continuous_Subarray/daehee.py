import copy

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = copy.copy(nums)
        nums_copy.sort()
        start = len(nums_copy)                      # 시작점을 맨뒤로
        end = 0
        for i in range(len(nums_copy)):             
            if nums_copy[i] != nums[i]:             # 위치가 바뀐경우만 확인
                start = min(start, i)               # 뒤 index가 더 작은걸로 업데이트
                end = max(end, i)                   # 앞 index가 더 큰걸로 업데이트
        return end-start+1 if end-start>=0 else 0
