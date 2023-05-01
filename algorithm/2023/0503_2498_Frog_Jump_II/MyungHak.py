# 결국 최대값을 가장 줄이려면 아래와 같이 움직여야 함
# 0번째 --> 2번째 --> 4번째 --> .... n번째 --> n-2번째 --> n-4번째 --> ... --> 0번째
# 결국 2칸씩 띄워가면 거리 측정한 다음 최대값 return하면 ㅗ딤

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) < 3:
            return stones[-1]
          
        return max([stones[i]-stones[i-2] for i in range(2, len(stones))])
