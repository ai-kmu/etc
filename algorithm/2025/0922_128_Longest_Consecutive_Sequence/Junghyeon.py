class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        long_seq = 0
        
        for i in num_set:
            if i - 1 not in num_set:
                x = i
                count = 1
                while x + 1 in num_set:
                    x += 1
                    count += 1
                long_seq = max(long_seq, count)
        
        return long_seq
