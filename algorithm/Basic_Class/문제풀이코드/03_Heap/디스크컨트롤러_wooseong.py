import heapq as hq

def solution(jobs):
    num_job = len(jobs)
    # 예외: 개수가 하나면 걸리는 시간이 답임
    if len(jobs) == 1:
        return jobs[0][1]
    
    # 처리할 수 있는 애들 중에 소요 시간이 짧은 앨 넣어줄 heap
    heap = []
    
    # prev: 이전에 한 작업의 시작 시각
    # curr: 현재 시각
    prev = -1
    curr = 0
    
    # do: 처리한 작업 수, 다 할 때까지 while
    do = 0
    answer = 0
    while do < len(jobs):
        # 현재 처리 가능한 요청만 heap에 삽입
        for (req, dur) in jobs:
            # 현재 처리할 수 있으려면
            # 이전 작업 요청 시각 < 이번 작업 요청 시각 <= 현재 시각
            if prev < req <= curr:
                # 기준이 소요 시간이므로 dur, req로 뒤집어서 넣기
                hq.heappush(heap, (dur, req))
                
        # heap이 있으면
        # 1. curr == 현재 시각 == 이전 작업 완료 시각 ==> prev
        # 2. 현재 시각 (curr) 업데이트: 이번 작업 소요 시간만큼
        # 3. curr == 현재 시각 == 이번 작업 완료 시각
        #    따라서 answer += (curr - req)
        # 4. 작업 하나 했으니 do += 1
        if heap:
            (dur, req) = hq.heappop(heap)
            prev = curr
            curr += dur
            answer += (curr - req)
            do += 1
        # 없으면
        # 아직 못하는 거니까 curr += 1
        else:
            curr += 1
            
    
    # 답은 평균 내림한 거
    return int(answer // num_job)
