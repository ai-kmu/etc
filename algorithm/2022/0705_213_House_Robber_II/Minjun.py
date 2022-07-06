class Solution:
    def rob(self, nums: List[int]) -> int:
        tmp = []
        
        # len(nums) 짝수일 때, 최대값 계산 함수
        def evenSum(n):
            odd = 0
            even = 0
            for i in range(len(n)):
                if (i%2) == 0:
                    odd += n[i]
                else:
                    even += n[i]
            return max(odd, even)
        
        # nums 길이가 짝수이면, 최대값 계산 함수 호출  
        if len(nums) % 2 == 0:
            return evenSum(nums)
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 3:
            return max(nums)
        
        # nums 길이가 홀수이면, len(nums) 짝수로 만들고, 계산 함수 호출
        for i in range((len(nums)//2)+1):
            standard = nums[i]
            copy = nums[:]
            copy.pop(i+1)
            copy.pop(i)
            copy.pop(i-1)
            tmp.append((standard + evenSum(copy)))
            
        return max(tmp)
            
