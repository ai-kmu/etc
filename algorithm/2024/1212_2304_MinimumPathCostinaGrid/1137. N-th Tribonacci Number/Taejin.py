class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0, 1, 1]

        for i in range(n - 2):
            seq.append(sum(seq[-3:]))

        return seq[n]
        
