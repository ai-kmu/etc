class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_val = int(a, base=2) + int(b, base=2)
        return format(sum_val, 'b')
