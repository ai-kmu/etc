class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # arr, int k, k번 반복하는 array로 modify
        # sub array -> max sum
        
        # 머리 + 몸통(k-2 반복) + 꼬리로 계산했을 때와 arr에서 구할 수 있는 subarray max를 비교
        # max suffix_sum + max(total * (k-2), 0) + max prefix_sum 로 구할 수 있음
        n = len(arr)
        modulo = 10**9 + 7
        
        # arr을 업데이트하지 않고, dp를 초기화
        dp = [0 for _ in range(n)]
        # 각 값들을 0으로 초기화
        dp[0] = arr[0]
        total = arr[0]
        prefix_sum = arr[0] # 0을 포함하는 sub max
        suffix_sum = arr[0] # n-1을 포함하는 sub max
        
        # kadane's algorithm
        for i in range(1, n):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
            total += arr[i]
            prefix_sum = max(total, prefix_sum)    
        
        suffix_sum = dp[-1]
        kadane_max = max(dp)
        if k == 1: # 1이면 kadane_max만 구하면 됨
            return max(kadane_max, 0) % modulo
        else:
            return max(suffix_sum + prefix_sum + max(total * (k-2), 0), kadane_max, 0) % modulo
        
