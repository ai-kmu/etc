import heapq

def solution(scoville, K):
    answer = 0
    
    # 현재 리스트를 힙으로 변환
    heapq.heapify(scoville)
    
    while True:
        # 가장 맵지 않은 스코빌 지수를 min1에 넣음
        min1 = heapq.heappop(scoville)
        
        # 만약 min1이 k보다 크다면 heap에서 다시 min1을 가져옴
        if min1 >= K:
            break
        
        # 만약 scoville 힙이 아무것도 없으면 -1을 answer에 넣음
        elif len(scoville) == 0:
            answer = -1
            break
        
        # 두 번째로 매운 수치를 min2에 저장
        min2 = heapq.heappop(scoville)
        
        # 섞은 음식의 스코빌 지수 계산
        new_scoville = min1 + 2 * min2
        
        # 섞은 음식을 heap에 넣음
        heapq.heappush(scoville, new_scoville)
        
        # 섞은 횟수를 1을 더해줌
        answer += 1
    
    return answer
