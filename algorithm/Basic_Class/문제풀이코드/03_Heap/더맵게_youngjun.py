import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) >= 2:
        f_spicy = heapq.heappop(scoville)
        
        if f_spicy >= K:
            break
        else:
            s_spicy = heapq.heappop(scoville)
            heapq.heappush(scoville, f_spicy + (2 * s_spicy))
            answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer
