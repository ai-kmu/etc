class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        whole_sum = sum(nums)
        
        # 큰 숫자부터 넣는 것이 훨씬 빠름
        nums.sort(reverse=True)
        
        if whole_sum % k != 0:
            return False
        
        partial_sum = whole_sum // k
        
        # subset마다 남은 sum과, 남은 sum이 동일한 subset의 수로 딕셔너리를 만듦 
        remains = dict([(partial_sum, k) for _ in range(k)])
        
        def recur(i, remains):
            if i >= len(nums):
                return remains == {}
            
            # 각 subset마다 nums[i]를 집어넣어가며 recursion을 수행
            for partial_sum, count in remains.items():
                new_remains = remains.copy()
                
                if partial_sum < nums[i]:
                    continue
                else:
                    new_remains[partial_sum] = count - 1
                    
                    if new_remains[partial_sum] == 0:
                        new_remains.pop(partial_sum)
                    
                    new_sum = partial_sum - nums[i]
                    if new_sum > 0:
                        new_remains[new_sum] = new_remains.get(new_sum, 0) + 1
            
                if recur(i+1, new_remains):
                    return True
                  
            return False
        
        return recur(0, remains)
        
        
