import heapq
def solution(scoville, K):
    # 힙으로 만듭니다.
    heapq.heapify(scoville)
    # 진행이 불가능해질때까지 진행합니다.
    cnt = 0
    while len(scoville) >= 2:
        # 조건을 만족하면 끝냅니다.
        if scoville[0] >= K:
            return cnt
        # 조건을 만족하지 못하면 변화시킵니다.
        heapq.heappush(scoville, (heapq.heappop(scoville)+2*heapq.heappop(scoville)))
        cnt += 1
    # 진행이 불가능하나 조건을 만족하면 끝냅니다.
    if scoville[0] >= K:
        return cnt
    # 진행이 불가능하면 -1을 리턴합니다.
    return -1
