# 풀이 실패
# 풀이 안 해주셔도 됩니다
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        data = [
            (a, "a"),
            (b, "b"),
            (c, "c"),
        ]

        pq = []

        for count, char in data:
            if count > 0:
                heapq.heappush(pq, (-count, char))

        res = [] 
...
