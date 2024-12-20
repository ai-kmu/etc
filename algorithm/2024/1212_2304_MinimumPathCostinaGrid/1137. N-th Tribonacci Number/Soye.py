class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        if n < 3:
            return a[n]
        else:
            for i in range(3, n+1):
                tmp = a[i-1] + a[i-2] + a[i-3]
                a.append(tmp)
        
        return a[n]
