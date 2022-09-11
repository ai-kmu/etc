class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        
        # kadane's algorithm
        def kadanesum(arr):
            cursum = 0
            maxsum = -1e-9
            for num in arr:
                cursum += num
                if cursum < 0:
                    cursum = 0
                if cursum > maxsum:
                    maxsum = cursum
            return maxsum
        
        
        # prefix, suffix sum
        # kadane's algorithm과는 다르게 무조건 맨 끝에서부터 sum을 구함
        def fixsum(arr):
            cursum = 0
            maxsum = -1e-9
            for num in arr:
                cursum += num
                if cursum > maxsum:
                    maxsum = cursum
            return maxsum
        
        
        # k = 1일 경우 array의 subarray로 maximum sum을 구할 수 있음
        if k == 1:
            return int(kadanesum(arr) % (1e9 + 7))
        # k > 1일 경우 array를 두개 이어붙인 경우의 subarray의 maximum sum,
        # prefix sum과 suffix sum, array의 전체합을 k배만큼 더한 것 중 큰 쪽이 정답
        else:
            return int(max(kadanesum(arr*2), fixsum(arr) + fixsum(arr[::-1]) + sum(arr) * (k - 2)) % (1e9 + 7))
