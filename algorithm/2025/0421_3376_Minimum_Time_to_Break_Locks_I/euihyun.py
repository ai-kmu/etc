#못풀었수... 솔루션 봤수.
#리뷰안해주셔도 됩니다.

from functools import lru_cache
from typing import List
from math import ceil, inf

class Solution:
    def findMinimumTime(self, strength: List[int], k: int, x=1) -> int:
        
        
        @lru_cache(None)
        def minTime(x: int, mask: int, mn=inf) -> int:
        
            if mask.bit_count() == n:
                return 0

            time = []

            for i, s in enumerate(strength):
                if mask & (1 << i):  
                    continue

                time.append(ceil(s / x) + minTime(x + k, mask | (1 << i)))

            return min(time)

        n = len(strength) 

        
        return minTime(x, 0)
