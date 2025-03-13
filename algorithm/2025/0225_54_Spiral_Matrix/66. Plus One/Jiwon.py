class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        d = 10 ** (len(digits) - 1)
        for i in digits:
            num += (i * d)
            d //= 10

        num += 1
        ans = []
        for i in str(num):
            ans.append(int(i))
        return ans
        
