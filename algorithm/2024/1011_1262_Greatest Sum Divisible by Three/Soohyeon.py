class Solution(object):
    def maxSumDivThree(self, nums):
        sums = [0, 0, 0] 

        for num in nums:
            modSums = []

            for i in range(3):
                modSums.append(sums[i] + num)
            
            for i in range(3):
                mod = modSums[i] % 3
                sums[mod] = max(sums[mod], modSums[i]) 
        return sums[0]