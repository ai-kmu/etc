#풀이 실패
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(x,nums_len):
            if nums_len >= 3:
                ans = nums[x - 1] * nums[x] * nums[x + 1]
                
                if nums_len == 0:
                    return ans
            elif nums_len == 2:
                ans = 1 * nums[x] * nums[x + 1]
                
                if nums_len ==0:
                    return ans
            dfs(x,len(nums) - 1)

        return dfs(1,len(nums))
            
            
