# 풀다 안풀려서 참고하여 풀었음

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # events process

        events = [[L, -H, R] for L, R, H in buildings]
        # 정렬할 것인데, 단순 내림차순으로 정렬하기 위함
        events += [[R, 0, 0] for _, R, _ in buildings]

        events.sort()

        # res : result, [x, height]
        # live  : heapq, (-height, x) 가장 높이가 큰 건물이 먼저 오게 하고 x 좌표가 먼저 오게 함

        res = [[0, 0]]
        live = [(0, float('inf'))]

        for pos, negH, R in events:
            # step1, remove already ended event
            while live[0][1] <= pos: # 현재 pos보다 작으면 지워버림
                heapq.heappop(live)
            # step2. starting event => negH != 0 -> insert live
            if negH:
                heapq.heappush(live, (negH, R))
            # step3. prev height != highest height 인 경우에만 insert res

            if res[-1][1] != -live[0][0]:
                res.append([pos, -live[0][0]])

        return res[1:]
