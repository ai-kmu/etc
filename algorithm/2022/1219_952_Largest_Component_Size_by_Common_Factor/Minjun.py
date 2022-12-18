import math
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        count = len(nums)
        def is_prime_number(x):
            for i in range(2, int(math.sqrt(X))+1):
                if x % i == 0:
                    return -1
            nonlocal count
            count -= 1
            return x
        for i, x in enumerate(nums):
            is_prime_number(x)
        return count
