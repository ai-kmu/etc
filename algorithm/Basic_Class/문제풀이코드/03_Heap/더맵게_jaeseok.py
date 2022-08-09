import heapq

def solution(scoville, K):
    answer = 0
    # scoville heapify
    heapq.heapify(scoville)
    while len(scoville) > 1:
        # 제일 작은 스코빌 heappop
        sco1 = heapq.heappop(scoville)
        # 제일 작은 스코빌이 K보다 높으면 모든 스코빌이 K보다 높으므로 break
        if sco1 >= K:
            break
        # 두 번째로 작은 스코빌 heappop
        sco2 = heapq.heappop(scoville)
        # 새로운 스코빌을 생성하고 heappush
        nsco = sco1 + sco2 * 2
        heapq.heappush(scoville, nsco)
        # 한 번 스코빌을 섞을 때마다 answer에 1씩 추가
        answer += 1
    
    # 루프를 다 돌았는데도 제일 작은 스코빌이 K보다 작으면 -1 return
    if heapq.heappop(scoville) < K:
        return -1
    return answer
