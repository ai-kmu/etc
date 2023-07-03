class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        a = len(nums)

        cnt = len(nums)
        while a > 0:
            tmp = []
            for i in range(a-1):
                tmp.append(nums[i+1]-nums[i])

        b = []
        
        return cnt
