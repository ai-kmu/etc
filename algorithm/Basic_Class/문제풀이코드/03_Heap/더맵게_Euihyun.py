import heapq
def solution(scoville, K):
    answer = 0
    # 힙으로 만들고
    heapq.heapify(scoville)
    
    # 최대만큼 돌리면서
    for i in range(1000000):
        # scoville 에 heappop 한거 + heappop*2 한거 추가
        scoville.append(heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        # 정답 갯수 늘려주고
        answer += 1
        
        # scoville[0]이 >k 보다 크면 정답생긴거니 멈춤
        if scoville[0] >= K :
            break
        # scoville이 2개보다 적게 되면 만들수 없으니 -1 반환후 멈춤
        if len(scoville) <= 2:
            answer = -1
            break
    
    return answer
