class Solution:
    def rob(self, nums: List[int]) -> int:
        def evenSum(nums):
            odd = 0
            even = 0
            for i in range(len(nums)):
                if (i%2) == 0:
                    odd += i
                else:
                    even += i
            return max(odd, even)
        
        # nums 길이가 짝수이면,        
        if len(nums) % 2 == 0:
            return evenSum(nums)
        
        # nums 길이가 홀수이면,
        for i, v in enumerate(nums):
            standard = i
            
            if nums == 1:
                nums.pop(-1)
                nums.pop(2)
                nums.pop(1)
            else:
                nums.pop(i+1)
                nums.pop(i-1)
                nums.pop(i)
            
            return standard + evenSum(nums)
            
        
