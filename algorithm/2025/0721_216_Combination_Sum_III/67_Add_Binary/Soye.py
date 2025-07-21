class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            tmp = a^b
            add = (a&b) << 1
            a, b = tmp, add

        ans = bin(a)[2:]

        return ans
