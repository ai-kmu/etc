class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        
        nums = [x for x in range(1, n+1)]
        
        def dfs(curr, nums, j):
            if len(curr) == n:
                self.ans += 1
            else:
                for i in range(len(nums)):
                    if nums[i] % j == 0 or j % nums[i] == 0:
                        dfs(curr + [nums[i]], nums[:i] + nums[i+1:], j-1)
        
        dfs([], nums, n)

        return self.ans
