# 황달 개구리의 최소 점프 여행기...
# 제일 인접한 돌로 뛰어야 최소 점프가 되는데 그렇다고 바로 옆 돌로만 뛰면,
# 돌아올 때 마지막 돌에서 첫번째 돌로 한 번에 뛰어야 되기 때문에 최대 경로가 되버린다.
# 따라서, 하나 건너띄어 뛰어야 한다.
# 황달개구리 파이팅

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        polzzak = 0
        if len(stones) == 2:
            return stones[-1]
        for i in range(len(stones)-2):
            if polzzak < stones[i+2] - stones[i]:
                polzzak = stones[i+2] - stones[i]
        return polzzak
            
