# 솔루션 참고
# https://algo.monster/liteproblems/1888
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        target = "01"
        # cnt: 010101...과 일치하지 않는 index 수
        cnt = sum(c != target[i & 1] for i, c in enumerate(s))
        # n - cnt: 101010...과 일치하지 않는 index 수
        ans = min(cnt, n - cnt)
        for i in range(n):
            cnt -= s[i] != target[i & 1]
            cnt += s[i] != target[(i + n) & 1]
            ans = min(ans, cnt, n - cnt)
        return ans
