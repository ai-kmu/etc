class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for i in nums_set:
            ch_len = 0
            if i-1 not in nums_set:
                j = i 
                while j in nums_set:
                    ch_len = ch_len + 1
                    j = j + 1
                result = max(ch_len, result)
            else:
                continue
               
        return result

        
