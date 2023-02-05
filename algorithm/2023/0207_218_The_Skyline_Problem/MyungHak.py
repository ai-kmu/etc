# 풀이 실패

# 풀이 안해주셔도 됩니다


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, None) for _, R, _ in buildings})
        events.sort()
        
        res = [[0, 0]]
        hp = [(0, float("inf"))]
        for pos, negH, R in events:
            while pos >= hp[0][1]:
                heappop(hp)
            
            if negH:
                heappush(hp, (negH, R))
                
            if res[-1][1] != hp[0][0]:
                res.append([pos, -hp[0][0]])
        
        return res[1:]
