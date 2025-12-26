class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        num = str(bin(n))[2:]
        num = str(num).zfill(32)

        reverse_num = ""

        for i in num[::-1]:
            reverse_num += i

        return int(reverse_num, 2)
