class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            tmp = [0 for i in range(len(nums)//2)]
            t, a, b, eo = 0, 0, 0, 0
            for idx, i in enumerate(nums):
                if t == 0:
                    t += 1
                    a = i
                else:
                    b = i
                    if eo == 0:
                        tmp[idx//2] = min(a, b)
                    else:
                        tmp[idx//2] = max(a, b)

                    t, a, b = 0, 0, 0
                    
                    if eo == 0:
                        eo = 1
                    else:
                        eo = 0
                
            nums = tmp

        return nums[0]
        
