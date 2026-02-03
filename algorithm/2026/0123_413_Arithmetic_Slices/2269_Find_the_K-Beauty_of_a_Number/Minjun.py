class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0

        for i in range(len(str(num))-k+1):
            a = str(num)[i:i+k]
            print(a, ans)
            if not a:
                a = "0"*k
                continue
            if int(a) != 0 and num % int(a) == 0:
                ans += 1
            
        return ans
