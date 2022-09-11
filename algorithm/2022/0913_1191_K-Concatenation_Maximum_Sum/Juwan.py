class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        def max_val_subarr(arr):

            max_val = 0

            m = len(arr)

            temp = 0

            for i in range(m):

                temp += arr[i]

                max_val = max(temp, max_val)

                if temp < 0:
                    temp = 0

            return max_val
        
        if k < 3:
            return max_val_subarr(arr*k)%(10**9+7)
        
        
        a = max_val_subarr(arr)
        b = max_val_subarr(arr*2)
        
        return max([a, b, b + sum(arr)*(k - 2)])%(10**9+7)
        

            
