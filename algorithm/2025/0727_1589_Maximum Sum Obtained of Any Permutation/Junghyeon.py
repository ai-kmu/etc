class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n_nums = len(nums)
        n_requests = len(requests)
      
        freq = [0] * n_nums
        for left, right in requests:
            freq[left] += 1
            if right < n_nums - 1:
                freq[right + 1] -= 1

        for idx in range(1, n_nums):
            freq[idx] += freq[idx - 1]

        freq.sort()
        nums.sort()

        MOD = 10**9 + 7
        total_sum = 0
        for idx in range(n_nums - 1, -1, -1):
            total_sum = (total_sum + freq[idx] * nums[idx]) % MOD

        return total_sum
