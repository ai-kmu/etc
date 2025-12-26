class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n).lstrip('-0b')
        while len(a) < 32:
            a = "0"+str(a)
        return int(a[::-1],2)
