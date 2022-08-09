# 테스트20만 통과한 5점짜리 코드...
import heapq

def solution(jobs):
    # 뒤집어서 넣을 new_jobs
    new_jobs= []
    
    start = []
    # 요청부터 종료까지 시간을 위해 총길이
    # 처음은 0 더해주기 위해서 0으로
    days = [0]
    # 계산값들 넣어주기
    avg = []
    n = len(jobs)
    
    # 뒤집어서 heapq 생성
    for i in jobs:
        heapq.heappush(new_jobs, i[::-1])
    
    # 뒤집은거에서 하나씩 빼서
    # 시작 시간 넣어주고
    # 요청으로 부터 종료시간 계산을 위해 총길이 
    # 계산값 다시 넣어주기
    # 남은거 없을때 종료
    while True:
        hq = heapq.heappop(new_jobs)
        start.append(hq[1])
        days.append(hq[0] + days[-1])
        avg.append(days[-1] - start[0])
        start.pop()
        if len(new_jobs) == 0:
            break
        
    # 평균 
    return sum(avg)/n
