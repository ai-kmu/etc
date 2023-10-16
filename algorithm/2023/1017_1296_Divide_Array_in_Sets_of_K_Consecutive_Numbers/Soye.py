class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        num_count = collections.Counter(nums)
        sorted_nums = sorted(nums, key = lambda x: x)

        for n in sorted_nums: 
            if num_count[n] == 0:
                continue
            n_sets_needed = num_count[n]
            for j in range(k):
                numInSequence = n + j 
                if numInSequence not in num_count:
                    return False
                else: 
                    num_count[numInSequence] -= n_sets_needed
                
                if num_count[n + j] < 0:
                    return False
        
        return True
