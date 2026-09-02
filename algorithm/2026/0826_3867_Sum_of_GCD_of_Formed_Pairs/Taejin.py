class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def EEA(a, b):
            if a < b:
                return EEA(b, a)

            elif b == 0:
                return a

            else:
                return EEA(b, a % b)
        
        prefixGcd = []
        mx_i = 0
        for i in range(len(nums)):
            mx_i = max(mx_i, nums[i])
            prefixGcd.append(EEA(nums[i], mx_i))
        
        prefixGcd.sort()
        ret = 0
        i, j = 0, len(prefixGcd) - 1
        while i < j:
            ret += EEA(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1
        
        return ret

        
