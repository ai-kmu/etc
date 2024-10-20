class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(2 ** len(nums)):
            binstr = bin(i)[2:].zfill(len(nums))
            if binstr not in nums:
                return binstr
