class Solution(object):
    def findMin(self, nums):
        # 정렬돼있기 때문에 nums 돌면서
        # 첫번째 보다 작은값 있으면 return
        for i in nums:
            if nums[0] > i:
                return i
        
        # 아니면 첫번째를 리턴
        return nums[0]
