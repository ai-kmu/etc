# 솔루션 봄 (차이 배열, 누적합)
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        freq = [0] * (len(nums) +1)
        for i, j in requests:
            freq[i] += 1
            if j + 1 < len(freq):
                freq[j+1] -=1
        for i in range(1, len(nums)):
            freq[i] += freq[i-1]
        freq = freq[:len(nums)]        
        freq.sort(reverse=True)
        ans = 0
        for i in range(len(nums)):
            ans += nums[i]*freq[i]%(10**9 + 7)
        return ans %(10**9 + 7)
            
