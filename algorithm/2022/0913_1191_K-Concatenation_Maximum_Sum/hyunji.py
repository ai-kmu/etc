# 오답
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        # 1. k=1일때의 answer * k
        dp = [0] * len(arr)
        dp[0] = arr[0]
        
        for i in range(len(arr)):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
        
        a = max(dp) * k
        
        if k < 2:
            return a
        
        # 2. maximum suffix sum + maximum prefix sum + (k-1) * whole array sum(k>2)
        arr_r = arr[::-1]
        
        dp_r = [0] * len(arr_r)
        dp_r[0] = arr_r[0]
        
        for i in range(len(arr_r)):
            dp_r[i] = max(dp_r[i-1] + arr_r[i], arr_r[i])
        
        suffix = max(dp_r)
        prefix = max(dp)
        total = sum(arr) * (k-2)
        
        answer = suffix + prefix + total
        
        if suffix < 0:
            return 0
        
        return max(suffix, answer)
        
