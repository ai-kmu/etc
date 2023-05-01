class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # 두 칸씩하면 됨
        n = len(stones)

        if n == 2:
            return stones[-1] - stones[0]
        else:
            return max(stones[i] - stones[i-2] for i in range(2, n))
