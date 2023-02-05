# 아예 못풀겠어서 정답 보고 공부만 했습니다..

class Solution:
    def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for (L, R, H) in buildings]
        events += [(R, 0, 0) for (_, R, _) in buildings]
        events.sort()

        ans = [(0, 0)]
        live = [(0, float("inf"))]

        for (L, negH, R) in events:
            while live[0][1] <= L:
                heapq.heappop(live)
            if negH:
                heapq.heappush(live, (negH, R))
            if ans[-1][1] != -live[0][0]:
                ans.append((L, -live[0][0]))
        return ans[1:]
