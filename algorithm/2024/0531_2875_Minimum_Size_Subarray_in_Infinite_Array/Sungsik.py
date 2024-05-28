class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        answer = 0
        
        # 만약, target이 nums의 sum보다 클 경우, 이를 빼주고 계산해도 무방
        q, r = divmod(target, sum(nums))
        answer += q * len(nums)
        
        # 끝이랑 앞이 붙는 경우가 있어 nums를 2배로 늘림
        nums = nums + nums
        n = len(nums)
        
        target = r
        
        if target:
            # two-pointer를 이동하면서 target과 맞을 경우
            # 이를 min_arr과 비교하여 min_arr보다 작을 경우 update
            l = r = 0
            tmp_sum = 0
            min_arr = float('inf')
            
            while l < n and r < n:
                tmp_sum += nums[r]
                while tmp_sum < target and r < n - 1:
                    r += 1
                    tmp_sum += nums[r]
                
                if tmp_sum == target:
                    min_arr = min(r - l + 1, min_arr)
                
                while tmp_sum > target and l < r:
                    tmp_sum -= nums[l]
                    l += 1
                
                if tmp_sum == target:
                    min_arr = min(r - l + 1, min_arr)
                
                r += 1
        
            if min_arr == float('inf'):
                return -1
            return answer + min_arr
        return answer
        
