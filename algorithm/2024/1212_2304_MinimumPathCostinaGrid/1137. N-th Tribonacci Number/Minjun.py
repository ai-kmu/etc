class Solution:
    def tribonacci(self, n: int) -> int:
        j = [0, 1, 1]
        def cal(a,b,c):
            t = a + b + c
            return t
        for i in range(n):
            j.append(cal(j[i],j[i+1],j[i+2]))
        return j[-3]
