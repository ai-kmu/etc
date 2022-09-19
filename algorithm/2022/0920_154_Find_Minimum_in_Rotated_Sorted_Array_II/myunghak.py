# 우선 리스트를 탐색하며 내림차순이 아닌부분 찾음
# 내림차순이 아닌 부분이 있으면 그부분을 출력
# 모두 내림차순으로 정렬 되어 있으면 첫번째 값 출력

class Solution:
    def findMin(self, nums: List[int]):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
        
