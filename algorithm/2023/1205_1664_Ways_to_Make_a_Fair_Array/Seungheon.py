class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        # 초깃값 설정
        sum_e = 0
        sum_o = 0    
        for i, n in enumerate(nums[1:]):
            if i % 2 == 0:
                sum_e += n
            else:
                sum_o += n 
        result = 1 if sum_e == sum_o else 0

        for i, n in enumerate(nums):
            if i == 0:
                continue
            if i % 2 == 1:
                sum_e = sum_e - nums[i] + nums[i-1]
            else:
                sum_o = sum_o - nums[i] + nums[i-1]

            if sum_e == sum_o:
                result += 1

        return result
