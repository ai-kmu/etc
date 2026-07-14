# 솔루션 참고...ㅜㅠ

import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = {}

        for i in answers:
            if i + 1 not in cnt:
                cnt[i + 1] = 1
            
            else:
                cnt[i + 1] += 1

        ans = 0

        for n in cnt:
            ans += math.ceil(cnt[n] / n) * n
        
        return ans
