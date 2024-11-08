class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            tmp = []
            for s in str(n):
                tmp.append(int(s) ** 2)
            n = sum(tmp)
        return False
