# 백트래킹으로 풀려고 시도했으나 Time Limit Exceeded 발생

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False
        
        target = total // k
        subset = [0] * k
        
        def backtracking(idx):
            if idx == len(nums):
                for s in subset:
                    if s != target:
                        return False
                    else:
                        return True
            
            for i in range(k):
                if subset[i] + nums[idx] <= target:
                    subset[i] += nums[idx]
                    if backtracking(idx + 1):
                        return True
                    
                    subset[i] -= nums[idx]
                    
            return False

        return backtracking(0)
