# 풀다가 솔루션 봤습니다.
# 풀이 안해주셔도 됩니다..


class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:

        from itertools import permutations
        from math import ceil

        ans = float('inf')

        for perm in permutations(strength):
            t = 0
            x = 1
            for s in perm:
                t += ceil(s/x)
                x += k
            ans = min(ans, t)

        return ans
