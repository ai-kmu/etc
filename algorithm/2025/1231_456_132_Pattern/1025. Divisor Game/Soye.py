class Solution:
    def divisorGame(self, n: int) -> bool:
        ans = False

        if n%2 == 0:
            n = n-1
            ans = True

        return ans
