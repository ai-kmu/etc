class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums)):            
            if 1 < i:                       # 길이가 3 이상인 경우에만 가능
                nums[i] += max(nums[0:i-1]) # 그 전까지 더한 값들 중 가장 큰 값을 이번 값에 더함 / 붙어있으면 안되기 때문에 0~ㅑ-1까지만 
        return max(nums)
