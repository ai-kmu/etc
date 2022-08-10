import heapq

def solution(jobs):
    n = len(jobs)
    answer = 0
    start = -1
    end  = 0
    i = 0
    q = []
    # 작업이 전부 수행될 때까지 while문 수행
    while i != n:
        for job in jobs:
            # 이전의 작업의 수행 중에 들어올 수 있는 새로운 작업들을 heap에 추가, 이때 작업의 수행 시간이 기준이 됨
            if start < job[0] <= end:
                heapq.heappush(q, (job[1], job[0]))
        # 힙에 작업이 들어가 있으면 heappop해서 start와 end를 갱신
        if q:
            time, n_start = heapq.heappop(q)
            # 새로운 start는 전 작업이 끝나는 시간 or 그 시간에서 대기시간이 추가된 형태
            start = end
            # 새로운 end는 새로운 작업이 끝나는 시간
            end += time
            # 요청부터 종료까지 걸린 시간이 answer에 더해짐
            answer += (end - n_start)
            # 작업을 하나 수행했으므로 i 추가
            i += 1
        else:
            # 어떠한 작업도 없는 상태에서는 대기시간 1초 추가
            end += 1
            
                
    return answer // n
