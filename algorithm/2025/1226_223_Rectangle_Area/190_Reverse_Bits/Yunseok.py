class Solution:
    def reverseBits(self, n: int) -> int:
        num_bit = bin(n)
        reversed_str = ""
        for i in range(len(num_bit) - 1, 1, -1):
            reversed_str += num_bit[i]

        left_val = 34 - len(num_bit)
        for i in range(left_val):
            reversed_str += "0"

        return int(reversed_str, 2)
