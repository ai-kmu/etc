class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums) # sorting
        if nums == sorted_nums: # 정렬한 것과 원래 array가 일치하면 0 반환
            return 0
        for front in range(len(nums)): # 앞에서부터 안 겹치는 index 찾기
            if nums[front] != sorted_nums[front]:
                break
        for back in reversed(range(len(nums))): # 뒤에서부터 안 겹치는 index 찾기
            if nums[back] != sorted_nums[back]:
                break
                
        return back-front+1 # answer 구하기
