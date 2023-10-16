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
                if numInSequence not in num_count:  # numInSequence랑 연속되는 숫자가 없으므로
                    return False  
                else:  # numInSequence랑 연속되는 숫자가 있으면
                    num_count[numInSequence] -= n_sets_needed
                
                if num_count[n + j] < 0:  # 써야하는 숫자의 갯수가 부족하면
                    return False
        
        return True
