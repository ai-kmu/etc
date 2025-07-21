class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int('0b' + a, base=2) + int('0b' + b, base=2))[2:]
