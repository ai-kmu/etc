class Solution(object):
    def flipLights(self, n, presses):
        if presses == 0:
            return 1
        m = min(n, 6)
        seen = set()
        for mask in range(16):
            b1 = (mask >> 0) & 1
            b2 = (mask >> 1) & 1
            b3 = (mask >> 2) & 1
            b4 = (mask >> 3) & 1
            cnt = b1 + b2 + b3 + b4
            if cnt > presses or ((presses - cnt) & 1):
                continue
            s = []
            for i in range(1, m + 1):
                t = b1 ^ (b2 & (i % 2 == 0)) ^ (b3 & (i % 2 == 1)) ^ (b4 & ((i - 1) % 3 == 0))
                s.append('0' if t else '1')
            seen.add(''.join(s))
        return len(seen)
