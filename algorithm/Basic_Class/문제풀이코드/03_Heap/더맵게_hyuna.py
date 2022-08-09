import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    # scoville의 0번째 인덱스는 최소값이기 때문에 최소값이 K보다 크거나 힙의 크기가 2보다 클때까지 진행한다
    while scoville[0] < K and len(scoville) >= 2:
        # 가장 맵지 않은 음식과 그 다음으로 맵지 않은 음식의 스코빌 지수를 가지고 새로운 음식의 지수를 구한다
        pop1 = heapq.heappop(scoville)
        pop2 = heapq.heappop(scoville)
        temp = pop1 + (pop2 * 2)
        
        # 새로운 지수를 다시 힙에 추가하고 섞은 횟수를 증가시킨다
        heapq.heappush(scoville, temp)
        answer += 1
        
    # 최소 스코빌 지수가 K보다 작다면 -1을 리턴한다
    if scoville[0] < K:
        answer = -1
        
    return answer
