class Solution:
    def maxJump(self, stones: List[int]) -> int:
        return max([stones[1] - stones[0]] + [stones[i] - stones[i-2] for i in range(2, len(stones))])
