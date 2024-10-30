class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        appear = [0] * (2 ** n)
        
        # 등장한 숫자를 appear에 저장
        for num in nums:
            appear[int(num, 2)] = 1
        
        # 처음으로 안 등장한 숫자를 binary string 형태로 치환한 후 return
        for i, a in enumerate(appear):
            if not a:
                bin_str = "{0:b}".format(i)
                length = len(bin_str)
                return '0' * (n - length) + bin_str
