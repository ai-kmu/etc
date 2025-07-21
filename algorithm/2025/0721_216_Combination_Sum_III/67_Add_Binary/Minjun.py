class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        la = len(a) - 1
        
        lb = len(b) - 1
        sa = 0
        sb = 0
        for i in a:
            if i == '1':
                sa += 2 ** la
            la -= 1
        for j in b:
            if j == '1':
                sb += 2 ** lb
            lb -= 1
        c = sa + sb
        ans = ""
        while c > 0:
            ans = str(c % 2) + ans
            c = c // 2
        return ans
