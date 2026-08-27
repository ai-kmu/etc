class Solution:
    def gcd(a, b):
        r = a % b
        if r == 0:
            return b
        else:
            gcd(b, r)

    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        mx = 0
        ans = 0

        for i in range(n):
            if mx < nums[i]:
                mx = nums[i]
            prefixGcd.append(gcd(mx, nums[i]))
        
        prefixGcd.sort()

        for i in range(n//2):
            ans += gcd(prefixGcd[i], prefixGcd.pop())

        return ans
    
    
        
