class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        while n > 1:
            winners = []
            for i in range(n//2):
                if i % 2 == 0:
                    winners.append(min(nums[2*i], nums[2*i+1]))
                if i % 2 == 1:
                    winners.append(max(nums[2*i], nums[2*i+1]))
            n = n // 2
            nums = winners
        
        return nums[0]
