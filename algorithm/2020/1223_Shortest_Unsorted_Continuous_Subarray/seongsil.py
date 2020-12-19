class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        first, last = 0,len(nums)-1
        if nums == sorted_nums:
            return 0
        
        while nums[first] == sorted_nums[first]: #정렬이 필요한 시작점 찾기
            first += 1

        while nums[last] == sorted_nums[last]: #정렬이 필요한 끝지점 찾기
            last -= 1

        return last-first+1
