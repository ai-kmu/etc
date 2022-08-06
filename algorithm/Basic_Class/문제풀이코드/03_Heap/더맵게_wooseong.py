import heapq as hq

def solution(scoville, K):
    # min heap 사용: 작은 거 두 개를 뽑기 위함
    hq.heapify(scoville)
    
    answer = 0
    # 가장 작은 게 K보다 작고 heap에 두 개 이상 남았을 때
    while (scoville[0] < K) and (len(scoville) >= 2):
        # 작은 거 두 개 뽑고 섞기
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        new = first + 2 * second
        answer += 1
        # 섞은 거 넣기
        hq.heappush(scoville, new)
    
    # 가장 작은 게 여태 K보다 작다 == 불가능하다
    return -1 if scoville[0] < K else answer
