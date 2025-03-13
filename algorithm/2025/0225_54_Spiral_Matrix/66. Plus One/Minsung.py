class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ''.join([str(x) for x in digits])
        digit = int(digit) + 1
        ans = list()
        while digit != 0:
            ans.append(digit%10)
            digit = digit // 10
        
        ans = ans[::-1]
        return ans
