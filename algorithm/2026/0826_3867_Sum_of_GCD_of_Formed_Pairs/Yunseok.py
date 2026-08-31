class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        prefix_gcd = []
        mx_i = 0
        for i in range(n):
            mx_i = max(mx_i, nums[i])
            prefix_gcd.append(gcd(nums[i], mx_i))

        prefix_gcd.sort()

        total = 0
        lo, hi = 0, n - 1
        while lo < hi:
            total += gcd(prefix_gcd[lo], prefix_gcd[hi])
            lo += 1
            hi -= 1
        
        return total
