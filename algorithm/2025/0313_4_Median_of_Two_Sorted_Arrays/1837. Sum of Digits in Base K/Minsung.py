class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = ''
        cnt = 8
        while True:
            if cnt == -1: break
            t = n // int(k**cnt)
            cnt -= 1
            if ans=='' and t==0:
                continue
            n -= t*(k**(cnt+1))
            ans += str(t)
        res = 0
        for i in ans:
            res += int(i)
        return res

        # 34 // 6**2 = 0
        # 34 // 6**1 = 5
        # 34 // 6**0
