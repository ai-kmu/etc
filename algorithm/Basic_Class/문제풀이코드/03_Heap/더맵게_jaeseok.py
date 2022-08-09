import heapq

def solution(scoville, K):
    answer = 0
    # 스코빌 list heapify
    heapq.heapify(scoville)
    while True:
        # 제일 낮은 숫자를 pop
        min1 = heapq.heappop(scoville)
        # 만약 제일 낮은 숫자가 최소 스코빌 지수보다 높다면 모든 음식이 K보다 높다는 의미이므로 break
        if min1 >= K:
            break
        # scoville을 전부 섞어도 최소 스코빌 지수에 도달할 수 없는 경우는 -1을 return
        elif not scoville:
            answer = -1
            break
        # 두 번째로 낮은 숫자를 heappop
        min2 = heapq.heappop(scoville)
        # 새로운 스코빌 지수는 두 번째 음식의 스코빌에서 2를 곱한 것을 첫 번째 음식의 스코빌에서 더한 것
        new_scoville = min1 + (2 * min2)
        # 새로운 스코빌을 heappush하고 answer에 1 추가
        heapq.heappush(scoville,new_scoville)
        answer += 1
    return answer
