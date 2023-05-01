class Solution:
    def maxJump(self, stones: List[int]) -> int:

        maxlen = 0
        # 돌이 두개 밖에 없을 경우 
        if len(stones) < 3:
            return stones[1] 
        
        # 돌이 두개 이상일 경우
        # length의 값은 min이여야 하기 때문에 돌다리를 건널 수 있는 방법은 바로 다음 혹은 그 다음 돌이다
        # 다음 다음 돌의 값이 더 큰 값일 것이기 때문에 현재 돌과 다음다음 돌의 값의 차를 구해 max를 취해 maxlen을 찾는다 
        for i in range(2, len(stones)):
            maxlen = max(stones[i]-stones[i-2], maxlen)
        
        return maxlen
