#findUnsortedSubarray
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        #맨 왼쪽이 최소값이 안되게 하기
        while start <= end and nums[start]==min(nums[start:end + 1]):
            start += 1

        #제일 오른쪽이 최대값이 안되게게
       while start <= end and nums[end]==max(nums[start:end + 1]):
            end -= 1

        return end - start + 1
