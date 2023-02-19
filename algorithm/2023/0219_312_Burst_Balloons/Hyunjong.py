# 이번엔 아에 틀렸어요...
# recursive방식으로 풀다가 막힌거 같아요
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]

        def recursive(left, right):
            if left == right:
                return 0
            max_ = 0
            for i in range(left+1, right-1):
                coins = nums[i-1] * nums[i] * nums[i+1]
                coins += recursive(left, i) + recursive(i, right)
                max_ = max(max_, coins)
            
            return max_
        return recursive(0, n+2)
