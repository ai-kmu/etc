class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        # 돌이 4개보다 없으면 마지막에서 처음 가는게 제일 큼
        if n < 4:
            return stones[-1] - stones[0]
        
        max_jump = 0
        # 인접한 돌을 건너 가면서 와야 minimum cost 를 찾을수 있음
        for i in range(n-2):
            jump = stones[i+2] - stones[i]
            max_jump = max(jump,max_jump)
        
        return(max_jump)
