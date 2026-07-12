from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # answer[i]라고 말한 토끼 : i + 1 배수만큼 있어야함
        # 1이라고 답변 -> 최소 2마리, 1이 3개 있으면, 4마리 있어야함 -> 답변 + 1의 배수만큼
        cnt = Counter(answers)
        return sum([(k + 1) * math.ceil(v / (k + 1)) for k, v in cnt.items()])
