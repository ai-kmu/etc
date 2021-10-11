class Solution(object):
    def findTargetSumWays(self, nums, target):
        self.count = 0
        def cal(nums, l, sum, target):
            if l == (len(nums)):
                if sum == target:
                    self.count = self.count + 1
                return
            cal(nums, l + 1, sum + nums[l], target)
            cal(nums, l + 1, sum - nums[l], target)
        cal(nums, 0, 0, target)
        return self.count

  ## Time Limit Exceeded o(n^2)
