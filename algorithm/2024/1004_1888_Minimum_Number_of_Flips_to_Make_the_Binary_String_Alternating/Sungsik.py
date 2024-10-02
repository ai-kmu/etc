class Solution:
    def minFlips(self, s):
        n = len(s)
        e, o = (n + 1) // 2, n // 2
        x = s[::2].count('1') - s[1::2].count('1')
        ans = min(e - x, o + x)
        if n&1 == 0: return ans
        for i in s:
            x = 2 * int(i) - x
            ans = min(ans, e - x, o + x)
        return ans
