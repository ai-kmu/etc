# 힌트보고 풀었는데 왜 되는지 모르겠어요
class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        n = len(stones)
        if n == 2:
            return stones[-1]

        result = 0
        for i in range(0, n-2):
            dist = stones[i+2] - stones[i] 
            result = max(result, dist)
        return result
