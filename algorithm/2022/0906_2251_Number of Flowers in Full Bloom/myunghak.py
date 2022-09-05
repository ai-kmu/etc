class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        flower_length = len(flowers)
        
        def bl(arr, x):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < x : 
                    left = mid + 1 
                else: 
                    right = mid
            return left

        def br(arr, x):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if x < arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        flowers_1 = sorted(f[0] for f in flowers)
        flowers_2 = sorted(f[1] for f in flowers)
        
        return [br(flowers_1,p) - bl(flowers_2, p) for p in persons]
