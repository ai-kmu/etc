class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0

        n = len(piles) // 3
        idx = len(piles) - 2

        for _ in range(n):
            ans += piles[idx]
            idx -= 2
        return ans
