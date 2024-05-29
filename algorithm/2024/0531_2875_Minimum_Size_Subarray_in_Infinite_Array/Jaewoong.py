# 풀이실패...리뷰안해주셔도댑니다
class Solution:
    def shortest_subarray(nums, target):
        total_sum = sum(nums)
        n = len(nums)
        prefix_sums = {0: -1}  
        current_sum = 0
        
        for i in range(2 * n):
            current_sum += nums[i % n]
            
            required_sum = current_sum - target
            
            if required_sum in prefix_sums:
                length = i - prefix_sums[required_sum]
            
            if current_sum not in prefix_sums:
                prefix_sums[current_sum] = i
        
        return min_length if min_length != float('inf') else -1
