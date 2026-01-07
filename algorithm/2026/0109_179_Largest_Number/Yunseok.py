import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def comp(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        str_nums = list(map(str, nums))

        sorted_nums = sorted(str_nums, key=functools.cmp_to_key(comp))

        return str(int(''.join(sorted_nums)))
    
